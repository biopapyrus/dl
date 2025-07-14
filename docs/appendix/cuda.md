# CUDA

GPU（Graphics Processing Unit）は、コンピュータやゲーム機で高速に画像処理を行い、モニターにデータを表示させるための重要なデバイスの一つです。かつては主にゲーム分野で使用されていましたが、現在では計算量の多い深層学習にとって不可欠な存在となっています。GPU は NVIDIA や AMD をはじめ、複数の企業によって開発・製造されていますが、特に NVIDIA 社はこの分野の先駆者であり、高性能な GPU を提供しているため、同社の製品が広く普及しています。

GPU は、モニターやキーボードのように単に接続するだけでは利用できません。GPU を使用するには、まず GPU ドライバーと呼ばれるソフトウェアをインストールし、コンピュータが GPU を認識できるようにする必要があります。ドライバーをインストールすることで、基本的な画像処理機能が利用可能になりますが、GPU を用いて高度な計算を行うには、難解なプログラミング言語を利用してプログラムを記述する必要があります。

これを解決するために、NVIDIA 社は CUDA（Compute Unified Device Architecture）というライブラリを提供しています。CUDA をインストールすることで、開発者は CUDA プログラミング言語を使用して、GPU を活用したプログラムを効率的に記述できるようになります。CUDA は、CUDA プログラミング言語で書かれたコードを NVIDIA 製 GPU が理解できる形式に変換する役割を果たしています。なお、AMD 社の GPU を利用している場合は、AMD 社が提供している ROCm（Radeon Open Compute Platform）をインストールする必要があります。

CUDA プログラミング言語は C 言語をベースに拡張されたものであり、初心者にとって書きやすいとは言えません。この点を補うために、PyTorch や TensorFlow といった Python ライブラリが広く利用されています。これらのライブラリは CUDA と連携し、Python で記述されたコードを GPU が理解できる形式に変換する機能を提供します。この仕組みにより、開発者は複雑な GPU 固有のコードを記述する必要がなくなり、Python を使って効率的に GPU を活用した計算を実行できるようになります。

本ページでは、GPU ドライバーと CUDA のインストール方法を紹介します。ここでは、NVIDIA GeForce RTX 3070 LHR を搭載した Ubuntu 24.04 環境を例に、CUDA のインストール手順を説明します。なお、GPU の型番がわからない場合でもドライバーのインストールは可能ですが、エラーが発生した場合には型番を調べる必要があります。その際は、以下のコマンドを使用して確認してください。


```bash
lspci | grep -i nvidia
# 01:00.0 VGA compatible controller: NVIDIA Corporation GA104 [GeForce RTX 3070 Lite Hash Rate] (rev a1)
# 01:00.1 Audio device: NVIDIA Corporation GA104 High Definition Audio Controller (rev a1)
```


## CUDA のインストール方法（Ubuntu）

### 準備

インストールを開始する前に、まず Ubuntu のデフォルトでインストールされているビデオドライバーを無効にする必要があります。まず、テキストエディタで次のファイルを開きます。ファイルが存在しない場合は新規作成してください。

```bash
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
```

ファイルに以下の 2 行を追加します。

```text
blacklist nouveau
options nouveau modeset=0
```

設定を反映させるため、次のコマンドを実行してシステムを再起動します。

```
sudo update-initramfs -u
sudo reboot
```



### GPU ドライバーのインストール

NVIDIA 社が提供する GPU ドライバーをインストールします。まず、必要なリポジトリおよびセキュリティキーをシステムに追加します。

```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```

次に、利用可能な GPU ドライバーを確認します。表示されたドライバーの中で、**recommended** と表示されているものが推奨されているドライバーです。なお、同じ型番の GPU でも、システムのバージョンにより異なるドライバーが推奨される場合があります。

```bash
ubuntu-drivers devices
# == /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
# modalias : pci:v000010DEd00002488sv00001462sd00003909bc03sc00i00
# vendor   : NVIDIA Corporation
# model    : GA104 [GeForce RTX 3070 Lite Hash Rate]
# driver   : nvidia-driver-555 - third-party non-free
# driver   : nvidia-driver-545-open - third-party non-free
# driver   : nvidia-driver-535-server - distro non-free
# driver   : nvidia-driver-560 - third-party non-free recommended
# driver   : nvidia-driver-550 - third-party non-free
# driver   : nvidia-driver-470-server - distro non-free
# driver   : nvidia-driver-470 - distro non-free
# driver   : nvidia-driver-550-open - third-party non-free
# driver   : nvidia-driver-535-server-open - distro non-free
# driver   : nvidia-driver-555-open - third-party non-free
# driver   : nvidia-driver-535 - distro non-free
# driver   : nvidia-driver-545 - third-party non-free
# driver   : nvidia-driver-560-open - third-party non-free
# driver   : nvidia-driver-535-open - distro non-free
# driver   : xserver-xorg-video-nouveau - distro free builtin
```

**recommended** と表示されたドライバーをインストールします。

```bash
sudo apt install nvidia-driver-560
```

```{warning}
**recommended** と表示された以外のバージョンのドライバをインストールすると、再起動後にモニターを認識できなくなる恐れがあります。
```

インストールが完了したら、システムを再起動します。


```bash
sudo reboot
```

再起動後、`nvidia-smi` のコマンドを実行して、GPU に関する情報が表示されれば、ドライバーが正しくインストールされたことが確認できます。この時点で表示される CUDA バージョンは実際のものと異なる場合があるので、気にしなくて構いません。

```bash
nvidia-smi
# Mon Nov 18 13:41:58 2024
# +-----------------------------------------------------------------------------------------+
# | NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
# |-----------------------------------------+------------------------+----------------------+
# | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
# | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
# |                                         |                        |               MIG M. |
# |=========================================+========================+======================|
# |   0  NVIDIA GeForce RTX 3070        Off |   00000000:01:00.0  On |                  N/A |
# |  0%   36C    P8             11W /  220W |     131MiB /   8192MiB |      0%      Default |
# |                                         |                        |                  N/A |
# +-----------------------------------------+------------------------+----------------------+
# 
# +-----------------------------------------------------------------------------------------+
# | Processes:                                                                              |
# |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
# |        ID   ID                                                               Usage      |
# |=========================================================================================|
# |    0   N/A  N/A      1690      G   /usr/lib/xorg/Xorg                            105MiB |
# |    0   N/A  N/A      1796      G   /usr/bin/gnome-shell                           10MiB |
# +-----------------------------------------------------------------------------------------+
```

なお、`nvidia-smi` コマンドを実行した際に以下のようなエラーが表示され、`sudo modprobe nvidia` コマンドで `Key was rejected by service` というエラーが出る場合、Secure Boot が有効になっている可能性があります。Secure Boot を無効にすると GPU ドライバーが正しく認識されるようになります。Secure Boot を無効にするために、コンピュータの BIOS 設定画面で設定します。コンピュータの製造元により、BIOS 設定画面の起動方法が異なるので、インターネットで検索しながら対処してください。

```bash
nvidia-smi
# NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

sudo modprobe nvidia
# modprobe: ERROR: could not insert 'nvidia': Key was rejected by service
```




### CUDA ライブラリのインストール

GPU が正常に動作することを確認したら、次に CUDA ライブラリをインストールして、GPU を大規模な演算に利用できるようにします。CUDA は NVIDIA の公式サイトからダウンロードできます。インストール方法は、[CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) から適切なバージョンを選んでスクリプトを表示し、それに従ってインストールします。例えば、Ubuntu 24.04 に CUDA 12.6 をインストールするには、次のコマンドを実行します。



```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin
sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.6.1/local_installers/cuda-repo-ubuntu2404-12-6-local_12.6.1-560.35.03-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2404-12-6-local_12.6.1-560.35.03-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2404-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6
```


```{note}
CUDA のバージョンについては、最新バージョンをインストールするのではなく、利用する深層学習ライブラリ（例：PyTorch）でサポートされているバージョンを選ぶことをおすすめします。例えば、PyTorch では[公式サイト](https://pytorch.org/get-started/locally/)で対応する CUDA バージョンを確認できます。2024 年 10 月現在、CUDA 12.4、12.1、11.8 が主にサポートされています。これらのバージョンの CUDA をインストールすると、PyTorch のインストールが簡単になります。なお、PyTorch を自分でビルドする場合、CUDA のバージョンを気にせずインストールできます。
```

CUDA のインストールが完了したら、次に CUDA の機能を使用するために、インストール先をシステムに反映させます。`/etc/profile` ファイルを開き、次の 2 行を追加します。


```bash
export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
```

その後、システムを再起動します。

```bash
sudo reboot
```

再起動後、`nvcc` コマンドを実行して、インストールされた CUDA のバージョンが表示されれば、インストールは成功です。

```bash
nvcc -V
# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2024 NVIDIA Corporation
# Built on Wed_Aug_14_10:10:22_PDT_2024
# Cuda compilation tools, release 12.6, V12.6.68
# Build cuda_12.6.r12.6/compiler.34714021_0
```

### cuDNN ライブライのインストール

PyTorch を利用するのであれば CUDA のインストールだけで十分です。ただし、Tensorflow などでは CUDA とそれに対応した cuDNN ライブラリが必要です。Tensorflow を利用するのに必要な CUDA と cuDNN の対応は、Tensorflow の[インストールガイド](https://www.tensorflow.org/install/source#gpu)で確認できます。例えば、CUDA のバージョンが 12.5 の場合は、cuDNN のバージョンは 9.3 である必要があります。

[cuDNN アーカイブ](https://developer.nvidia.com/cudnn-archive)よりインストールしたいバージョンの cuDNN を選び、　CUDA と同様にシステムのバージョンを選択して、インストールスクリプトを表示させます。例えば、Ubuntu 24.04 に cuDNN 9.3 をインストールする場合には、次のようなコードが表示されます。


```bash
wget https://developer.download.nvidia.com/compute/cudnn/9.3.0/local_installers/cudnn-local-repo-ubuntu2404-9.3.0_1.0-1_amd64.deb
sudo dpkg -i cudnn-local-repo-ubuntu2404-9.3.0_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-ubuntu2404-9.3.0/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn
```

最後にシステムを再起動します。

```bash
sudo reboot
```

以上の作業で CUDA および cuDNN のインストールが終わります。
