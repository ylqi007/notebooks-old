# _*_coding:utf-8_*_
import tensorflow as tf
from tensorflow.python.framework import graph_util
from create_tf_record import *

resize_height = 224  # 指定图片高度
resize_width = 224  # 指定图片宽度


def freeze_graph(input_checkpoint, output_graph):
    """
    :param input_checkpoint:
    :param output_graph: PB 模型保存路径
    :return:
    """
    # 检查目录下ckpt文件状态是否可用
    # checkpoint = tf.train.get_checkpoint_state(model_folder)
    # 得ckpt文件路径
    # input_checkpoint = checkpoint.model_checkpoint_path

    # 指定输出的节点名称，该节点名称必须是元模型中存在的节点
    output_node_names = "InceptionV3/Logits/SpatialSqueeze"
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
    graph = tf.get_default_graph()  # 获得默认的图
    input_graph_def = graph.as_graph_def()  # 返回一个序列化的图代表当前的图

    with tf.Session() as sess:
        saver.restore(sess, input_checkpoint)  # 恢复图并得到数据
        # 模型持久化，将变量值固定
        output_graph_def = graph_util.convert_variables_to_constants(
            sess=sess,
            # 等于:sess.graph_def
            input_graph_def=input_graph_def,
            # 如果有多个输出节点，以逗号隔开
            output_node_names=output_node_names.split(","))

        # 保存模型
        with tf.gfile.GFile(output_graph, "wb") as f:
            f.write(output_graph_def.SerializeToString())  # 序列化输出
        # 得到当前图有几个操作节点
        print("%d ops in the final graph." % len(output_graph_def.node))

        # for op in graph.get_operations():
        #     print(op.name, op.values())