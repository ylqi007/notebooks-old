
## Contents:
1. 如何将训练好的模型持久化，并学习持久化的原理；
2. 如何将 ckpt 文件转化为 pb 文件；
3. 如何用 pd 模型进行预测。

## 1. 模型持久化
为了让训练得到的模型保存下来方便下次直接调用，我们需要将训练得到的神经网络模型持久化。

### 1.1 持久化代码实现
TensorFlow 提供了 `tf.train.Saver` 类。使用 `tf.train.Saver` 保存模型时会产生多个文件，会把**计算图的结构**和**图上的参数取值**分成不同的文件存储。 <br>
[Save the model](codes/demo_1.py)

`tf.train.Saver` 保存模型时生成的文件：
* `checkpoint` 文件是检查点文件，文件保存了一个目录下所有模型文件列表。
* `model.ckpt.data` 文件保存了 TensorFlow 程序中每一个变量的取值
* `model.ckpt.index` 文件则保存了 TensorFlow 程序中变量的索引
* `model.ckpt.meta` 文件则保存了 TensorFlow 计算图的结构（可以简单理解为神经网络的网络结构），该文件可以被 `tf.train.import_meta_graph` 加载到当前默认的图来使用。

加载模型的代码基本上和保存模型的代码是一样的。在加载模型的程序中也是先定义了TensorFlow计算图上所有运算，并声明了一个 tf.train.Saver类。两段代码唯一不同的是，在加载模型的代码中没有运行变量的初始化过程，而是将变量的值通过已经保存的模型加载出来。 <br>
[Restore the model 1](codes/demo_1.py)

如果不希望重复定义图上的运算，也可以直接加载已经持久化的图，大致要分成两步：
1. 先要重新引入 graph 的结构。`model.ckpt.meta` 文件保存了 TensorFlow 计算图的结构(可以简单理解为神经网络的网络结构)，
该文件可以被 `tf.train.import_meta_graph` 加载到当前默认的图来使用；
2. 然后加载相应的数据。也就是 `saver.restore(sess, "model.ckpt")`    <br>
[Restore the model 2](codes/demo_1.py)

上述给出的例子中，默认保存和加载 TF 计算图上定义的**所有**变量。但是有时候只需要保存或加载**部分**变量。
比如已有一个训练好的五层神经网络，现在想要尝试六层的网络，则可以直接加载前五层，而仅仅训练最后一层。 <br>
为了保存或加载部分变量，在声明 `tf.train.Saver` 类的时候，**可以提供一个列表来指定需要保存或加载的变量**。    <br>
除了可以选取需要被加载的变量，`tf.train.Saver` 类也支持在保存或者加载时给变量重命名。 Tensorflow 可以通过字典(dictionary)将模型保存时的变量名和需要加载的变量联系起来。
这样做的主要目的之一就是方便使用**变量的滑动平均值**。(什么是**变量的滑动平均值**)

#### 1.1.1 变量的滑动平均值 ？






