"""
To define a custom map function which takes a single sample input element (data sample)
and returns multiple elements (data samples).

Ref: In Tensorflow's Dataset API how do you map one element into multiple elements?
https://stackoverflow.com/questions/48471926/in-tensorflows-dataset-api-how-do-you-map-one-element-into-multiple-elements
"""

import tensorflow as tf
import numpy as np


input = [10, 20, 30]


# =========================================================================== #
# Build a dataset from a list using tf.data.Dataset.from_tensor_slices(),
# and then create an iterator to iterate over this dataset.
# =========================================================================== #
def demo1():
    """
    basic example.
    :return:
    """
    dataset = tf.data.Dataset.from_tensor_slices(input)
    iterator = dataset.make_one_shot_iterator()
    next_element = iterator.get_next()

    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(next_element))
            except tf.errors.OutOfRangeError:
                print('Finished')
                break


# =========================================================================== #
# With basic map function:
# 1. my_map_func1: call my_map_func1 on each element in the dataset, i.e. dataset = [a, b, c...]
# map() function will realize: my_map_func1(a), my_map_func1(b), my_map_func1(c), ...
# 2. my_map_func2: a map function with additional argument
# =========================================================================== #
def my_map_func1(i):
    return [i+1, i+2, i+3]


def my_map_func2(i, arg):
    return [i+arg, i+arg, i+arg]


def demo2():
    # dataset = tf.data.Dataset.from_tensor_slices(input).map(lambda x: my_map_func1(x))
    dataset = tf.data.Dataset.from_tensor_slices(input).map(lambda x: my_map_func2(x, 7))
    iterator = dataset.make_one_shot_iterator()
    next_element = iterator.get_next()

    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(next_element))
            except tf.errors.OutOfRangeError:
                print('Finished!')
                break


# =========================================================================== #
# With complex map function
#
# =========================================================================== #
def my_map_func3(i):
    # return [i, i+1, i+1]
    return [[i, i+1, i+2]]


def demo3():
    ds = tf.data.Dataset.from_tensor_slices(input)
    # ds = ds.map(map_func=lambda input: tf.py_func(func=my_map_func1, inp=[input], Tout=[tf.int64, tf.int64, tf.int64]))
    ds = ds.map(map_func=lambda input: tf.py_func(func=my_map_func3, inp=[input], Tout=[tf.int64]))
    element = ds.make_one_shot_iterator().get_next()

    with tf.Session() as sess:
        while True:
            try:
                # res = sess.run(element)
                # print(res)
                # print(type(res), len(res), type(res[0]))
                print(sess.run(element))
            except tf.errors.OutOfRangeError:
                print('Finished!')
                break


# =========================================================================== #
# Result of my_map_func1
# (11, 12, 13)      <class 'tuple'> 3 <class 'numpy.int64'>
# (21, 22, 23)
# (31, 32, 33)
# Finished!

# Result of my_map_func3
# (array([10, 11, 12]),)    <class 'tuple'> 1 <class 'numpy.ndarray'>
# (array([20, 21, 22]),)
# (array([30, 31, 32]),)
# Finished!
# =========================================================================== #


# =========================================================================== #
# With complex map function to flat
# ds after map function my_map_func4,
#     (array([10, 11, 12]),)
#     (array([20, 21, 22]),)
#     (array([30, 31, 32]),)
#     Finished!
# ds after flat_map, i.e. flat_map will flat each element, i.e. (array([10, 11, 12],), (array([10, 11, 12],)....
# 10
# 11
# 12
# 20
# 21
# 22
# 30
# 31
# 32
# Finished!
# =========================================================================== #
def my_map_func4(i):
    return np.array([i, i+1, i+2])


def demo4():
    ds = tf.data.Dataset.from_tensor_slices(input)
    ds = ds.map(map_func=lambda input: tf.py_func(func=my_map_func4, inp=[input], Tout=[tf.int64]))
    ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(x))
    element = ds.make_one_shot_iterator().get_next()

    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(element))
            except tf.errors.OutOfRangeError:
                print('Finished!')
                break


# =========================================================================== #
# With complex map function to flat, and return multiple variables
# ds after map function my_map_func5:
#     (array([b'testA', b'testA', b'testA'], dtype=object), array([10, 20, 30]))
#     (array([b'testB', b'testB', b'testB'], dtype=object), array([10, 20, 30]))
#     (array([b'testC', b'testC', b'testC'], dtype=object), array([10, 20, 30]))
#     Finished
# ds after flat_map function:
#     (b'testA', 10)
#     (b'testA', 20)
#     (b'testA', 30)
#     (b'testB', 10)
#     (b'testB', 20)
#     (b'testB', 30)
#     (b'testC', 10)
#     (b'testC', 20)
#     (b'testC', 30)
#     Finished
# =========================================================================== #
input1 = [b'testA', b'testB', b'testC']


def my_map_func5(i):
    return np.array([i, i, i]), np.array([10, 20, 30])


def demo5():
    ds = tf.data.Dataset.from_tensor_slices(input1)
    # lambda x: x will be every element in tf.data.Dataset.from(input1), input1 = [b'testA', b'testB', b'testC']
    ds = ds.map(map_func=lambda x: tf.py_func(func=my_map_func5, inp=[x], Tout=[tf.string, tf.int64]))
    ds = ds.flat_map(map_func=lambda mystr, myint: tf.data.Dataset.zip((tf.data.Dataset.from_tensor_slices(mystr),
                                                                        tf.data.Dataset.from_tensor_slices(myint))))

    element = ds.make_one_shot_iterator().get_next()

    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(element))
            except tf.errors.OutOfRangeError:
                print('Finished')
                break


# =========================================================================== #
# With clean map function to flat, with lambda
# lambda x: tf.data.Dataset.from_tensor_slices([x, x+1, x+2]) will create a dataset with 3 elements
# and then `ds.flat_map()` will flat each dataset
# =========================================================================== #
def demo6():
    ds = tf.data.Dataset.from_tensor_slices(input)
    ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices([x, x+1, x+2]))
    next_element = ds.make_one_shot_iterator().get_next()

    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(next_element))
            except tf.errors.OutOfRangeError:
                print('Finished!')
                break


# =========================================================================== #
# Does not work yet.
# =========================================================================== #
# element = { 'feat1': [2, 4], 'feat2': [3]}
#
#
# def split(element):
#     dict_of_new_elements = {
#         'feat1': [
#             element['feat1'][0],
#             element['feat1'][1]],
#         'feat2': [
#             element['feat2'],
#             element['feat2']]
#     }
#     return tf.data.Dataset.from_tensor_slices(dict_of_new_elements)
#
#
# def demo7():
#     dataset = split(element)
#     dataset.flat_map(split)


if __name__ == '__main__':
    demo6()
