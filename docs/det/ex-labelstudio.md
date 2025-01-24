# 演習：Label Studio

[Label Studio](https://labelstud.io/) は、Python で作られたウェブベースのアプリケーションで、画像やその他のデータにアノテーション（タグ付け）を行うために使用されます。画像分類のためのタグ付けや、特定領域を矩形や多角形で囲む物体検出のタグ付けに適しています。ソースコードは Apache License 2.0 のもとで公開されており、商用利用や改変・再配布が可能です。また、Label Studio で作成されたデータの著作権は作成者に帰属し、自由に利用できます。


## インストール

Label Studio は PyPI から配布されており、Python パッケージとして `pip` コマンドでインストールできます。

```bash
pip install label-sutdio
```

## Label Studio 起動

起動前に、Label Studio がデータにアクセスできるように環境変数を設定します。例えば、データがデスクトップの ws/images フォルダ内にある場合、次のコマンドを実行してください。Label Studio を起動する前に、毎回これを実行する必要があります。


```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users/USERNAME/Desktop/ws"
```

次に、以下のコマンドで Label Studio を起動します。初回起動時には、`-db` で指定された場所にデータベースが自動的に作成されます。

```bash
label-studio -db ~/Desktop/ws/label_studio.sqlite3
```

実行後、表示される URL をブラウザで開くと、Label Studio の登録・ログイン画面が表示されます。



## 初期設定

登録・ログイン画面で新規登録（SIGN UP）を行い、メールアドレスとパスワードを入力します。これらの情報は暗号化され、`-db` で指定されたデータベースに保存されます。


## プロジェクト作成

Label Studio をログインしたのちに、Project を作成します。Project 作成画面では「Project Name」、「Data Import」、および「Labeling Setup」の 3 つのタブが表示されます。


- 「Project Name」タブにおいて、Project Name を kvasir とし、そのほかの設定は変更しません。
- 「Data Import」タブについてはデフォルトのままで変更しません。
- 「Labeling Setup」タブにおいて、「Object Detection with Bounding Boxes」を選び、ラベル設定画面において、すでに登録された「Airplane」および「Cars」を「X」で削除し、Add label names 欄に「polyp」を入力し、「Add」ボタンをクリックして登録します。


編集後の画面は {numref}`fig-labelstudio_project_labelsettings` のようになります。


```{figure} ../_static/labelstudio_project_labelsettings.png
---
name: fig-labelstudio_project_labelsettings
---
Label Studio 新規プロジェクトにおける Labeling Setup の設定画面。
```

最後に「Save」ボタンをクリックします。物体検出用のデータをアノテーションするプロジェクトはこれで作成できました。


## 画像データ

サンプルデータを利用する場合は、[kvasirdet.zip](https://medDL.biopapyrus.jp/data/kvasirdet.zip) を使ってください。このデータセットは内視鏡画像を集めた医療用データセットで、[Simula Research Laboratory](https://datasets.simula.no/) にて公開されています。Kvasir データセットは研究および教育目的に限り利用可能で、それ以外の用途での使用は許可されていません。データセットを扱う際は、利用規約を必ず遵守してください。


## データ登録

Label Studio でアノテーションを付けたい画像をすべて、デスクトップ上の `ws` フォルダの `images` フォルダの中に入れます。次に、プロジェクトページの右上にある「Settings」ボタンをクリックし、設定画面を表示させます。設定画面の左側にあるメニューから「Cloud Storage」をクリックします。

続けて、Cloud Storage 登録画面にて「Add Source Storage」ボタンをクリックして、次のように各項目を設定します。

- Storage Type: Local files
- Storage Title: storage1
- Absolute local Path: `C:\Users/USERNAME/Desktop/ws/images`
- File Filter Regex: `.*(jpe?g|png|tiff)`
- Treat every bucket object as a source file: **ON**


```{figure} ../_static/labelstudio_project_addstorage.png
---
name: labelstudio_project_addstorage
---
Label Studio に画像を登録するときの設定
```

設定後「Check Connection」ボタンをクリックして Label Studio が正しくデータを認識できるかを確認します。「Successfully connected!」と表示されましたら正しく設定されたことになります。続けて「Add Storage」ボタンをクリックしてデータを登録します。

データを登録後に、登録画面には次のようなデータセット一覧が表示されます。「Sync Storage」をクリックすると、Label Studio が設定に基づいて画像を取り組みます。しばらくすると、指定されたストレージにある画像がすべて登録されます。


```{figure} ../_static/labelstudio_syncdata.png
---
name: labelstudio_syncdata
---
登録したデータストレージにある画像を同期
```

## アノテーション作業

データを登録したのちに Label Studio のプロジェクトページに戻ると、登録した画像の一覧が表示されます。


```{figure} ../_static/labelstudio_project_mainpage.png
---
name: labelstudio_project_mainpage
---
プロジェクトページに表示される登録済みデータセット
```

任意の画像をクリックすると、その画像のラベリングページに遷移します。ラベリングページにて、下側に表示されるラベル「polyp」をクリックしてから、画像中にあるポリープの左上付近をクリックし、そのままドラッグしてポリープの右下までに移動させてからマウスを離します。これで、ポリープを囲む矩形が描かれます。この矩形のことをバウンディングボックスと呼びます。なお、一度作成したバウンディングボックスをあとから修正したり、削除したりすることが可能です。


```{figure} ../_static/labelstudio_project_labeling.png
---
name: labelstudio_project_labeling
---
画像にアノテーションをつけるページ
```

すべてのポリープを囲めたら、最後に「Submit」ボタンをクリックします。これで 1 枚の画像についてアノテーション作業が完了になります。この作業をすべての画像に対して繰り返します。


## データエクスポート

アノテーション作業が完了したら、アノテーション情報をエクスポートします。プロジェクトページに戻り、右上の「Export」ボタンをクリックします。次に、ポップアップウィンドウに表示されたフォーマットの中から「COCO」を選び、「Export」ボタンをクリックします。画像とアノテーションと共にダウンロードが開始されます。



```{figure} ../_static/labelstudio_export.png
---
name: labelstudio_export
---
アノテーションデータをファイルに保存
```

