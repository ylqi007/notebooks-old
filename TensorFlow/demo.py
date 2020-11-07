#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/15/20 6:13 PM
# @Author  : Shark
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
#
# 以线性回归为例，深入理解tensorflow的Operation、Tensor、Node的区别
# https://www.codenong.com/cs105854164/

# tensorflow=1.14
# python=3.7
# tensorboard --logdir ./tensorboard/linear_regression/

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 使用numpy生成200个随机点
x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]     # x_data.shape = (200, 1)
noise = np.random.normal(0, 0.02, x_data.shape)
y_data = np.square(x_data) + noise

# 定义两个placeholder存放输入数据
x = tf.placeholder(tf.float32, [None, 1], name="model_input")
y = tf.placeholder(tf.float32, [None, 1], name="model_output")

# 定义神经网络中间层
weights_L1 = tf.Variable(tf.random_normal([1, 10]), name="Dense1_weights")
biases_L1 = tf.Variable(tf.zeros([1, 10]), name="Dense1_bias")  #加入偏置项
Wx_plus_b_L1 = tf.matmul(x, weights_L1) + biases_L1
L1 = tf.nn.tanh(Wx_plus_b_L1, name="Dense_output")      #加入激活函数

# 定义神经网络输出层
weights_L2 = tf.Variable(tf.random_normal([10, 1]), name="Dense2_weights")
biases_L2 = tf.Variable(tf.zeros([1, 1], name="Dense2_bias"))    #加入偏置项
Wx_plus_b_L2=tf.matmul(L1, weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2, name="Dense2_ouput")   #加入激活函数

# 定义损失函数（均方差函数）
loss = tf.reduce_mean(tf.square(y - prediction), name="loss_function")
# 定义反向传播算法（使用梯度下降算法训练）
optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss, name="optimizer")

# tensorboard
loss_scaler = tf.summary.scalar('loss', loss)
merge_summary = tf.summary.merge_all()

# 模型保存
saver = tf.train.Saver()

gpu_options = tf.GPUOptions()
gpu_options.visible_device_list = "1"
gpu_options.allow_growth = True
config = tf.ConfigProto(gpu_options = None)

with tf.Session(config=config) as sess:
    # 变量初始化
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./tensorboard/linear_regression', graph=sess.graph)

    # 训练2000次
    for i in range(2000):
        opti, loss_, merge_summary_ = sess.run([optimizer, loss, merge_summary],
                                               feed_dict={x: x_data, y: y_data})
        writer.add_summary(merge_summary_, global_step=i)
        if i % 100 == 0:
            print("now is training {} batch,and loss is {}".format(i+1, loss_))
    save_path = saver.save(sess, "./linear_model/linear_model.ckpt")
    print("model have saved in {}".format(save_path))


# =========================================================================== #
# Conclusion
# =========================================================================== #
# 1. 声明的占位符placeholder，比如上面的model_input，是一个节点node，对应的是operation，用椭圆符号表示；
# 2. 声明的变量，把比如上面的Dense1_weights，本质上也是一个node，虽然用的是圆角矩形（namespace），将其双击展开，发现里面包含了3个节点node；
# 3. 常量、占位符、变量声明、操作函数本质上都是节点node，都是一种操作operation；
# 4. 只有在节点之间流动的箭头才表示的是tensor，实现箭头表示有tensor的流动，虚线箭头表示节点之间具有依赖关系；
# 5. graph的组成由两部分组成，即 节点node 和 边tensor，但是我们并没有直接创建tensor，既没有直接创建边啊，
# 比如有一个变量，如下：
# `x = tf.random_normal([2, 3], stddev=0.35, name = "weights")`
# 我们常常说创建了一个（2,3）的tensor，但是实际上在graph中又是一个节点node，这到底是怎了区分和理解呢？
# 可以这样理解：
# Tensor可以看做一种符号化的句柄，指向操作节点（node）的运算结果，在执行后返回这个节点运算得到的值，
# 在graph中的表现来看，就是这个节点运算之后输出的边，用一个带箭头的边来表示，这样个人觉得比较好理解。



