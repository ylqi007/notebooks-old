import tensorflow as tf
import matplotlib.pyplot as plt


TRUE_W = 3.0
TRUE_b = 2.0
NUM_EXAMPLES = 1000

inputs  = tf.random.normal(shape=[NUM_EXAMPLES])
noise   = tf.random.normal(shape=[NUM_EXAMPLES])
outputs = inputs * TRUE_W + TRUE_b + noise


class Model(object):
    def __init__(self):
        # Initialize the weights to `5.0` and the bias to `0.0`
        # in practice, these should be initialized to random values (for example, with `tf.random.normal`)
        self.W = tf.Variable(5.0)
        self.b = tf.Variable(0.0)

    def __call__(self, x):
        return self.W * x + self.b


def loss(target_y, predicted_y):
    return tf.reduce_mean(tf.square(target_y - predicted_y))


if __name__ == '__main__':
    print(tf.__version__)
    model = Model()
    assert model(3.0).numpy() == 15.0

    plt.scatter(inputs, outputs, c='b')
    plt.scatter(inputs, model(inputs), c='r')
    plt.show()

    print('Current loss: %1.6f' % loss(model(inputs), outputs).numpy())



