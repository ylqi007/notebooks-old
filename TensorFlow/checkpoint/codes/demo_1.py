import os
import tensorflow as tf


def demo1():
    """
    保存模型的代码。
    Use `tf.train.Saver` to save the checkpoint
    :return:
    """
    # 声明两个变量并计算他们的和
    v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
    v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
    result = v1 + v2

    init_op = tf.global_variables_initializer()

    # 声明 tf.train.Saver类用于保存模型
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init_op)
        # 将模型保存到model.ckpt文件中
        model_path = 'model/demo1/model.ckpt'
        saver.save(sess, model_path)


def demo2():
    """
    加载模型的代码。
    在加载模型的程序中也是先定义了TensorFlow计算图上所有运算，并声明了一个 `tf.train.Saver` 类。
    两段代码唯一不同的是，在加载模型的代码中没有运行变量的初始化过程，而是将变量的值通过已经保存的模型加载出来。
    The difference between demo1 and demo2 is there is no initial process in demo2.
    :return:
    """
    # 使用和保存模型代码中一样的方式来声明变量
    v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
    v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
    result = v1 + v2

    saver = tf.train.Saver()
    with tf.Session() as sess:
        # 加载已经保存的模型，并通过已经保存的模型中的变量的值来计算加法
        model_path = 'model/demo1/model.ckpt'
        saver.restore(sess, model_path)
        print(sess.run(result))


def demo3():
    """
    如果不希望重复定义图上的运算，也可以直接加载已经持久化的图。
    :return:
    """
    # 直接加载持久化的图
    model_path = 'model/demo1/model.ckpt'
    model_path1 = 'model/demo1/model.ckpt.meta'
    saver = tf.train.import_meta_graph(model_path1)

    with tf.Session() as sess:
        saver.restore(sess, model_path)
        # 通过张量的的名称来获取张量
        print(sess.run(tf.get_default_graph().get_tensor_by_name('add:0')))


def demo4():
    # 这里声明的变量名称和已经保存的模型中变量的的名称不同
    v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='other-v1')
    v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='other-v2')
    res = v1 + v2

    # 如果直接使用 tf.train.Saver() 来加载模型会报变量找不到的错误，下面显示了报错信息
    # tensorflow.python.framework.errors.FailedPreconditionError:Tensor name 'other-v2'
    # not found in checkpoint file model/model.ckpt
    # saver = tf.train.Saver()

    # 使用一个字典来重命名变量就可以加载原来的模型了
    # 这个字典指定了原来名称为 v1 的变量现在加载到变量 v1中（名称为 other-v1）
    # 名称为v2 的变量加载到变量 v2中（名称为 other-v2）
    # key -> `model.ckpt` 中的变量
    # val -> variable in current graph, i.e. v1 (with name 'other-v1')
    # Tensorflow 可以通过字典（dictionary）将模型保存时的变量名和需要加载的变量联系起来。
    saver = tf.train.Saver({'v1': v1, 'v2': v2})
    with tf.Session() as sess:
        saver.restore(sess, "model/demo1/model.ckpt")
        print(sess.run(res))


if __name__ == '__main__':
    demo4()

