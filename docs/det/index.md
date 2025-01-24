# 物体検出


物体検出タスクでは、画像内に存在する物体を分類するだけでなく、それらの物体がどこにあるのか（バウンディングボックスの座標）を特定する必要があります。初期の物体検出手法では、物体らしき領域を推定して切り出し、その領域を分類する two-stage method が一般的でした。代表的な手法として Faster R-CNN {cite}`ref_fasterrcnn` が挙げられます。その後、計算リソースの制約を考慮し、物体の座標推定と分類を一度に最適化する one-stage method が登場しました。代表的な手法には、YOLO（You Only Look Once）{cite}`ref_yolo` や SSD（Single Shot MultiBox Detector）{cite}`ref_ssd` があります。Two-stage method と one-stage method は、目的によって使い分けられています。例えば、精度が最優先されるタスク（医療画像解析や高精度な監視システムなど）では two-stage method が選ばれることが多い一方、リアルタイム性が求められるタスクでは one-stage method が適しています。



```{bibliography} ../references.bib
:filter: docname in docnames
:style: plain
```


