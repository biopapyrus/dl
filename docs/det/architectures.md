# 代表的なアーキテクチャ


## R-CNN


R-CNN (regions with CNN features) {cite}`ref_rcnn` は、物体検出のための深層学習アーキテクチャです（{numref}`rcnn_arch`）。R-CNN では、入力画像に対して selective search {cite}`ref_selsearch` と呼ばれるアルゴリズムを適用し、物体らしい領域を約 2,000 個の候補として抽出します。次に、これらの候補領域を CNN に入力し特徴抽出を行います。抽出された特徴は、最終的にサポートベクトルマシン（SVM）に入力して分類を行います。

```{figure} ../_static/rcnn_arch.png
---
name: rcnn_arch
width: 70%
---
R-CNN のアーキテクチャ。Girshick et al{cite}`ref_rcnn` Figure 1 より転載。
```

R-CNN は、従来の物体検出手法に比べて高い精度を達成しましたが、いくつかの課題もありました。一つは、学習および推論の処理に非常に時間がかかる点です。1 枚の画像で物体検出を行うだけでも膨大な計算リソースを必要とし、リアルタイム処理や動画解析には適していませんでした。また、候補領域を生成する selective search は、手作業で設計されたアルゴリズムであり、学習によって最適化されるものではありません。その結果、画像の特徴が変化した場合に柔軟に対応できず、適切な候補領域を見逃すリスクがありました。これらの課題を解決するために、後続の手法である Fast R-CNN{cite}`ref_fastrcnn` や Faster R-CNN{cite}`ref_fasterrcnn` が開発されました。


## Fast R-CNN

Fast R-CNN {cite}`ref_fastrcnn` は、物体検出に用いられる深層学習アーキテクチャで、R-CNN {cite}`ref_rcnn` の改良版として提案されました。この手法は、R-CNN と同様に selective search アルゴリズム {cite}`selsearch`を用いて物体候補領域（Regions of Interest; RoI）を生成し、それらを分類することで物体を検出しています。しかし、R-CNN とは異なり、特徴量抽出の方法と処理の流れを効率化することで、大幅な速度向上を実現しています。

R-CNN では、各候補領域に対して個別に CNN を適用し特徴量を抽出していましたが、Fast R-CNN ではまず画像全体に対して一度だけ CNN を適用し、convolution feature map を生成します（{numref}`fig-fastrcnn_arch`）。次に、この各候補領域の特徴量をこの convolution feature map から抽出しています。これにより、CNN を利用した処理回数を大幅に削減することができました。また、R-CNN が浅いニューラルネットワークを使用していたのに対し、Fast R-CNN は VGG16 などの深層ニューラルネットワークを使用し、より表現力の高い特徴を学習できるようになりました。


```{figure} ../_static/fastrcnn_arch.png
---
name: fig-fastrcnn_arch
width: 80%
---
Fast R-CNN のアーキテクチャ。Girshick et al{cite}`ref_fastrcnn` Figure 1 より転載。
```

分類の出力では、ソフトマックス関数を用いて各候補領域がどのクラスに属するかを判定します。一方、位置回帰の出力では、バウンディングボックスの位置情報を示す実数値を予測します。これら 2 つのタスクを 1 つのモデルで同時に最適化することで、計算コストを下げながら高性能を実現しています。



## Faster R-CNN

Faster R-CNN {cite}`ref_fasterrcnn` は、R-CNN {cite}`ref_rcnn` や Fast R-CNN {cite}`ref_fastrcnn` を改良した物体検出アルゴリズムです。これらの先行手法では、物体の位置を検出するために selective search {cite}`ref_selsearch` というアルゴリズムを使用していましたが、この処理が非常に時間を要するものでした。これに対して、Faster R-CNN では、物体の位置検出とクラス判定の両方を CNN で行う仕組みを取り入れました。selective search を排除することで、アルゴリズム全体の処理速度を大幅に向上させました。

Faster R-CNN のアーキテクチャは次のように動作します。まず、入力画像は CNN（一般的には VGGNet や ResNet）を通じて 特徴マップ に変換されます（{numref}`fig-fasterrcnn_arch`）。次に、この特徴マップを Region Proposal Network (RPN) に入力し、物体の候補領域（バウンディングボックス）を推定します。その後、推定された領域情報と特徴マップを RoI pooling 層に渡し、物体のクラスと位置情報を最終的に判定します。

```{figure} ../_static/fasterrcnn_arch.png
---
name: fig-fasterrcnn_arch
width: 50%
---
Faster R-CNN のアーキテクチャ。Ren et al{cite}`ref_fasterrcnn` Figure 2 より転載。
```

特徴マップが RPN に渡されると、RPN は特徴マップ全体に対して小さな n×n のスライディングウィンドウを適用します（{numref}`fig-fasterrcnn_rpn`）。各スライディングウィンドウの中央を基準点（アンカー）として、複数の仮想的なバウンディングボックス（anchor boxes）を生成します。たとえば、1 つのアンカーにつき k 種類の異なるサイズやアスペクト比の anchor boxes が作られます。これらの anchor boxes は、RPN 内の 2 つの分岐（cls 層と reg 層）でそれぞれ処理されます。cls 層では、各 anchor box に物体が含まれている確率を出力します（物体あり/なしの分類）。reg 層では、各 anchor box の座標（位置と大きさ）を微調整して、より適切なバウンディングボックスを生成します。このプロセスにより、RPN は画像中の物体候補領域を効率的に生成します。

```{figure} ../_static/fasterrcnn_rpn.png
---
name: fig-fasterrcnn_rpn
width: 60%
---
Faster R-CNN RPN のアーキテクチャ。Ren et al{cite}`ref_fasterrcnn` Figure 3 より転載。
```

RPN で生成された候補領域（バウンディングボックス）は、元の特徴マップとともに RoI pooling 層に渡されます。この層では、候補領域に該当する部分の特徴マップを固定サイズ（例: 7×7）にリサイズし、全結合層に入力できる形式に整えます。

次に、この特徴ベクトルを全結合層を通じて、ソフトマックス層と回帰層に渡されます。ソフトマックス層では、各候補領域に含まれる物体のクラス（例: 犬、車など）を推定します。また、回帰層では、バウンディングボックスの位置をさらに精密に調整します。この設計により、Faster R-CNN は、物体検出において高速かつ高精度な性能を実現しています。PASCAL VOC や COCO のようなベンチマークデータセットで高い精度を達成しており、画像分類や物体検出タスクにおける重要な基盤となっています。




## YOLO

YOLO (You Only Look Once) {cite}`ref_yolo` は、物体検出における代表的な one-stage method のアルゴリズムです。従来の R-CNN 系列の two-stage method とは異なり、YOLO は画像を一度に処理し、物体の位置とクラスを同時に推定します。画像全体を一度に処理することで、物体間の空間情報も活用できる点が特長です。この仕組みにより、YOLO は検出精度を高めるだけでなく、リアルタイム処理が求められる応用にも対応可能な速度を実現しています。

YOLO の処理では、まず入力画像を S&times;S のグリッドに分割します。次に、グリッドで分割された各領域（グリッドセル）に対して、あらかじめ設定された B 個のバウンディングボックス（anchor boxes）を割り当てます。各バウンディングボックスには、その領域に物体が含まれている確率（信頼スコア, $ P(\text{object}) $）と、バウンディングボックスの座標（中心座標、幅、高さ）を予測する役割があります。信頼スコアは、バウンディングボックス内に検出対象の物体が含まれている場合は 1.0、背景である場合は 0.0 に近い値を取るように学習されます。さらに、各グリッドセルにおいて、物体が存在すると仮定した場合にそれがどのカテゴリに属するかを示す条件付き確率 $ P(\text{class|object}) $ を計算します。この条件付き確率と信頼スコア $ P(\text{object}) $ を掛け合わせることで、それぞれのバウンディングボックスがどのクラスに属する物体を含んでいるかを推定します。

```{figure} ../_static/yolo_arch.png
---
name: yolo_arch
width: 85%
---
YOLO のアーキテクチャ。Redmon et al[^yolo] Figure 2 より編集。
```

YOLO では、バウンディングボックスの座標、信頼スコア、そして分類時の条件付き確率が正解ラベルとどれだけ異なるかを計算計算し、これらを単一の損失関数にまとめて評価・最適化します。これにより、全ての予測を一括で行うことが可能となり、R-CNN 系で必要とされた候補領域の生成や特徴抽出といった段階的な処理が不要になり、大幅な速度向上が実現されました。

YOLO の初期バージョン（YOLOv1）は、シンプルなアーキテクチャながら、高速かつ高精度な物体検出を実現しました。ただし、小さな物体や複数の物体が重なった状況での検出には課題がありました。その後、改良が進み、例えば anchor boxes の導入や、異なる解像度で物体を検出可能にするマルチスケール検出機能の追加により、精度が大幅に向上しました。

YOLO、YOLOv2 {cite}`ref_yolov2` および YOLOv3 {cite}`ref_yolov3` は、オリジナルの開発者である Joseph Redmon らによって発表されました。しかし、Redmon は倫理的な懸念などから開発を中止しました。その後も YOLO の名を冠した新たなバージョンのアーキテクチャが複数の研究者や団体によって開発されています。

YOLOv4 および YOLOv7 は、YOLO のベースフレームワークである Darknet を管理している Bochkovskiy らによって発表されました。YOLOv5、YOLOv8、YOLOv11 は、スペインの Ultralytics 社 によって開発され、PyTorch をベースに実装されています。YOLOv6 は、中国の Meituan（美団）社 によって発表され、主に産業用途での実用性を考慮して設計されました。YOLOv9 は、YOLOv4 や YOLOv7 に携わった研究者たちが開発しました。YOLOv10 は、清華大学の研究者グループによって開発され、新しいアーキテクチャが採用されています。

このように、YOLO の名称は共通ですが、各バージョンの開発元は異なり、使用されている技術や特徴、ライセンス形態も異なります。そのため、YOLO を利用する際は、性能や機能だけでなく、ライセンス条件についても事前に確認することが重要です。



## SSD

SSD (Single Shot MultiBox Detector) {cite}`ref_ssd` は、画像全体を一度に処理して物体の位置（バウンディングボックス）とクラスを同時に推定する仕組みを採用しています。SSD は、YOLO に続く one-staeg method 代表的な手法の一つです。

SSD のアーキテクチャは、特徴マップを活用して物体を検出します。ベースとなる畳み込みニューラルネットワーク（例えば VGG16）が画像から特徴を抽出し、その後の畳み込み層で異なる解像度の特徴マップを生成します（{numref}`ssd_arch`）。これらのマップを用いて、異なるスケールの物体を検出可能にしています。具体的には、低解像度のマップは大きな物体の検出に、高解像度のマップは小さな物体の検出に適しています。また、各特徴マップ上で複数のデフォルトバウンディングボックス（default boxes）を事前に定義しており、各ボックスに対してクラスと位置を同時に予測します。


```{figure} ../_static/ssd_arch.png
---
name: ssd_arch
width: 98%
---
SSD のアーキテクチャ。Liu et al[^ssd] Figure 1 より編集。
```

SSD にはいくつかの課題もあります。例えば、小さな物体や密集した物体を検出する場合、精度が低下する傾向があります。また、低解像度の特徴マップに依存する物体検出では、細部情報が失われる可能性があり、細かい検出が求められる応用では精度が課題となります。これらの問題を解決するため、後続の改良版（例: SSD512、FSSD）が提案されてきました。



## RetinaNet


RetinaNet  {cite}`ref_retinanet` は、物体検出の分野で one-stage method の性能を大きく向上させたアルゴリズムの一つです。従来、two-stage method（例: Faster R-CNN）は高い精度を実現する一方で処理速度が遅く、one-stage method（例: SSD、YOLO）は高速だが精度で劣るとされていました。RetinaNet は、Focal Loss と呼ばれる新しい損失関数を導入することで、one-stage method における精度の課題を克服し、速度と精度のバランスを大幅に改善しました。

RetinaNet のアーキテクチャは、画像から特徴を抽出するバックボーンネットワーク（例: ResNet）と、特徴マップの中で物体を検出するための Feature Pyramid Network (FPN) で構成されています。FPN により、異なる解像度の特徴マップを利用して、大きな物体から小さな物体まで効率的に検出することができます。これに加え、各特徴マップ上でアンカーボックス（anchor boxes）を使用して、物体の位置とクラスを同時に予測します。

RetinaNet の最大の特徴は、Focal Loss にあります。この損失関数は、one-stage method におけるクラス不均衡問題に対処するために設計されました。従来の損失関数では、検出対象物が少なく背景の例が圧倒的に多いため、検出が困難な小さな物体や曖昧な物体が誤って無視されることが多くありました。Focal Loss は、難しい例に重点を置き、簡単な例の影響を抑えることで、検出精度を大幅に向上させています。


[^retinanet]: Lin T, Goyal P, Girshick R, He K, Dollár P. Focal Loss for Dense Object Detection. *arXiv* 2018. DOI:[https://doi.org/10.48550/arXiv.1708.02002]()


## 参照文献

```{bibliography} ../references.bib
:filter: docname in docnames
:style: plain
```

