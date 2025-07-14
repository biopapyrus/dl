# 演習：Label Studio

[Label Studio](https://labelstud.io/) は、Python で作られたウェブベースのアプリケーションで、画像やその他のデータにアノテーション（タグ付け）を行うために使用されます。画像分類のためのタグ付けや、特定領域を矩形や多角形で囲む物体検出のタグ付けに適しています。ソースコードは Apache License 2.0 のもとで公開されており、商用利用や改変・再配布が可能です。


## インストール

Label Studio は PyPI から配布されており、Python パッケージとして `pip` コマンドでインストールできます。

```bash
pip install label-sutdio
```

## Label Studio 起動

起動前に、Label Studio がデータにアクセスできるように環境変数を設定します。例えば、データがデスクトップ（Desktop）の ws/images フォルダ内にある場合、次のコマンドを実行してください。この際、`USERNAME` を各自のユーザー名（ログイン名）に置き換えてください。また、Label Studio を起動する前に、毎回これを実行する必要があります。


```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users/USERNAME/Desktop/ws"
```

次に、以下のコマンドで Label Studio を起動します。初回起動時には、`-db` で指定された場所にデータベースが自動的に作成されます。2 回目以降も、同様なコマンドを利用して起動します。

```bash
label-studio -db ~/Desktop/ws/label_studio.sqlite3
```

実行後、表示される URL をブラウザで開くと、Label Studio の登録・ログイン画面が表示されます。



## 初期設定

登録・ログイン画面で新規登録（SIGN UP）を行い、メールアドレスとパスワードを入力します。これらの情報は暗号化され、`-db` で指定されたデータベースに保存されます。このデータベースを他のコンピュータにコピーすることで、そのコンピュータで同様な Label Studio 環境を再現できます。つまり、同じユーザー情報でログインでき、また同じようなプロジェクトが表示されます。


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

サンプルデータを利用する場合は、[kvasirdet.zip](https://dl.biopapyrus.jp/data/kvasirdet.zip)[^kvasir_dataset] を使ってください。このデータセットは内視鏡画像を集めた医療用データセットで、[Simula Research Laboratory](https://datasets.simula.no/) にて公開されています。Kvasir データセットは研究および教育目的に限り利用可能で、それ以外の用途での使用は許可されていません[^kvasir_termsofuse]。データセットを扱う際は、利用規約を必ず遵守してください。



[^kvasir_dataset]: Pogorelov et al. (2017) KVASIR: A Multi-Class Image Dataset for Computer Aided Gastrointestinal Disease Detection. *Proceedings of the 8th ACM on Multimedia Systems Conference*, [10.1145/3083187.3083212](https://doi.org/10.1145/3083187.3083212)

[^kvasir_termsofuse]: "The use of the Kvasir dataset is restricted for research and educational purposes only." [simula Kvasir](https://datasets.simula.no/kvasir/)


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

任意の画像をクリックすると、その画像のアノテーションページに遷移します。アノテーションページにて、下側に表示されるラベル「polyp」をクリックしてから、画像中にあるポリープの左上付近をクリックし、そのままドラッグしてポリープの右下までに移動させてからマウスを離します。これで、ポリープを囲む矩形が描かれます。この矩形のことをバウンディングボックスと呼びます。なお、一度作成したバウンディングボックスをあとから修正したり、削除したりすることが可能です。


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


なお、この方法でエクスポートされたデータには、アノテーションデータに加えて画像も含まれます。画像の枚数が多くなるとシステムに負荷がかかるため、実際の運用ではウェブブラウザを利用してエクスポートするのではなく、Label Studio API を使用してアノテーションデータのみを抽出することが一般的です。



## ML-assisted labeling


学習済みモデルを Label Studio に組み込むことで、アノテーション作業を効率化できます。ここでは、[内視鏡画像ポリープ検出](ex-polyp_detection)の演習で得られたモデルを活用し、ML-assisted labeling を実施する手順を紹介します。


まず、準備作業として、[内視鏡画像ポリープ検出](ex-polyp_detection)の演習で作成したモデルの重みファイル（`kvasirdet.pth`）をダウンロードし、Label Studio の作業フォルダ（Desktop/ws）に配置します。次に、ML-assisted labeling などの開発機能を利用するために、Label Studio のプラグインをインストールします。


```bash
pip install gunicorn
pip install label-studio-ml
pip install label_studio_ml
pip install label-studio-sdk
pip install redis
```

ライブラリのインストールが完了したら、ターミナルを 2 つ開きます。1 つは Label Studio の本体を起動するため、もう 1 つは検出モデルを実行するために使用します。

まず、Label Studio を起動します。この際、必要な環境変数を設定してください。

```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users/USERNAME/Desktop/ws"
label-studio -db ~/Desktop/ws/label_studio.sqlite3
```

次に、もう 1 つのターミナルで、PyTorch で作成した検出モデルを Label Studio に組み込むためのプログラムを作業フォルダ（`Desktop/ws`）にダウンロードします。

```bash
wget https://raw.githubusercontent.com/biopapyrus/dl/refs/heads/main/scripts/mlassistedlabel.py
```

ダウンロードしたプログラムを Python で実行します。この際、`--weight` オプションで検出モデルの重みファイルのパスを指定してください。また、ホスト名やポート番号は省略可能ですが、実行のたびに変更される可能性があるため、固定しておくことを推奨します。

```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users/USERNAME/Desktop/ws"

python mlassistedlabel.py --host 127.0.0.1 --port 8010 --weight kvasirdet.pth
##  * Serving Flask app "label_studio_ml.api" (lazy loading)
##  * Environment: production
##    WARNING: This is a development server. Do not use it in a production deployment.
##    Use a production WSGI server instead.
##  * Debug mode: off
##  * Running on http://127.0.0.1:8010/ (Press CTRL+C to quit)
```

上記のように `Running on http://...` と表示されれば、正常に動作しています。


ターミナルでの作業はこれで完了しました。次に、ウェブブラウザから Label Studio にアクセスし、プロジェクト設定ページを開きます。「Model」メニューをクリックし、「Connect Model」を選択してください。表示されたフォームには、以下のように入力します。


- Name: kvasirdet（任意の名前で構いません。）
- Backend URL: http://127.0.0.1:8010/ （`mlassistedlabel.py` 実行時に表示された URL を入力します。）
- Select authentication method: No Authentication
- Any extra params to pass during model connection: （空白にします。）
- Interactive preannotations: ON


設定が完了したら、画面右下の「Validate and Save」ボタンをクリックします。問題なく接続できれば、Model ページに追加されたモデルが「Connected」として表示されます（{numref}`fig-labelstudio_model_status`）。


```{figure} ../_static/labelstudio_model_status.png
---
name: fig-labelstudio_model_status
width: 70%
---
Label Studio に登録したモデルの状態。
```


なお、Model ページには「Start model training on annotation submission」オプションがあります。これを ON にすると、Label Studio でアノテーションが追加された際に、そのデータを利用してモデルの学習が自動的に行われるようになります。ただし、この学習の仕組みはやや複雑で、本演習では扱いません。

また、モデルによるアノテーションデータをすべて削除する場合は、以下のコマンドをターミナルで実行します。

```bash
curl -H 'Authorization: Token 80115b1c4f4c8c9594c86f65f4566a9920ea1287' -X POST "http://127.0.0.1:8010/api/dm/actions?id=delete_tasks_predictions&project=1"
```

ここで、Token に続く英数字の列は、Label Studio の個人設定ページで取得できます。また、`http://127.0.0.1:8010` の部分は、モデルを実行した際に表示された URL に置き換えてください。`project=1` の数字は、該当するプロジェクトの ID に変更します。プロジェクト ID は、プロジェクトページの URL から確認できます。例えば、プロジェクトの URL が `http://127.0.0.1:8080/projects/1/` の場合、プロジェクト ID は `1` です。

