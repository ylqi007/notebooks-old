**模型**可以在训练期间和训练完成后进行保存。这意味着模型可以从任意中断中恢复，并避免耗费比较长的时间在训练上。

在发布研究模型和技术时，大多数机器学习从业者分享：

* 用于创建模型的代码
* 模型训练的权重 (weight) 和参数 (parameters) 。      

共享数据有助于其他人了解模型的工作原理，并使用新数据自行尝试。

## 1. 在训练期间保存模型（以 checkpoints 形式保存）
可以使用训练好的模型而无需从头开始重新训练，或在您打断的地方开始训练，以防止训练过程没有保存。 `tf.keras.callbacks.ModelCheckpoint` 允许在训练的过程中和结束时回调保存的模型。
* `tf.keras.callbacks.ModelCheckpoint`

### 1.1 `Checkpoint` 回调用法

### 1.2 `Checkpoint` 回调选项

## 2. 这些文件是什么？
训练的权重(weights)会被保存到`checkpoint`中，即格式化文件的集合中，这些文件包含二进制格式的训练权重。`Checkpoints`包含：
* 一个或多个包含模型权重的分片。
* 索引文件，指示哪些权重存储在哪个分片中。

如果你只在一台机器上训练一个模型，你将有一个带有后缀的碎片： `.data-00000-of-00001`

## 3. 手动保存权重
* `Model.save_weights`
* `tf.keras`

## 4. 保存整个模型
### 4.1 将模型保存为HDF5文件

### 4.2 通过 saved_model 保存


## References
1. [保存和恢复](https://www.tensorflow.org/tutorials/keras/save_and_load?hl=zh-cn)       
2. [Using the SavedModel format](https://tensorflow.google.cn/guide/saved_model?hl=zh-cn)   
