[TOC]

## 1. TF function notes
* [tf.global_variables或者tf.all_variables的用法](https://blog.csdn.net/UESTC_C2_403/article/details/72356235)
* [Tensorflow小技巧整理：tf.trainable_variables(), tf.all_variables(), tf.global_variables()的使用](https://blog.csdn.net/Cerisier/article/details/86523446?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight)
* [what is the difference between var.op.name and var.name in tensorflow?](https://stackoverflow.com/questions/38240050/what-is-the-difference-between-var-op-name-and-var-name-in-tensorflow)

## 1. Protocol Buffer

### 1.1 Protocol Buffer 是什么

Protobuf是Protocol Buffers的简称，它是Google公司开发的一种**数据描述语言**，*用于描述一种轻便高效的结构化数据存储格式*，并于2008年对外开源。Protobuf可以用于**结构化数据串行化**，或者说**序列化**。它的设计非常适用于在网络通讯中的数据载体，很适合做数据存储或 RPC 数据交换格式，它序列化出来的数据量少再加上以 **K-V** 的方式来存储数据，对消息的版本兼容性非常强，可用于通讯协议、数据存储等领域的语言无关、平台无关、可扩展的序列化结构数据格式。开发者可以通过Protobuf附带的工具生成代码并实现将结构化数据序列化的功能。

Protobuf中最基本的数据单元是message，是类似Go语言中结构体的存在。在message中可以嵌套message或其它的基础数据类型的成员。

教程中将描述如何用protocol buffer语言构造你的protocol buffer数据，包括`.proto`文件的语法以及如何通过`.proto`文件生成数据访问类。教程中使用的是proto3版本的protocol buffer语言。



### 1.2 为什么要发明 protocol buffers ？

## References:

* [Protobuf语言指南](https://juejin.im/post/6844903942170624008)
* [高效的数据压缩编码方式 Protobuf](https://halfrost.com/protobuf_encode/)
* [Explore in every moment of the hard thinking](https://halfrost.com/)
* [Language Guide](https://developers.google.com/protocol-buffers/docs/overview)
* [eishay/jvm-serializers](https://github.com/eishay/jvm-serializers/wiki)
* [protocol buffers 文档(一)-语法指导](https://www.cnblogs.com/WindSun/p/12536229.html)
* [Protocol Buffers 开发者指南](https://phenix3443.github.io/notebook/protobuf/proto2-language-guide.html)
* [以线性回归为例，深入理解tensorflow的Operation、Tensor、Node的区别](https://www.codenong.com/cs105854164/)
* [Tensorflow 模型保存与恢复（1）使用tf.train.Saver()](https://blog.csdn.net/JerryZhang__/article/details/85042426)
* [Tensorflow 模型保存与恢复（2）使用SavedModel](https://blog.csdn.net/JerryZhang__/article/details/85058005)
* [Tensorflow 模型保存与恢复（3）保存模型到单个文件中](https://blog.csdn.net/JerryZhang__/article/details/85082169)
* []()


