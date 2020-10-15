import tensorflow as tf

# dataset is Dataset object with type=tf.string
dataset = tf.data.TextLineDataset('./data/file.txt')
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

# Apply transormations to dataset
dataset1 = dataset.map(lambda string: tf.string_split([string]).values)
# Shuffling the dataset is straightforward
dataset1 = dataset1.shuffle(buffer_size=3)  # It will load elements 3 by 3 and shuffle them at each iteration.
dataset1 = dataset1.batch(2)
# dataset1 = dataset1.prefetch(1)     # It will always have one batch ready to be loaded
iterator1 = dataset1.make_one_shot_iterator()
next_element1 = iterator1.get_next()


def wrong_demo():
    """
    This will print the following forever:
        Tensor("IteratorGetNext:0", shape=(), dtype=string)
        Tensor("IteratorGetNext_1:0", shape=(), dtype=string)
    But I am still confusing about the reason.
    :return:
    """
    for line in dataset:
        print(line)


def right_demo1():
    with tf.Session() as sess:
        for i in range(3):
            print(sess.run(next_element))


def right_demo2():
    print(next_element1)
    with tf.Session() as sess:
        for i in range(2):
            print(sess.run(next_element1))


def right_demo3():
    dataset2 = tf.data.TextLineDataset('./data/file.txt').batch(2)
    iterator2 = dataset2.make_initializable_iterator()
    init_op = iterator2.initializer
    next_element2 = iterator2.get_next()
    with tf.Session() as sess:
        sess.run(init_op)
        print(sess.run(next_element2))
        print(sess.run(next_element2))
        sess.run(init_op)
        print(sess.run(next_element2))
        print(sess.run(next_element2))


if __name__ == '__main__':
    print(dataset)
    # Wrong demo
    # wrong_demo()
    # Right demo 1
    # right_demo1()
    # right_demo2()
    right_demo3()
