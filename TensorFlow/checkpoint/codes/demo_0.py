import tensorflow as tf

v = tf.Variable(0, dtype=tf.float32, name='v')
# 在没有申明滑动平均模型时只有一个变量 v，所以下面语句只会输出 v:0
for variables in tf.global_variables():
    print('Actual variable name:', variables.name)
    print('Actual variable name:', variables)

ema = tf.train.ExponentialMovingAverage(0.99)
maintain_averages_op = ema.apply(tf.global_variables())
# 在申明滑动平均模型之后，TensorFlow会自动生成一个影子变量 v/ExponentialMovingAverage
# 于是下面的语句会输出 v:0 和 v/ExponentialMovingAverage:0
for variables in tf.global_variables():
    print('Variable after exponential moving average: ', variables.name)
    print('Variable after exponential moving average: ', variables)

# print('tf.global_variable: ', tf.global_variables())
# [<tf.Variable 'v:0' shape=() dtype=float32_ref>, <tf.Variable 'v/ExponentialMovingAverage:0' shape=() dtype=float32_ref>]
# `tf.global_variables()` returns a list containing two variables


saver = tf.train.Saver()
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    sess.run(tf.assign(v, 10))
    sess.run(maintain_averages_op)
    # 保存时，TensorFlow会将v:0 和 v/ExponentialMovingAverage:0 两个变量都保存下来
    saver.save(sess, 'model/modeltest.ckpt')
    print(sess.run([v, ema.average(v)]))
    # 输出结果 [10.0, 0.099999905]


v = tf.Variable(0, dtype=tf.float32, name='v')
# 通过变量重命名将原来变量v的滑动平均值直接赋值给 V
saver = tf.train.Saver({'v/ExponentialMovingAverage': v})
with tf.Session() as sess:
    saver.restore(sess, 'model/modeltest.ckpt')
    print(sess.run(v))
    # 输出 0.099999905  这个值就是原来模型中变量 v 的滑动平均值


