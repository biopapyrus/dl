# ラベリング

Label Studio でラベリング作業を行うには、まずプロジェクトを新規作成し、データを登録する必要があります。本節では、画像データを登録してラベリングを行うまでの手順を示します。


## プロジェクト作成

`--data-dir` オプションを付けて Label Studio を起動し、ログインします。起動時に、デスクトップ上の ws ディレクトリを Label Studio から認識させるため、環境変数を設定します。

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


起動後、「Create Project」ボタンをクリックして新規プロジェクトを作成します。画面には「Project Name」「Data Import」「Labeling Setup」の3つのタブが表示されます。


- **Project Name**: プロジェクト名を spikeDet とし、その他の設定は変更しません。
- **Data Import**: デフォルト設定のまま使用します。
- **Labeling Setup**: 「Object Detection with Bounding Boxes」を選択します。既存の「Airplane」や「Cars」を削除し、Add label names 欄に spike と入力して「Add」をクリックします。その他の設定は変更しません。編集後の画面例は {numref}`fig-labelstudio_project_labelsettings` のようになります。


```{figure} ../_static/labelstudio_project_labelsettings.png
---
name: fig-labelstudio_project_labelsettings
---
Label Studio プロジェクト新規作成時の設定例。
```

最後に「Save」をクリックします。


## データ登録

次に、spikeDet プロジェクトに登録するデータを、Label Studio が認識している ws ディレクトリの下に入れます。[gwhd.zip](https://dl.biopapyrus.jp/data/gwhd.zip) をダウンロードし、zip を展開してください。展開後、gwhd 中にある images ディレクトリをデスクトップ上の ws ディレクトリに配置します。

続いて、images ディレクトリにある画像を Label Studio に登録します。画像の登録方法には、「ローカルファイルとして登録する方法」と「プロジェクトの Import 機能を利用する方法」の二種類があります。前者は、指定したディレクトリ内の画像を一括で取り込むことができるため、画像の枚数が多い場合に便利です。一方、後者は、ブラウザ上で指定された場所に画像をドラッグ＆ドロップするだけで登録できます。ただし、一度に取り込める画像の枚数には上限があります。

### ローカルファイルとして登録

Label Studio で spikeDet プロジェクトページの右上にある「Settings」をクリックし、設定画面を開きます。左側のメニューから「Cloud Storage」を選択し、「Add Source Storage」をクリックします。設定例は次の通りです（{numref}`fig-labelstudio_project_addstorage`）。

- **Storage Type**: Local files
- **Storage Title**: storage1
- **Absolute local path**: `/Users/jsun/Desktop/ws/images`
- **File Filter Regex**: `.*(jpe?g|png|tiff)`
- **Treat every bucket object as a source file**: ON


```{figure} ../_static/labelstudio_project_addstorage.png
---
name: fig-labelstudio_project_addstorage
width: 80%
---
ローカルコンピューターにあるデータを Label Studio プロジェクトに登録するときの設定例。
```

設定後、「Check Connection」をクリックして接続確認します。「Successfully connected!」と表示されれば正しく設定されています。「Add Storage」をクリックしてデータを登録します。

登録後、データセット一覧が表示されます。「Sync Storage」をクリックすると、Label Studio が指定されたストレージ内の画像を取り込みます。取り込みが完了すると、画像枚数（Tasks）と同期時間（Last Sync）が表示されます（{numref}`fig-labelstudio_syncdata`）。


```{figure} ../_static/labelstudio_syncdata.png
---
name: fig-labelstudio_syncdata
width: 80%
---
データ同期前後の画面例。同期後はタスク数と同期時間が表示される。
```


### Import 機能を利用して登録

プロジェクトページを開き、右上の「Import」をクリックします。アップロード画面が表示されたら、登録したい画像をドラッグ＆ドロップし、最後に「Import」ボタンをクリックすると画像が登録されます。

```{figure} ../_static/labelstudio_project_dataimport.png
---
name: fig-labelstudio_project_dataimport
---
プロジェクトに画像を Import する例。
```

なお、この方法で登録された画像は、Label Studio の作業フォルダに保存されます。具体的には、`--data-dir` で指定したディレクトリの下にある media/upload ディレクトリ内に保存されます。


## ラベリング作業

データ登録後、プロジェクトページには登録済みの画像一覧が表示されます。

```{figure} ../_static/labelstudio_project_mainpage.png
---
name: labelstudio_project_mainpage
---
プロジェクトページに表示される登録済みデータセット
```

任意の画像をクリックするとアノテーションページに移動します。下部のラベル「spike」を選択し、画像中の小麦の穂の左上をクリックしてドラッグし、右下まで囲むことで矩形（バウンディングボックス）を描きます。一度作成した矩形は、後から修正や削除が可能です。


```{figure} ../_static/labelstudio_project_labeling.png
---
name: labelstudio_project_labeling
---
画像にアノテーションをつけるページ
```

すべての穂を囲んだら「Submit」をクリックします。これで1枚の画像のアノテーションが完了です。この作業をすべての画像に繰り返します。
