
import tensorflow as tf
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile


def demo0():
    v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
    v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
    result = v1 + v2

    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)

        # 导出当前计算图的 GraphDef 部分，只需要这一步就可以完成从输入层到输出层的过程
        graph_def = tf.get_default_graph().as_graph_def()

        # 将图中的变量及其取值转化为常量，同时将图中不必要的节点去掉
        # 在下面，最后一个参数['add']给出了需要保存的节点名称
        # add节点是上面定义的两个变量相加的操作
        # 注意这里给出的是计算节点的的名称，所以没有后面的 :0
        output_graph_def = graph_util.convert_variables_to_constants(sess, graph_def, (['add']))

        # 将导出的模型存入文件
        if not tf.gfile.Exists('model/demo3/'):
            tf.gfile.MkDir('model/demo3/')
        with tf.gfile.GFile('model/demo3/combined_model.pb', 'wb') as f:
            f.write(output_graph_def.SerializeToString())


def demo1():
    """
    通过下面的程序可以直接计算定义加法运算的结果，当只需要得到计算图中某个节点的取值时，
    这提供了一个更加方便的方法，以后将使用这种方法来使用训练好的模型完成迁移学习。
    :return:
    """
    with tf.Session() as sess:
        model_filename = 'model/demo3/combined_model.pb'
        # 读取保存的模型文件，并将文件解析成对应的 GraphDef Protocol Buffer
        with gfile.FastGFile(model_filename, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())

        # 将graph_def 中保存的图加载到当前的图中，
        # return_elements = ['add: 0'] 给出了返回的张量的名称
        # 在保存的时候给出的是计算节点的名称，所以为add
        # 在加载的时候给出的张量的名称，所以是 add:0
        result = tf.import_graph_def(graph_def, return_elements=['add: 0'])
        print(sess.run(result))
        # 输出 [array([3.], dtype=float32)]


if __name__ == '__main__':
    demo1()

