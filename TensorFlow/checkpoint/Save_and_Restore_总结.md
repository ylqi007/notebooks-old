
## 1. 持久化代码实现
* `tf.train.Saver` class
    * `checkpoint`文件是检查点文件，文件保存了一个目录下所有模型文件列表;
    * `model.ckpt.data`文件保存了TensorFlow程序中每一个变量的取值;
    * `model.ckpt.index`文件则保存了TensorFlow程序中变量的索引;
    * `model.ckpt.meta`文件则保存了TensorFlow计算图的结构（可以简单理解为神经网络的网络结构），该文件可以被 `tf.train.import_meta_graph` 加载到当前默认的图来使用。
* `tf.train.Saver.restore()`
* Tensorflow 可以通过字典（dictionary）将模型保存时的变量名和需要加载的变量联系起来。


## 2. CKPT v.s. PB
TensorFlow模型持久化-保存模型文件
* `CKPT` 格式能够保存模型训练过程中的数据，防止训练过程中断导致数据丢失；
* `PB` 格式能够提供便捷的离线测试，其中只保存了模型前向传播过程中的值，其中不再是变量，而是以常量的形式将模型参数进行保存；因此，数据不再会变动，不能进行反馈调节；


## References:
1. [tensorflow学习笔记——模型持久化的原理，将CKPT转为pb文件，使用pb模型预测](https://www.cnblogs.com/wj-1314/p/11289619.html)     
2. [TensorFlow模型持久化-保存模型文件](https://chenzhen.online/2019/03/04/TensorFlow%E6%A8%A1%E5%9E%8B%E6%8C%81%E4%B9%85%E5%8C%96-%E4%BF%9D%E5%AD%98%E6%A8%A1%E5%9E%8B%E6%96%87%E4%BB%B6/)




