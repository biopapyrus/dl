# 利用設定

## インストール

Label Studio は Python で作られたウェブアプリケーションです。Python が使える環境であれば、Label Studio を利用できます。インストールは Python のパッケージ管理ツール `pip` を使って行います。

```bash
pip install label-sutdio
```


なお、Anaconda を利用して作成した Python 環境では、psycopg2 ライブラリがインストールされていない場合があります。その場合は、先に psycopg2 をインストールしてから Label Studio をインストールしてください。

```bash
conda install psycopg2
pip install label-studio
```


## 初期設定

コンピューター上の画像などのデータを効率よく Label Studio に取り込むためには、Label Studio が対象ディレクトリにアクセスできるよう設定する必要があります。環境変数を設定して適切な値を指定することで、特定のディレクトリにあるデータを一括で取り込むことが可能になります。この設定は、Label Studio を起動する前に毎回実行する必要があります。


`````{tab-set}

````{tab-item} Windows (Prompt)
```{code-block} powershell
$env:LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
$env:LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="C:\Users\USERNAME\Desktop\ws"
```
````

````{tab-item} macOS
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/Users/USERNAME/Desktop/ws"
```
````

````{tab-item} Ubuntu
```{code-block} bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT="/home/USERNAME/Desktop/ws"
```
````

`````

```{note}
Windows では、操作環境としてコマンドプロンプト（または Anaconda Prompt）と PowerShell（または Anaconda PowerShell）が利用できます。両者では環境変数の設定方法が異なります。本資料では コマンドプロンプト（または Anaconda Prompt）における実行例を示します。
```

ただし、この設定を行わなくても、ドラッグ＆ドロップによるデータの取り込みは可能です。


## Label Studio 起動

Label Studio は、ターミナルで `label-studio` コマンドを実行するだけで起動できます。初回起動時には、内部で使用するデータベースの初期化や、データ格納用ディレクトリの作成が行われるため、少し時間がかかります。これらのデータベースやデータ格納ディレクトリは、OS によって次の場所に作成されます。

- Windows: `C:\Users\USERNAME\AppData\Roaming\label-studio`
- macOS: `/Users/USERNAME/Library/Application Support/label-studio`
- Ubuntu: `/home/USERNAME/.local/share/label-studio`

しかし、これらのデータ保存場所は、普段利用者が直接アクセスすることが少なく、データの確認やバックアップなどが行いにくいという問題があります。そのため、Label Studio を起動する際には、専用のフォルダを指定することをおすすめします。たとえば、デスクトップに `labelstudio_data` フォルダを作成し、次のように指定します。


`````{tab-set}

````{tab-item} Windows (Prompt)
```{code-block} powershell
label-studio start --data-dir C:\Users\USERNAME\Desktop\labelstudio_data
```
````

````{tab-item} macOS
```{code-block} bash
label-studio start --data-dir ~/Desktop/labelstudio_data
```
````

````{tab-item} Ubuntu
```{code-block} bash
label-studio start --data-dir ~/Desktop/labelstudio_data
```
````

`````



```{note}
macOS および Ubuntu では、デスクトップは `~/Desktop` と指定できます。一方、Windows では利用形態によって異なり、通常は `C:\Users\USERNAME\Desktop` だが、OneDrive を利用している場合は `C:\Users\USERNAME\OneDrive\Desktop` となることもあります。また、日本語環境では `Desktop` が`デスクトップ`になっている場合があります。正しいパスを指定するためには、対象のディレクトリのプロパティを確認して、正確なパスを指定してください。
```

コマンド実行後、表示される URL をブラウザで開くと、Label Studio の登録・ログイン画面が表示されます。初回利用時は「Sign Up」から、メールアドレスとパスワードを入力してユーザー登録を行います。登録情報は、`labelstudio_data` フォルダ内の `label_studio.sqlite3` ファイル（データベース）に暗号化されて保存されます。

このように `--data-dir` を指定しておくと、データベースやアップロードしたファイルを含め、Label Studio の環境がすべてひとつのディレクトリにまとめられます。そのため、USB などで他のコンピューターに丸ごと移動することも可能です。また、データの保存場所が明確になることで、バックアップや環境の移行も簡単に行えます。
