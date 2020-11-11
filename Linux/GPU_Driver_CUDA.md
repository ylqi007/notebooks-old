[TOC]



显卡：（GPU）主流是Nvidia的GPU，深度学习本身需要大量计算。GPU的并行计算能力，在过去几年里恰当地满足了深度学习的需求。AMD的GPU基本没有什么支持，可以不用考虑。

驱动：没有显卡驱动，就不能识别GPU硬件，不能调用其计算资源。但是呢，Nvidia在Linux上的驱动安装特别麻烦，尤其对于新手简直就是噩梦。得屏蔽第三方显卡驱动。

CUDA：是Nvidia推出的只能用于自家GPU的并行计算框架。只有安装这个框架才能够进行复杂的并行计算。主流的深度学习框架也都是基于CUDA进行GPU并行加速的，几乎无一例外。还有一个叫做cudnn，是针对深度卷积神经网络的加速库。



Reference

1. [显卡、显卡驱动、cuda 之间的关系是什么？ - Zhang Wang的回答 - 知乎](https://www.zhihu.com/question/59184480/answer/162623008)
2. [GPU，CUDA，cuDNN的理解](https://blog.csdn.net/u014380165/article/details/77340765)
3. [Different CUDA versions shown by nvcc and NVIDIA-smi](https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi)
4. [使用 apt 安装 CUDA](https://www.tensorflow.org/install/gpu?hl=zh-cn#install_cuda_with_apt)
5. [Which NVIDIA cuDNN release type for TensorFlow on Ubuntu 16.04 [closed]](https://stackoverflow.com/questions/48784645/which-nvidia-cudnn-release-type-for-tensorflow-on-ubuntu-16-04)
6. [Install TensorFlow-GPU by Anaconda (conda install tensorflow-gpu)](https://wangpei.ink/2019/03/29/Install-TensorFlow-GPU-by-Anaconda(conda-install-tensorflow-gpu)/)
7. [Python Installation - Conda Install](https://developers.google.com/earth-engine/guides/python_install-conda)

