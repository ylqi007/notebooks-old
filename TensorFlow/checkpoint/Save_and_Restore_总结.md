
## 1. 持久化代码实现
* `tf.train.Saver` class
    * `checkpoint`文件是检查点文件，文件保存了一个目录下所有模型文件列表;
    * `model.ckpt.data`文件保存了TensorFlow程序中每一个变量的取值;
    * `model.ckpt.index`文件则保存了TensorFlow程序中变量的索引;
    * `model.ckpt.meta`文件则保存了TensorFlow计算图的结构（可以简单理解为神经网络的网络结构），该文件可以被 `tf.train.import_meta_graph` 加载到当前默认的图来使用。
* `tf.train.Saver.restore()`
* Tensorflow 可以通过字典（dictionary）将模型保存时的变量名和需要加载的变量联系起来。

## References:
1. [tensorflow学习笔记——模型持久化的原理，将CKPT转为pb文件，使用pb模型预测](https://www.cnblogs.com/wj-1314/p/11289619.html)     
