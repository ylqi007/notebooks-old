"""
Ref: How to map a function with additional parameter using the new Dataset api in TF1.3?
https://stackoverflow.com/questions/46263963/how-to-map-a-function-with-additional-parameter-using-the-new-dataset-api-in-tf1

"""
import tensorflow as tf
import numpy as np


def fun(x, arg):
    return x * arg


my_arg = tf.constant(3, dtype=tf.int64)
dataset = tf.data.Dataset.range(10)
dataset = dataset.map(lambda x: fun(x, my_arg))
print(dataset)

iterator = dataset.make_initializable_iterator()    # Need sess.run(iterator.initializer)
next_element = iterator.get_next()

with tf.Session() as sess:
    sess.run(iterator.initializer)

    while True:
        try:
            print(sess.run(next_element))
        except tf.errors.OutOfRangeError:
            print('Finished')
            break



# =========================================================================== #
# How to pass the value into a model
# =========================================================================== #
EPOCHS = 10
BATCH_SIZE = 16


def fun1(X, y, arg1, arg2):
    return X * arg1, y * arg2


arg1 = tf.constant(2, dtype=tf.float64)
arg2 = tf.constant(3, dtype=tf.float64)

# Using two numpy arrays to represent features and labels
features, labels = (np.array([np.random.sample((100, 2))]),
                    np.array([np.random.sample((100, 1))]))

dataset = tf.data.Dataset.from_tensor_slices((features, labels))
dataset = dataset.map(lambda X, y: fun1(X, y, arg1, arg2)).repeat().batch(BATCH_SIZE)
iterator = dataset.make_one_shot_iterator()
X, y = iterator.get_next()

# Make a simple model
net = tf.layers.dense(X, 8, activation=tf.tanh)     # Pass the first value from iterator.get_next() as input
net = tf.layers.dense(net, 8, activation=tf.tanh)
prediction = tf.layers.dense(net, 1, activation=tf.tanh)

loss = tf.losses.mean_squared_error(predictions=prediction, labels=y)   # Pass the second value from iterator.get_net() as label

train_op = tf.train.AdamOptimizer().minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(EPOCHS):
        _, loss_val = sess.run([train_op, loss])
        print('Iter: {},\tLoss: {:.4f}'.format(i, loss_val))

