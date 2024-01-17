# Linux配置

## Ubuntu配置

### 软件镜像源

[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

备份并修改`/etc/apt/sources.list`

```txt
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
```

### 终端（fish）

```bash
sudo apt install fish
```

方法一：在`~/.bashrc`中添加（不需要迁移原有的脚本）：

```bash
if [[ $(ps --no-header --pid=$PPID --format=cmd) != "fish" ]]
then
    exec fish
fi
```

fish中运行conda：在bash中运行：

```bash
conda init fish
```

方法二：迁移脚本到`/etc/fish/config.fish`（所有用户）或`~/.config/fish/config.fish`（当前用户）

### Git

```bash
sudo apt install git
```

生成rsa密钥：默认目录为`~/.ssh`

```bash
ssh-keygen -t rsa -C "邮箱"
```

测试ssh连接：

```bash
ssh -T "地址"
```

### C/C++

1.直接安装构建基础包

```bash
sudo apt update && sudo apt install build-essential
```

2.安装（GNU C/C++）

```bash
sudo apt install gcc g++
sudo apt install gdb
sudo apt install make cmake
```

3.安装（clang）

```bash
sudo apt install clang
sudo apt install lldb
```

### CUDA

[官方安装指南](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

### Python（miniconda）

[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

下载并安装miniconda后，在`~/.condarc`中修改：

```text
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
```

清除索引缓存：

```bash
conda clean -i
```

conda命令(tldr)：

```bash
conda create --name "虚拟环境名" python=3.11
conda info --envs
conda activate "虚拟环境名" /deactivate
conda remove --name "虚拟环境名" --all
conda install "包名"
conda list
conda clean --all
```

### Rustup/crates.io

[字节源](https://rsproxy.cn/#getStarted)

1. 设置Rustup镜像，在`~/.bashrc`中添加：

   ```bash
   export RUSTUP_DIST_SERVER="https://rsproxy.cn"
   export RUSTUP_UPDATE_ROOT="https://rsproxy.cn/rustup"
   ```

   并重启终端。

2. 安装Rust

   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://rsproxy.cn/rustup-init.sh | sh
   ```

3. 设置crates.io镜像， 修改配置文件`~/.cargo/config`

   ```text
   [source.crates-io]
   replace-with = 'rsproxy-sparse'
   [source.rsproxy]
   registry = "https://rsproxy.cn/crates.io-index"
   [source.rsproxy-sparse]
   registry = "sparse+https://rsproxy.cn/index/"
   [registries.rsproxy]
   index = "https://rsproxy.cn/crates.io-index"
   [net]
   git-fetch-with-cli = true
   ```

### 实用工具

- 文本编辑器（gedit，vim）

- 文件管理器（nautilus）

- **非常好用**：命令速查Too Long Didn't Read（tldr）

  第一次运行时更新数据库（需要连接到github）

  ```bash
  tldr --update
  ```

- 系统监控（htop，btop）

- 视频音频转换（ffmpeg）

- 图像转换（imagemagick）

### 临时访问github（修改hosts）

在`/etc/hosts`中添加：注意ip地址会变，通过解析域名的网站获取。

```text
199.232.69.194          github.global.ssl.fastly.net
140.82.113.3            github.com
185.199.108.154         github.githubassets.com
```

刷新DNS：

```bash
sudo systemctl restart systemd-resolved
```

### WSL2中通过Clash for Windows设置代理

- Clash for Windows客户端设置

  - 修改端口号（默认为7890），以16514为例
  - 打开Allow LAN

- 修改`~/.bashrc`

  ```bash
  host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
  export http_proxy="http://$host_ip:[端口]"
  export https_proxy="http://$host_ip:[端口]"
  ```

- 使用root用户保留之前设置的环境变量

  运行`sudo visudo`

  - Ubuntu20.04

    加入该行

    ```text
    Defaults env_keep="http_proxy https_proxy"
    ```

  - Ubuntu22.04

    取消该行注释

    ```text
    Defaults:%sudo env_keep += "http_proxy https_proxy ftp_proxy all_proxy no_proxy"
    ```

- 测试

  - 输入`source ~/.bashrc`，通过`echo $http_proxy`检查端口号
  - 输入`wget www.google.com`检查连接。
