# Docker

Docker は、アプリケーションを動作させる環境を簡単に構築、共有、運用できるプラットフォームです。Docker が一般的に使われる以前は、仮想マシンを利用するか、あるいはアプリケーションの動作に必要なライブラリや設定を手順書にまとめ、利用者がその手順に従って環境を構築する必要がありました。この作業は、開発者が機能テストを行ったり、利用者がアプリケーションを使ったりする度に繰り返す必要がありました。

これに対して、Docker を使うことで、開発者はアプリケーションとその動作環境を「コンテナ」と呼ばれる単位にまとめることができます。利用者はそのコンテナを展開するだけで、追加の設定を行うことなくアプリケーションを動作させることが可能です。これにより、開発から本番環境への移行がスムーズになり、利用者が行う煩雑な環境構築の手間を省けるだけでなく、環境の違いによるトラブルも大幅に減少します。また、Docker コンテナは仮想マシンに比べて軽量で、1 台のシステム上で複数のコンテナを効率よく実行できます。この特徴を活かして、開発者は大規模なアプリケーションを複数のコンポーネントに分割し、それぞれを個別のコンテナとして開発・運用することができます。これにより、開発の効率が飛躍的に向上します。

さらに、Docker の大きな利点は、アプリケーションをどの環境でも一貫して動作させられる点です。たとえば、開発者がローカル環境で動作させたアプリケーションを、そのまま本番環境に持ち込むことができます。また、複数の開発者が関わるプロジェクトでも、全員が同じ環境を共有することで「自分の環境では動くけれど、他の環境では動かない」といったトラブルを回避できます。さらに、クラウドサーバーへの展開（デプロイ）も簡単に行えるため、運用の効率が大幅に向上します。


## Docker のインストール方法（Ubuntu）

ターミナルを開き、Ubuntu に Docker をインストールできるように、Docker 関連のレポジトリを Ubuntu に登録します。

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl

sudo install -m 0755 -d /etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Docker および関連ライブラリをインストールします。


```bash
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

正しくインストールされれば次のように `docker` および `docker compose` コマンドが利用できるようになります。

```bash
docker --version
## Docker version 27.4.1, build b9d17ea
docker compose version
## Docker Compose version v2.32.1
```

続けて、Docker から GPU を利用できるように NVIDIA のサポートライブラリをインストールします。

```bash
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey |   sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list |   sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list

sudo apt-get update
sudo apt-get install nvidia-container-runtime
```

最後に、Docker 本体を一度再起動することで、Docker が GPU を認識できるようになります。

```bash
service docker restart
```

なお、実際に Docker コンテナからGPUを利用するには、Docker イメージを作成する際に、必要なオプションを指定する必要があります。次は、GPU を利用できる Docker イメージを作成する時に利用する Dockerfile の一例です。

```dockerfile
ARG PYTORCH="2.3.1"
ARG CUDA="12.1"
ARG CUDNN="8"
FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ARG UID
ARG GID
ARG USERNAME
ARG GROUPNAME

#setup environment
ENV FORCE_CUDA="1" \
    TORCH_CUDA_ARCH_LIST="8.6+PTX" \
    PATH="/usr/local/cuda/bin:$PATH" \
    TORCH_NVCC_FLAGS="-Xfatbin -compress-all" \
    CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"
```


