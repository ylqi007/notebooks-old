from datetime import datetime
import io
import itertools
from packaging import version
from six.moves import range

import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics

print("TensorFlow version: ", tf.__version__)
# assert version.parse(tf.__version__).release[0] >= 1, \
#     "This notebook requires TensorFlow 2.0 or above."


# Download the data. The data is already divided into train and test.
# The labels are integers representing classes.
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Names of the integer classes, i.e., 0 -> T-short/top, 1 -> Trouser, etc.
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Sets up a timestamped log directory.
logdir = "logs/train_data/" + datetime.now().strftime("%Y%m%d-%H%M%S")
# Creates a file writer for the log directory.
file_writer = tf.summary.FileWriter(logdir)


def visualize_single_image():
    print("Shape: ", type(train_images), type(train_images[0]), train_images[0].shape)
    print("Label: ", type(train_labels), type(train_labels[0]), train_labels[0], "->", class_names[train_labels[0]])

    # Reshape the image for the Summary API.
    img = np.reshape(train_images[0], (-1, 28, 28, 1))

    # Create the image summary
    img_summary = tf.summary.image(name="Training data", tensor=img)

    # Using the file writer, log the reshaped image.
    # with file_writer.as_default():
    with tf.Session() as sess:
        print('img_summary: ', img_summary)
        summary = sess.run(img_summary)
        print('summary: ', summary)
        file_writer.add_summary(summary, global_step=0)


def visualize_multiple_images():
    images = np.reshape(train_images[0:25], (-1, 28, 28, 1))
    imgs_summary = tf.summary.image("25 training data samples", images, max_outputs=25)
    with tf.Session() as sess:
        summary = sess.run(imgs_summary)
        file_writer.add_summary(summary, global_step=1)


def plot_to_image(figure):
    """
    Converts the matplotlib plot specified by 'figure' to a PNG image and return it.
    The supplied figure is closed and inaccessible after this call.
    :param figure:
    :return:
    """
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    # Closing the figure prevents it from being displayed directly inside.
    plt.close(figure)
    buf.seek(0)
    # Conver PNG buffer to TF image
    image = tf.image.decode_png(buf.getvalue(), channels=4)
    # Add the batch dimension
    image = tf.expand_dims(image, 0)
    return image


def image_grid():
    """
    Return a 5x5 grid of the MNIST images as a matplotlib figure.
    :return:
    """
    # Create a figure to contain the plot.
    figure = plt.figure(figsize=(10, 10))
    for i in range(25):
        # Start next subplit
        plt.subplot(5, 5, i + 1, title=class_names[train_labels[i]])
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
    return figure


def log_arbitrary_images():
    # Prepare the plot
    figure = image_grid()
    img_summary = tf.summary.image("Training_data", plot_to_image(figure))
    with tf.Session() as sess:
        print('img_summary: ', img_summary)
        summary = sess.run(img_summary)
        print('summary: ', summary)
        file_writer.add_summary(summary, global_step=2)


if __name__ == '__main__':
    # visualize_multiple_images()
    log_arbitrary_images()





