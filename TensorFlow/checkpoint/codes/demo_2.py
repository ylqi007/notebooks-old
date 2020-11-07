import tensorflow as tf


def demo0():
    """
    Save the model
    :return:
    """
    v = tf.Variable(0, dtype=tf.float32, name='v')
    # 在没有申明滑动平均模型时只有一个变量 v，所以下面语句只会输出 v:0
    for variables in tf.global_variables():
        print('Actual variable:', variables)
        print('Actual variable name:', variables.name)

    ema = tf.train.ExponentialMovingAverage(0.99)
    maintain_averages_op = ema.apply(tf.global_variables())
    # 在申明滑动平均模型之后，TensorFlow会自动生成一个影子变量 v/ExponentialMovingAverage
    # 于是下面的语句会输出 v:0 和 v/ExponentialMovingAverage:0
    for variables in tf.global_variables():
        print('Variable.name after exponential moving average: ', variables.name)
        print('Variable after exponential moving average: ', variables)

    # print('tf.global_variable: ', tf.global_variables())
    # [<tf.Variable 'v:0' shape=() dtype=float32_ref>, <tf.Variable 'v/ExponentialMovingAverage:0' shape=() dtype=float32_ref>]
    # `tf.global_variables()` returns a list containing two variables

    saver = tf.train.Saver()
    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_op)
        sess.run(tf.assign(v, 100))
        sess.run(maintain_averages_op)
        # 保存时，TensorFlow会将v:0 和 v/ExponentialMovingAverage:0 两个变量都保存下来
        saver.save(sess, 'model/demo2/model.ckpt')
        print(sess.run([v, ema.average(v)]))
        # 输出结果 [10.0, 0.099999905]


def demo1():
    """
    Restore the model.
    通过变量重命名直接读取变量的滑动平均值。从下面程序的输出可以看出，读取的变量 v 的值实际上是上面代码中变量 v 的滑动平均值。
    通过这个方法，就可以使用完全一样的代码来计算滑动平均模型前向传播的结果
    :return:
    """
    v = tf.Variable(0, dtype=tf.float32, name='v')
    # 通过变量重命名将原来变量v的滑动平均值直接赋值给 V
    saver = tf.train.Saver({'v/ExponentialMovingAverage': v})
    with tf.Session() as sess:
        saver.restore(sess, 'model/demo2/model.ckpt')
        print(sess.run(v))
        # 输出 0.099999905  这个值就是原来模型中变量 v 的滑动平均值


def demo2():
    """
    为了方便加载时重命名滑动平均变量，tf.train.ExponentialMovingAverage 类提供了 variables_tp_restore 函数来生成 tf.train.Saver类所需要的变量重命名字典，
    一下代码给出了 variables_to_restore 函数的使用样例
    :return:
    """
    v = tf.Variable(0, dtype=tf.float32, name='v')
    ema = tf.train.ExponentialMovingAverage(0.99)

    # 通过使用 variables_to_restore 函数可以直接生成上面代码中提供的字典
    # {'v/ExponentialMovingAverage': v}
    # 下面代码会输出 {'v/ExponentialMovingAverage': <tf.Variable 'v:0' shape=() dtype=float32_ref>}
    print(ema.variables_to_restore())

    saver = tf.train.Saver(ema.variables_to_restore())
    with tf.Session() as sess:
        saver.restore(sess, 'model/demo2/model.ckpt')
        print(sess.run(v))


if __name__ == '__main__':
    # demo0, save the model
    # demo0()
    # deom1, restore the model
    # demo1()
    # demo2
    demo2()