# 使用说明：

## 作用

本脚本可以在当前工作目录下，利用自定义命令“autocpp”，来对当前目录下所有的头文件自动生成对应的.cpp 文件，已经存在不会覆盖。

.cpp文件中主要包含头文件引用，类中函数实现（需要自己实现）。

## 环境

python3

## 在 liunx 下的使用方法

- **先下载 autocpp.py**

- **创建目录** 

  `mkdir -p ~/bin`

- **把下载的脚本文件移到目录里**

  `mv impl.py ~/bin/autocpp`

- **修改脚本权限**

  `chmod +x ~/bin/autocpp`

- **添加到环境变量里**

  在 `~/.bashrc` 或 `~/.zshrc` 文件中添加以下行：

  `export PATH="$HOME/bin:$PATH"`

- **运行配置文件**

  运行 `source ~/.bashrc` 或 `source ~/.zshrc`
