[TOC]

## 1. Protocol Buffer

### 1.1 Protocol Buffer 是什么

Protobuf是Protocol Buffers的简称，它是Google公司开发的一种**数据描述语言**，*用于描述一种轻便高效的结构化数据存储格式*，并于2008年对外开源。Protobuf可以用于**结构化数据串行化**，或者说**序列化**。它的设计非常适用于在网络通讯中的数据载体，很适合做数据存储或 RPC 数据交换格式，它序列化出来的数据量少再加上以 **K-V** 的方式来存储数据，对消息的版本兼容性非常强，可用于通讯协议、数据存储等领域的语言无关、平台无关、可扩展的序列化结构数据格式。开发者可以通过Protobuf附带的工具生成代码并实现将结构化数据序列化的功能。

Protobuf中最基本的数据单元是message，是类似Go语言中结构体的存在。在message中可以嵌套message或其它的基础数据类型的成员。

教程中将描述如何用protocol buffer语言构造你的protocol buffer数据，包括`.proto`文件的语法以及如何通过`.proto`文件生成数据访问类。教程中使用的是proto3版本的protocol buffer语言。



### 1.2 为什么要发明 protocol buffers ？

## References:

1. [Protobuf语言指南](https://juejin.im/post/6844903942170624008)
2. [高效的数据压缩编码方式 Protobuf](https://halfrost.com/protobuf_encode/)
3. [Explore in every moment of the hard thinking](https://halfrost.com/)
4. [Language Guide](https://developers.google.com/protocol-buffers/docs/overview)
5. [eishay/jvm-serializers](https://github.com/eishay/jvm-serializers/wiki)
6. [protocol buffers 文档(一)-语法指导](https://www.cnblogs.com/WindSun/p/12536229.html)
7. [Protocol Buffers 开发者指南](https://phenix3443.github.io/notebook/protobuf/proto2-language-guide.html)
8. 