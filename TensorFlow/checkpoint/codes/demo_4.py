import tensorflow as tf


def demo0():
    # 定义变量相加的计算
    v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
    v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')
    result = v1 + v2

    saver = tf.train.Saver()
    init_op = tf.global_variables_initializer()
    # 通过  export_meta_graph() 函数导出TensorFlow计算图的元图，并保存为json格式
    saver.export_meta_graph('model/demo4/model.ckpt.meda.json', as_text=True)
    with tf.Session() as sess:
        sess.run(init_op)
        saver.save(sess, 'model/demo4/model.ckpt')


def demo1():
    # tf.train.NewCheckpointReader()  可以读取 checkpoint文件中保存的所有变量
    reader = tf.train.NewCheckpointReader('model/demo4/model.ckpt')

    # 获取所有变量列表，这是一个从变量名到变量维度的字典
    all_variables = reader.get_variable_to_shape_map()
    for variable_name in all_variables:
        # variable_name 为变量名称， all_variables[variable_name]为变量的维度
        print(variable_name, all_variables[variable_name])

    # 获取名称为v1 的变量的取值
    print('Value for variable v1 is ', reader.get_tensor('v1'))
    '''
    v1 [1]     # 变量v1的维度为[1]
    v2 [1]     # 变量v2的维度为[1]
    Value for variable v1 is  [1.]   # 变量V1的取值为1
    '''


if __name__ == '__main__':
    demo0()
    demo1()
