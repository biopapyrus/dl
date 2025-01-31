# 物体検出


物体検出タスクでは、画像内に存在する物体を分類するだけでなく、それらの物体が存在している位置を囲んだ矩形（バウンディングボックス）の座標を特定する必要があります。このタスクには、物体の位置検出と種類判別を分けて行う two-stage method と、両者を同時に行う one-stage method の2つのアプローチがあります。


初期の物体検出手法では、まず物体らしき領域を推定し、その領域を切り出して分類を行う two-stage method が主流でした。この手法の代表例が Faster R-CNN {cite}`ref_fasterrcnn` です。一方で、計算リソースの制約や処理速度の向上を考慮し、物体の座標推定と分類を一度に最適化する one-stage method が登場しました。代表的な手法には、YOLO（You Only Look Once） {cite}`ref_yolo` や SSD（Single Shot MultiBox Detector） {cite}`ref_ssd` があります。


```{figure} ../_static/object_detection_arches.png
---
name: fig-objdet_archs
width: 90%
---

物体検出および領域抽出のアーキテクチャ。
```




```{bibliography} ../references.bib
:filter: docname in docnames
:style: plain
```


