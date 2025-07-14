# MMDetection

MMDetection は、深層学習を用いた物体検出やセグメンテーションのモデルを簡単に構築・運用できるライブラリです。物体検出やセグメンテーションのモデルは、画像分類と異なり、画像内の「どこに」「何が」あるのかという物体の位置と種類を同時に学習・推論する必要があり、そのアーキテクチャは非常に複雑です。このようなモデルを PyTorch でゼロから構築することは可能ですが、膨大な労力がかかります。

MMDetection は、このような複雑なモデルを簡単に構築できるようにするための Python ライブラリです。MMDetection を利用することで、「config」と呼ばれる設定ファイルを記述するだけで、さまざまなアーキテクチャを手軽に構築できます。また、MMDetection で生成したモデルは、統一された枠組みの中で同じコードを用いて訓練や推論に活用することが可能です。これにより、物体検出やセグメンテーションモデルの開発プロセスが大幅に効率化されます。

本ページでは、MMDetection をインストールする方法を紹介します。MMDetection は Python のパッケージで、本来ならば他の Python パッケージと同じく `pip` コマンドでインストールできますが、`pip` でインストールした MMDetection は利用時にエラーなどが出てきます。そのため、初心者の場合、Miniconda をインストールした上、Miniconda で仮想環境を構築し、その仮想環境の中で、MMDetection をソースコードからインストールすることをお勧めします。


まず、Miniconda を利用して仮想環境を構築します。

```bash
conda create -n mmdet python=3.11 -y
conda activate mmdet
```

次に、PyTorch をインストールします。MMDetection は、ユーザーから与えられた「config」を元に、PyTorch を利用してモデルを構築しています。そのため、MMDetection をインストールする前に、PyTorch をインストールする必要があります。PyTorch は [PyTorch Get Started](https://pytorch.org/get-started/locally/) を参考にして、システムのバージョンに適した PyTorch をインストールします。


```bash
conda install pytorch torchvision torchaudio -c pytorch -c nvidia
```

続けて、MMDetection 用の config の初期テンプレートや学習済みの重みなどをダウンロードしたりするのに便利なライブラリをインストールします。


```bash
pip install -U openmim
mim install mmengine
```

MMDetection の一部では、MMCV ライブラリーの機能を利用しています。MMCV をインストールします。MMCV のバージョンと MMDetection のバージョンが合わないと「ModuleNotFoundError: No module named 'mmcv._ext'」のようなエラーが発生して、MMDetection が利用できません。また、公式ウェブサイトでは、`mim` コマンドを利用して MMCV をインストールする例が示されているが、その例に従うと、'mmcv._ext' に関連した ModuleNotFoundError が発生します。そのため、ソースコードからインストールすることをお勧めします。

ここでは MMCV 2.1.0 をソースコードからインストールする例を示します。

```bash
git clone https://github.com/open-mmlab/mmcv.git -b v2.1.0 mmcv-v2.1.0
cd mmcv-v2.1.0
pip install --no-cache-dir -r ./requirements/build.txt
pip install --no-cache-dir .[all] -v
```

最後に、MMDetection をインストールします。MMDetection も公式ウェブサイトが推奨している `mim` コマンドを利用するのではなく、ソースコードからインストールすることをお勧めします。ここで、MMCV 2.1.0 に対応している MMDetection 3.3.0 をインストールします。


```bash
git clone https://github.com/open-mmlab/mmdetection.git -b v3.3.0 mmdet-v3.3.0
cd mmdet-v3.3.0
pip install --no-cache-dir -r ./requirements/build.txt
pip install --no-cache-dir . -v
```

