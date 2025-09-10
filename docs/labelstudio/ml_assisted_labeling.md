# ML-assisted labeling

Label Studio では、学習済みの機械学習モデルを組み込み、ラベリング作業を補助することができます。モデルを組み込むと、Label Studio で新しい画像を開いた際に予測結果が表示され、人はその予測を修正した上でアノテーションを登録します。モデルの精度が高ければ作業効率が向上しますが、精度が低い場合は修正作業が増え、かえって負担になることがあります。そのため、必要に応じて利用するのが便利です。

ここでは、[小麦穂検出](wheat_heading_detection)の演習で作成したモデルを使い、ML-assisted labeling を実施する手順を紹介します。

## 準備作業

### ライブラリーのインストール

Label Studio から機械学習モデルを利用できるように、必要なライブラリーをインストールします。

```bash
pip install gunicorn
pip install redis
pip install label-studio-ml
pip install label-studio-sdk
```

### 機械学習モデルの準備

[小麦穂検出](wheat_heading_detection)の演習で作成したモデルの重みファイル gwhd.pth をダウンロードし、デスクトップ上の ws ディレクトリに保存します。また、このモデルを Label Studio で利用するためのスクリプトも同じ場所に保存してください。

```bash
wget https://raw.githubusercontent.com/biopapyrus/dl/refs/heads/main/scripts/mlassistedlabel.py
```


## モデル登録

まず、ターミナルを開き、Label Studio を起動します。

`````{tab-set}

````{tab-item} Windows (Prompt)
```{code-block} powershell
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users\USERNAME\Desktop\ws"
label-studio start --data-dir C:\Users\USERNAME\Desktop\labelstudio_data
```
````

````{tab-item} macOS
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/Users/USERNAME/Desktop/ws"
label-studio start --data-dir ~/Desktop/labelstudio_data
```
````

````{tab-item} Ubuntu
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/home/USERNAME/Desktop/ws"
label-studio start --data-dir ~/Desktop/labelstudio_data
```
````

`````


次に、別のターミナルを開き、機械学習モデルを動作させます。このターミナルでは、mlassistedlabel.py ファイルのあるディレクトリに移動して実行してください。本資料の手順通りに作業していれば、このファイルはデスクトップ上の ws ディレクトリに保存されています。`cd` コマンドを使ってディレクトリを移動してから、mlassistedlabel.py を実行します。


`````{tab-set}

````{tab-item} Windows (Prompt)
```{code-block} powershell
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users\USERNAME\Desktop\ws"

cd C:\Users\USERNAME\Desktop\ws

python mlassistedlabel.py --host 127.0.0.1 --port 8010 --weight gwhd.pth --data-dir C:\Users\jsun\Desktop\labelstudio_data
##  * Serving Flask app "label_studio_ml.api" (lazy loading)
##  * Environment: production
##    WARNING: This is a development server. Do not use it in a production deployment.
##    Use a production WSGI server instead.
##  * Debug mode: off
##  * Running on http://127.0.0.1:8010/ (Press CTRL+C to quit)
```
````

````{tab-item} macOS
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/Users/USERNAME/Desktop/ws"

cd ~/Desktop/ws

python mlassistedlabel.py --host 127.0.0.1 --port 8010 --weight gwhd.pth data-dir ~/Desktop/labelstudio_data
##  * Serving Flask app "label_studio_ml.api" (lazy loading)
##  * Environment: production
##    WARNING: This is a development server. Do not use it in a production deployment.
##    Use a production WSGI server instead.
##  * Debug mode: off
##  * Running on http://127.0.0.1:8010/ (Press CTRL+C to quit)
```
````

````{tab-item} Ubuntu
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/home/USERNAME/Desktop/ws"

cd ~/Desktop/ws

python mlassistedlabel.py --host 127.0.0.1 --port 8010 --weight gwhd.pth data-dir ~/Desktop/labelstudio_data
##  * Serving Flask app "label_studio_ml.api" (lazy loading)
##  * Environment: production
##    WARNING: This is a development server. Do not use it in a production deployment.
##    Use a production WSGI server instead.
##  * Debug mode: off
##  * Running on http://127.0.0.1:8010/ (Press CTRL+C to quit)
```
````

`````



`Running on http://127.0.0.1:8010/` と表示されれば、モデルは正常に動作しています。



ターミナルでの準備が完了したら、ブラウザで Label Studio にアクセスし、プロジェクト設定ページを開きます。「Model」メニューをクリックし、「Connect Model」を選択してください。表示されるフォームには、以下の内容を入力します（{numref}fig-labelstudio_model_setup）。


ターミナルでの作業はこれで完了です。次に、ウェブブラウザから Label Studio にアクセスし、プロジェクト設定ページを開きます。「Model」メニューをクリックし、「Connect Model」を選択してください。表示されたフォームには、以下のように入力します（{numref}`fig-labelstudio_model_setup`）。


- **Name**: MODEL-1（任意の名前）
- **Backend URL**: http://127.0.0.1:8010/ （`mlassistedlabel.py` 実行時に表示された URL）
- **Select authentication method**: No Authentication
- **Any extra params to pass during model connection**: （空白）
- **Interactive preannotations**: ON


```{figure} ../_static/labelstudio_model_setup.png
---
name: fig-labelstudio_model_setup
width: 70%
---
Label Studio に機械学習モデルを登録する例。
```


入力が完了したら、右下の「Validate and Save」をクリックします。接続が正常に行われれば、Model ページに追加されたモデルが「Connected」と表示されます（{numref}`fig-labelstudio_model_status`）。ランタイムエラー（RUNTIME ERROR）が表示される場合は、1 分ほど待ってから再度「Validate and Save」をクリックしてください。複数回試してもエラーが続く場合は、URL の設定やモデルが正しく動作しているかを確認してください。


```{figure} ../_static/labelstudio_model_status.png
---
name: fig-labelstudio_model_status
width: 70%
---
Label Studio に登録したモデルの状態。
```

なお、Model ページには「Start model training on annotation submission」オプションがあります。これを ON にすると、Label Studio でアノテーションが追加された際に、そのデータを用いてモデルの学習を自動的に行うことができます。ただし、この仕組みはやや複雑であり、本演習では扱いません。


## 自動アノテーションの削除

また、モデルによるアノテーションデータをすべて削除する場合は、以下のコマンドをターミナルで実行します。

```bash
curl -H 'Authorization: Token 80115b1c4f4c8c9594c86f65f4566a9920ea1287' -X POST "http://127.0.0.1:8010/api/dm/actions?id=delete_tasks_predictions&project=1"
```

ここで、Token に続く英数字の列は、Label Studio の個人設定ページで取得できます。また、`http://127.0.0.1:8010` の部分は、モデルを実行した際に表示された URL に置き換えてください。`project=1` の数字は、該当するプロジェクトの ID に変更します。プロジェクト ID は、プロジェクトページの URL から確認できます。例えば、プロジェクトの URL が `http://127.0.0.1:8080/projects/1/` の場合、プロジェクト ID は `1` です。

