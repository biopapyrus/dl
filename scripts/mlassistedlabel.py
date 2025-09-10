import os
import argparse
import urllib
import PIL.Image
import torch
import torchvision
import label_studio_ml
import label_studio_ml.model
import label_studio_ml.api


ML_BACKEND_PATH = ''
LS_DATA_DIR = ''


def fasterrcnn(num_classes, weights=None):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights='DEFAULT')
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    num_classes = num_classes + 1  # class + background
    model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)
    if weights is not None:
        model.load_state_dict(torch.load(weights))
    return model


class MLBASE(label_studio_ml.model.LabelStudioMLBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # laebl config
        self.LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT = os.getenv('LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT')
        from_name, schema = list(self.parsed_label_config.items())[0]
        self.from_name = from_name
        self.to_name = schema['to_name'][0]
        self.labels = schema['labels']

        # model settings
        self.version = '0.0.0'
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model = fasterrcnn(1, ML_BACKEND_PATH)
        self.model.to(self.device)
        self.model.eval()
        

    def fit(self, *args, **kwargs):
        return {'labels': '', 'model_file': ''}
    

    def predict(self, tasks, **kwargs):
        
        # input images
        target_images = []
        for task in tasks:
            target_images.append(self.__abspath(task['data']['image']))

        input_tensors = self.__transform(target_images)

        # predictions
        pred_outputs = self.model(input_tensors)

        # format
        for i in range(len(pred_outputs)):
            pred_outputs[i] = self.__convert(target_images[i], pred_outputs[i])
        
        return pred_outputs

        
    def __abspath(self, filename):
        if '/data/local-files/?d=' in filename:
            filename = filename.replace('/data/local-files/?d=', '')
            if self.LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT is not None:
                filename = os.path.join(self.LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT, filename)
        elif '/data/upload/' in filename:
            filename = filename.replace('/data/', '')
            filename = os.path.join(LS_DATA_DIR, 'media', filename)
        else:
            print('Warning: cannot recognize the file path format.')
            print(filename)
            print('-----------')
        return urllib.parse.unquote(filename)
    

    def __transform(self, images):
        image_tensors = []
        for image in images:
            tensor = torchvision.transforms.functional.to_tensor(
                PIL.Image.open(image).convert('RGB')
            )
            image_tensors.append(tensor)
        return torch.stack(image_tensors).to(self.device)
        

    def __convert(self, image, pred_outputs, threshold=0.6):
        im = PIL.Image.open(image).convert('RGB')

        bboxes = pred_outputs['boxes'][pred_outputs['scores'] > threshold].detach().cpu().numpy()
        labels = pred_outputs['labels'][pred_outputs['scores'] > threshold].detach().cpu().numpy()
        scores = pred_outputs['scores'][pred_outputs['scores'] > threshold].detach().cpu().numpy()
        
        obj_instances = []
        for bbox, label, score in zip(bboxes, labels, scores):
            x1, y1, x2, y2 = bbox
            w = float((x2 - x1) / im.width * 100)
            h = float((y2 - y1) / im.height * 100)
            x = float(x1 / im.width * 100)
            y = float(y1 / im.height * 100)

            obj_instances.append({
                'from_name': self.from_name,
                'to_name': self.to_name,
                'type': 'rectanglelabels',
                'original_width': im.width,
                'original_height': im.height,
                'value': {
                    'rectanglelabels': [self.labels[int(label) - 1]],
                    'x': x,
                    'y': y,
                    'width': w,
                    'height': h,
                    'score': float(score),
                }
            })

        return {
            'result': obj_instances,
            'score': 1.0,
            'model_version': self.version,
        }



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8082)
    parser.add_argument('--weight', type=str, required=True)
    parser.add_argument('--data-dir', type=str, required=True)
    args = parser.parse_args()

    ML_BACKEND_PATH = args.weight
    LS_DATA_DIR = args.data_dir
    app = label_studio_ml.api.init_app(
        model_class=MLBASE,
        model_dir=os.path.dirname(__file__)
    )
    app.run(host=args.host, port=args.port, debug=True)

