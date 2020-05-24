
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
[Exponential average](codes/demo_2.py)

#### 1.1.2 `convert_variables_to_constants` 固化模型结构
> 使用 `tf.train.Saver` 会保存进行 TensorFlow 程序所需要的全部信息，然后有时并不需要某些信息。
> 比如在测试或者离线预测时，只需要知道如何从神经网络的输出层经过前向传播计算得到输出层即可，而不需要类似于变量初始化，模型保存等辅助接点的信息。
> 而且，将变量取值和计算图结构分成不同的文件存储有时候也不方便，于是 TensorFlow 提供了 `convert_variables_to_constants` 函数，
> 通过这个函数可以将计算图中的变量及其取值通过常量的方式保存，这样整个 TensorFlow 计算图可以统一存放在一个文件中，该方法可以固化模型结构，而且保存的模型可以移植到Android平台。 <br>
> [简单来说，就是只保存会用的变量，而一些辅助节点则不需要。] <br>

[convert_variables_to_constants](codes/demo_3.py)


### 1.2 持久化原理及数据格式
调用 `tf.train.Saver` 会生成 4 个文件。TF 模型的持久化就是通过这四个文件实现的。 
> TensorFlow是一个通过图的形式来表述计算的编程系统，TensorFlow程序中所有计算都会被表达为计算图上的节点。
> TensorFlow通过元图(MetaGraph)来记录计算图中节点的信息以及运行计算图中节点所需要的元数据。
> TensorFlow中元图是由 `MetaGraphDef Protocol Buffer` 定义的。`MetaGraphDef` 中的内容就构成了 TensorFlow 持久化的第一个文件.
```metadata json
message MetaGraphDef {
    MeatInfoDef meta_info_def = 1;
    GraphDef graph_def = 2;
    SaverDef saver_def = 3;
    map<string,CollectionDef> collection_def = 4;
    map<string,SignatureDef> signature_def = 5;
}
```
[MetaGraphDef](codes/demo_4.py) <br>
从上述的例子的输出中，可以看出 json 文件中确实有五类信息。

#### 1.2.1 `meta_info_def` 属性
> `meta_info_def` 属性是通过 `MetaInfoDef` 定义的。它记录了 TensorFlow 计算图中的元数据以及 TensorFlow 程序中所有使用到的运算方法的信息，

#### 1.2.2 `graph_def` 属性
> `graph_def` 属性主要记录了 TensorFlow 计算图上的节点信息。TensorFlow 计算图的每一个节点对应了 TensorFlow 程序中一个运算，
> 因为在 `meta_info_def` 属性中已经包含了所有运算的具体信息，所以 `graph_def` 属性只关注运算的连接结构。`graph_def` 属性是通过 `GraphDef Protocol Buffer` 定义的，`graph_def` 主要包含了一个 `NodeDef` 类型的列表。

#### 1.2.3 `saver_def` 属性
> `saver_def` 属性中记录了持久化模型时需要用到的一些参数，比如保存到文件的文件名，保存操作和加载操作的名称以及保存频率，清理历史记录等。
> `saver_def` 属性的类型为 `SaverDef`

####  1.2.4 `collection_def` 属性
> 在 TensorFlow 的计算图(tf.Graph)中可以维护不同集合，而维护这些集合的底层实现就是通过 `collection_def` 这个属性。
> `collection_def` 属性是一个从集合名称到集合内容的映射，其中集合名称为字符串，而集合内容为 `CollectionDef Protocol Buffer`。

####  1.2.5 `signature_def` 属性


> 最后一个文件的名字是固定的，叫 `checkpoint`。这个文件是 `tf.train.Saver` 类自动生成且自动维护的。
> 在 `checkpoint` 文件中维护了由一个 `tf.train.Saver` 类持久化的所有 TensorFlow 模型文件的文件名。
> 当某个保存的 TensorFlow 模型文件被删除的，这个模型所对应的文件名也会从 `checkpoint` 文件中删除。
> `checkpoint` 中内容格式为 `CheckpointState Protocol Buffer`，下面给出了 CheckpointState 类型的定义。
```metadata json
message CheckpointState {
    string model_checkpoint_path = 1,   # 保存了最新的TensorFlow模型文件的文件名。
    repeated string all_model_checkpoint_paths = 2; # 列表了当前还没有被删除的所有TensorFlow模型文件的文件名。
}
```
> `model_checkpoint_path` 属性保存了最新的 TensorFlow 模型文件的文件名。 `all_model_checkpoint_paths` 属性列表了当前还没有被删除的所有 TensorFlow 模型文件的文件名。




## Reference:
1. [tensorflow学习笔记——模型持久化的原理，将CKPT转为pb文件，使用pb模型预测](https://www.cnblogs.com/wj-1314/p/11289619.html)
