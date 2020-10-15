
TensorFlow 训练后的模型可以保存 `checkpoint` 文件或者 `pb` 文件。
`checkpoint` 文件是结构与权重分离的四个文件，便于训练；`pb` 文件则是 graph_def 的序列化文件，类似与 caffemodel，便于发布和离线测试。
官方提供的 `freeze_graph.py` 脚本可以将 `ckpt` 文件转换为 `pb` 文件。

如下面的例子中的四个文件：
```bash
-rw-rw-r--  1 root root       109 May 13  2019 checkpoint
-rw-rw-r--  1 root root 248007028 May 13  2019 yolov3_coco.ckpt.data-00000-of-00001
-rw-rw-r--  1 root root     14499 May 13  2019 yolov3_coco.ckpt.index
-rw-rw-r--  1 root root 250021107 May 13  2019 yolov3_coco.ckpt.meta
```

1). `checkpoint` 文件保存断点列表，可以用来迅速查找最近一次的断点文件。第一行就是最近的断点文件，从第二行开始保存的就是一些训练中保存的断点文件。
```python 
model_checkpoint_path: "yolov3_test_loss=10.1185.ckpt-30"
all_model_checkpoint_paths: "yolov3_test_loss=12.0302.ckpt-21"
all_model_checkpoint_paths: "yolov3_test_loss=11.0445.ckpt-22"
all_model_checkpoint_paths: "yolov3_test_loss=11.0670.ckpt-23"
all_model_checkpoint_paths: "yolov3_test_loss=11.2440.ckpt-24"
all_model_checkpoint_paths: "yolov3_test_loss=10.6401.ckpt-25"
all_model_checkpoint_paths: "yolov3_test_loss=10.6619.ckpt-26"
all_model_checkpoint_paths: "yolov3_test_loss=10.7017.ckpt-27"
all_model_checkpoint_paths: "yolov3_test_loss=10.3488.ckpt-28"
all_model_checkpoint_paths: "yolov3_test_loss=10.2554.ckpt-29"
all_model_checkpoint_paths: "yolov3_test_loss=10.1185.ckpt-30"
```

2). `yolov3_coco.ckpt.meta` 是 MetaGraphDef 序列化的二进制文件，保存了网络结构相关的数据(也就是计算图的结构，可以理解为神经网络的网络结构)，包括 `graph_def` 和 `saver_def` 等等。

3). `yolov3_coco.ckpt.index` 是数据索引文件。存储的核心内容是以 `tensor name` 为键，以 `BundleEntry` 为值的表格 entries；`BundleEntry` 的主要内容是权值的类型、形状、偏移、校验等信息。
index 文件由 `data block/index block/footer` 等组成，构建时主要涉及 `BundleWriter, TableBuilder, BlockBuilder` 几个类，除了 `BundleEntry` 的序列化，还涉及 `tensor name` 的编码以及优化(比如丢弃重复的前缀)和 data block 的 snappy 压缩。

4). `yolov3_coco.ckpt.data-00000-of-00001` 是数据文件，保存的是所有变量的实际值即网络权值。因此，它的尺寸通常要大得多。

简单来说就是：图结构(`.meta`) ==> 索引(`.index`) ==> 具体权重值(`.data-00000-of-00001`)。







## Reference:
1. [为什么tesnorflow保存model.ckpt文件会生成4个文件？](https://www.zhihu.com/question/61946760)
2. []()
3. []()
4. []()
5. []()


