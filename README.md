
# DeepNude

DeepNude Source Code 

DeepNude源代码  - 基于GAN的一条命令给小姐姐“换"衣服

去水印 (without watermark) 

带三个模型.lib文件下载地址 (with the download link of the 3 model files:cm.lib,mm.lib,mn.lib)

供广大程序员技术交流使用 (for research and development communication)

# Preinstallation

Before launch the script install these packages in your **Python3** environment:
- numpy
- Pillow
- setuptools
- six
- torch 
- torchvision
- wheel

建议使用Conda安装 :) 


```
 conda create -n deepnude -c anaconda python=3.6 numpy Pillow setuptools six pytorch torchvision wheel
 conda activate deepnude
```

# Models

* [CLI Checkpoints](https://drive.google.com/open?id=1w6ZO47To4BGh67WjeFCTBZiGVMFrK_po): *在运行之前需下载三个.lib文件，之后在项目根目录下新建checkpoints目录，将下载的三个文件放至checkpoints目录下*

* [备用磁力链接](magnet:?xt=urn:btih:7BE4EB8D640742D2FFEBD6495E9392E9E2C399BC)：
```
magnet:?xt=urn:btih:7BE4EB8D640742D2FFEBD6495E9392E9E2C399BC
```

若以上Google drive链接挂了可使用该链接。下载速度还蛮快的:)


# Launch the script

环境配好，模型下好之后便可以运行代码了！

```
 python3 main.py
```

The script will transform *input.png* to *output.png*.

# GPU

本项目默认使用id为0的GPU运行。 (default use GPU with id 0. if your environment do not have GPU, please modify the code in gan.py)

若运行环境不带GPU，则报错。如果没有GPU或想使用CPU运行程序，请将gan.py中

```
self.gpu_ids = [0] #FIX CPU
```

改为 (to)

```
self.gpu_ids = [] #FIX CPU
```

## Links
- https://pytorch.org/

