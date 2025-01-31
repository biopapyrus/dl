# conda

conda (Anaconda, Miniconda) は科学計算用の仮想環境を構築するためのソフトウェアです。Python を実行するための仮想環境を構築する際に利用されることが多いですが、実際には Python 以外のさまざまなソフトウェアやライブラリなどもインストールおよび管理を行うことができ、科学解析用の統合仮想環境を構築するためにソフトウェアです。conda を利用すると、科学解析用の様々なソフトウェアが自動的にインストールされるため、少ない操作ですぐに解析や機械学習などを開始することができ、比較的に初心者に勧められソフトウェアの一つです。

近年は Anaconda は、規模の大きい学術機関を含めてすべて有償になるとライセンスが変更されました。そのための回避策として Miniconda をインストールし、conda コマンドでソフトウェアやライブラリをインストールするときに default チャンネルを利用せずに conda-forge を指定するなどが挙げられます。そのため、conda を利用して機械学習を始めたい初心者は Miniconda をインストールし、conda コマンドで conda-forge を利用できるように設定を済ませる必要があります。なお、Python の実行環境を利用するだけが目的であれば、conda ではなく、pyenv などを利用されることがおすすめです。pyenv なら conda と同様に、複数の異なるのバージョンの Python を管理できます。



## miniconda のインストール方法（Ubuntu/macOS）

Ubuntu および macOS に miniconda をインストールには、基本的にターミナルで操作すると簡単です。[anaconda.com](https://anaconda.com) の [Quick command line install](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) を参考にして、次のコマンドを 1 行ずつ実行します。

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh
```

インストールが始まると、使用規約や初期設定事項など表示されます。次のように「Welcome to Anaconda3 ...」に続いて、ライセンス確認のコメントが表示されます。最後に `>>>` が表示されます。そのまま「Enter」キーを押します。

```bash
# Welcome to Anaconda3 20xx.xx
# 
# In order to continue the installation process, please review the license
# agreement.
# Please, press ENTER to continue
# >>>
```

次に、ライセンスが表示され、「スペース」キーを押して、ライセンスの一番下まで移動します。最後に `>>>` が表示されましたら、`yes` を入力して、「Enter」キーを押します。


```bash
# Anaconda End User License Agreement
# ...
# ...
# Do you accept the license terms? [yes|no]
[no] >>>
```

ライセンスへの同意後に、conda のインストール先を聞かれます。特別な理由がなければ変更せずに、`>>>` に続けて「Enter」キーを押します。

```bash
# Anaconda3 will now be installed into this location:
# /home/USERNAME/anaconda3
#
#   - Press ENTER to confirm the location
#   - Press CTRL-C to abort the installation
#   - Or specify a different location below
#
# [/home/USERNAME/anaconda3] >>>
```

インストール先が指定されると、インストールが行われます。しばらくして、インストールが終わると、conda を常時利用できるような状態にしますかと聞かれるので、`yes` を入力して「Enter」キーを押します。なお、ここで `no` を入力すると、conda を利用するときに毎回手動で起動させる必要があります。

```bash
# ...
# ...
# Preparing transaction: done
# Executing transaction: done
# installation finished.
# Do you wish the installer to initialize Anaconda3
# by running conda init? [yes|no]
# [no] >>>
```

インストールが完了すると、次のようなメッセージが表示されます。

```bash
# ...
# ...
```

ここまでの作業でインストールが終わりました。このままでも conda を利用できますが、この状態では conda の base 環境が常に自動的にアクティベートされます。そのため、少しの不注意で、base 環境にさまざまなライブラリをインストールしてしまい、conda 全体の環境が影響を及ぼしてしまいます。そこで、デフォルトで base 環境がアクティベートされないように、次のコマンドを実行します。

```bash
conda config --set auto_activate_base false
```

最後にインストールスクリプトを削除してインストールを終えます。

```bash
rm ~/miniconda3/miniconda.sh
```

ターミナルを再起動すると conda が利用できるようになります。

なお、必要に応じて、conda を使ってソフトウェアをインストールするときに、有償利用となる default チャンネルからインストールされないように、次の設定を行います。

```bash
conda config --remove channels defaults  
```

次のコマンドを実行した時に、「channles」の一覧に default がなく、conda-forge が表示されていれば、正しく設定が行われたことになります。

```bash
conda config --show channels
#  channels:
#  - conda-forge
```




## miniconda のインストール方法（Windows）

Windows では、コマンドプロンプトでインストールすることも、グラフィックインストーラーを利用してインストールすることもできます。コマンドプロンプトでインストールする場合は、 [anaconda.com](https://anaconda.com) の [Quick command line install](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) を参考にしてインストールを行います。グラフィックインストーラーを利用する場合は、[anaconda.com](https://anaconda.com) の[ダウンロードページ](https://www.anaconda.com/download/success) にて Miniconda Installer をダウンロードして利用します。ここでは、グラフィックインストーラーを利用する方法を説明します。


ダウンロードしたインストーラーをダブルクリックして起動させます。

```{image} ../_static/conda-windows-01.png
:alt: Miniconda Windows インストーラーアイコン
:width: 180px
:align: center
```

インストーラーが起動されたら「Next」をクリックし、続けます。

```{image} ../_static/conda-windows-02.png
:alt: Miniconda Windows インストーラー起動画面
:width: 80%
:align: center
```

次のように利用規約が表示されますので、確認してから「I Agree」をクリックします。

```{image} ../_static/conda-windows-03.png
:alt: Miniconda Windows ライセンス確認
:width: 80%
:align: center
```

Miniconda の利用ユーザーを指定します。基本、個人で利用するなら「Just Me」を選択し、「Next」をクリックします。

```{image} ../_static/conda-windows-04.png
:alt: Miniconda Windows 適用ユーザー
:width: 80%
:align: center
```

次に、インストール先のフォルダを設定します。基本、デフォルトのままにします。ただし、ユーザー名に全角文字や空白などが含まれている場合に、エラーなどが生じることがあります。この場合、デフォルトのインストール先を利用せずに、「C:\anaconda3」を指定します。


```{image} ../_static/conda-windows-05.png
:alt: Miniconda Windows インストール先
:width: 80%
:align: center
```


続けて、環境変数の設定を行います。「Create shortcuts」および「Register Miniconda3 as my default Python 3.12」にチェックを入れます。「Install」ボタンをクリックし、インストールを開始します。


```{image} ../_static/conda-windows-06.png
:alt: Miniconda Windows 環境変数 PATH 設定
:width: 80%
:align: center
```


インストールが開始され、しばらくすると次のようにインストールの完了を知らせる画面が表示されます。「Next」をクリックします。

```{image} ../_static/conda-windows-08.png
:alt: Miniconda Windows インストール完了
:width: 80%
:align: center
```

インストール終了後に、「Getting started with Conda」および「Welcome to Anaconda」の選択肢が表示されますが、すべてのチェックを外して「Finish」ボタンをクリックします。


```{image} ../_static/conda-windows-09.png
:alt: Miniconda Windows インストール完了
:width: 80%
:align: center
```


以上で、インストール作業が完了です。これ以降、Miniconda を利用して開発環境を構築したり、データ解析を行ったりする場合は、Windows のスタートメニューから「Anaconda Prompt」を選び、起動させて利用します。

```{image} ../_static/conda-windows-10.png
:alt: Miniconda 起動
:width: 80%
:align: center
```

最後に、必要に応じて、conda を使ってソフトウェアをインストールするときに、有償利用となる default チャンネルからインストールされないように、Anaconda Prompt を起動して次の設定を行います。

```bash
conda config --remove channels defaults  
```

次のコマンドを実行した時に、「channles」の一覧に default がなく、conda-forge が表示されていれば、正しく設定が行われたことになります。

```bash
conda config --show channels
#  channels:
#  - conda-forge
```
