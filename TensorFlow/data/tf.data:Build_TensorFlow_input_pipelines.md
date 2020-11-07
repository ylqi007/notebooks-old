# tf.data: Build TensorFlow input pipeline
> The `tf.data` API enables you to build complex input pipelines from simple, reusable pieces. 
> The `tf.data` API makes it possible to handle large amounts of data, read from different data formats, and perform complex transformations.
> [`tf.data` 可以处理大量的数据，读取不同格式的数据，并进行各种复杂操作。]
> 
> The `tf.data` API introduces a `tf.data.Dataset` abstraction that represents a sequence of elements, in which each element consists of one or more components. 
> For example, in an image pipeline, an element might be a single training example, with a pair of tensor components representing the image and its label.
> [`tf.data.Dataset` 是一个 class，代表一系列的 elements，其中每个 element 可以包含多个组件。
> 比如，对于一个 image data pipeline，每个 element 是一个单独的 training example，而每个 training example 有两个组件(image + its label)组成。]
> 
> There are two distinct ways to create a dataset:
> * A data source constructs a `Dataset` from data stored in memory or in one or more files.
> [从在 memory 或硬盘中的文件开始创建一个 `Dataset`]
> * A data transformation constructs a dataset from one or more `tf.data.Dataset` objects.
> [在一个或多个 `tf.data.Dataset` 的基础上进行一系列变换(transformation)，创建一个新的 `Dataset` Object。]

## 1. Basic mechanics
要想创建一个 input pipeline，必须从一个 data source 开始。比如：
* 从 **data in memory** 开始创建，则可以用 `tf.data.Dataset.from_tensors()` 或者 `tf.data.Dataset.from_tensor_slices()`
* 从 **TFRecord format file** 开始创建，则可以用 `tf.data.TFRecordDataset()`
* 从 **Dataset Object** 开始，在此基础上进行一些列变换，比如 `Dataset.map()`, `Dataset.batch()`....

### 1.1 Dataset structure
> A dataset contains elements that each have the **same (nested) structure** and the individual components of the structure can be of any type representable by `tf.TypeSpec`.
> [数据集包含每个具有相同（嵌套）结构的元素，并且该结构的各个组件可以是tf.TypeSpec可表示的任何类型。]
> * [以上应该是基于 `tf_v2`]
> 
> The `Dataset` transformations support datasets of any structure. When using the `Dataset.map()`, and `Dataset.filter()` transformations, 
> which apply a function to each element, **the element structure determines the arguments of the function**.
> [任何结构的 `Dataset` 都支持 transformation。当用 `Dataset.map()` or `Dataset.filter()` 的时候，指定的 `function` 会作用在每一个 element 上。
> **并且由每个 element 的数据结构决定 function 的 arguments。**]

## 2. Reading input data
### 2.1 Consuming Numpy arrays
> If all of your input data fits in memory, the simplest way to create a `Dataset` from them is to convert them to `tf.Tensor` objects and use `Dataset.from_tensor_slices()`.
> [如果 input data 在 memory 中，最简单的创建 `Dataset` 的方式是通过 `Dataset.from_tensor_slices()` 将其转换成 `tf.Tensor`。]
```python
train, test = tf.keras.datasets.fashion_mnist.load_data()
images, labels = train
images = images/255
dataset = tf.data.Dataset.from_tensor_slices((images, labels))
```
* This works well for a small dataset, but wastes memory--because the contents of the array will be copied multiple times--and can run into the 2GB limit for the tf.GraphDef protocol buffer.
[适用于小型的 dataset，但是比较占用 memory。]

### 2.2 Consuming Python generators
> The `Dataset.from_generator` constructor converts the python generator to a fully functional `tf.data.Dataset`.

### 2.3 Consuming TFRecord data
> The `tf.data` API supports a variety of file formats so that you can process large datasets that do not fit in memory. 
> For example, the **TFRecord** file format is a simple record-oriented binary format that many TensorFlow applications use for training data. 
> The `tf.data.TFRecordDataset` class enables you to stream over the contents of one or more TFRecord files as part of an input pipeline.
> [`tf.data` API 支持多种格式的数据文件，比如 TFRecord。TFRecord 文件是一种常常用于 TensorFlow 训练的二进制文件。
> `tf.data.TFRecordDataset` 可以将一个或多个 TFRecord 文件作为输入，输入到 input pipeline。]
>
> The `filenames` argument to the `TFRecordDataset` initializer can either be a string, a list of strings, or a `tf.Tensor` of strings. 
> Therefore if you have two sets of files for training and validation purposes, you can create a factory method that produces the dataset, taking filenames as an input argument
> [如果有两个数据集分别用于 training and validation，则可以通过一个工厂类，将 filenames 作为输入的参数。]
> 
> Many TensorFlow projects use serialized `tf.train.Example` records in their TFRecord files. These need to be decoded before they can be inspected。
> [TFRecord 文件中，通常是一些列的 serialized `tf.train.Example` records。这些 records 在使用之前必须要先经过 decode。]

### 2.4 Consuming text data
> Many datasets are distributed as one or more text files. The `tf.data.TextLineDataset` provides an easy way to extract lines from one or more text files. 
> Given one or more filenames, a `TextLineDataset` will produce one string-valued element per line of those files.

### 2.5 Consuming CSV data

### 2.6 Consuming sets of files


## 3. Batching dataset elements
### 3.1 Simple batching
> The simplest form of batching stacks `n` consecutive elements of a dataset into a single element. 
> The `Dataset.batch()` transformation does exactly this, with the same constraints as the `tf.stack()` operator, 
> applied to each component of the elements: i.e. for each component i, all elements must have a tensor of the exact same shape. 
> [简单的 Batching 操作就是将 dataset 中的 n 个连续的 elements 堆成一个单独的 element。
> 其中 Batching 涉及到的 `stack()` 操作会作用到 dataset 中 element 的每一个 component，因此要求 dataset 中的 element 都要有完全相同的 shape。]
> 
> While `tf.data` tries to propagate shape information, the default settings of `Dataset.batch` result in an unknown batch size because the last batch may not be full. 
> [`Dataset.batch()` 的默认设置会导致未知的 batch shape，因为最后一个 batch 可能不是完全的。]
> Use the `drop_remainder` argument to ignore that last batch, and get full shape propagation.

### 3.2 Batching tensors with padding
> The above recipe works for tensors that all have the same size. 
> However, many models (e.g. sequence models) work with input data that can have varying size (e.g. sequences of different lengths). 
> To handle this case, the `Dataset.padded_batch` transformation enables you to batch tensors of different shape by specifying one or more dimensions in which they may be padded.
> [对于 shape 不同的 tensors，可以通过 padding 的方式处理。]
```python
import tensorflow as tf
dataset = tf.data.Dataset.range(100)
dataset = dataset.map(lambda x: tf.fill([tf.cast(x, tf.int32)], x))
dataset = dataset.padded_batch(4, padded_shapes=(None,))
iterator = dataset.make_one_shot_iterator()
next = iterator.get_next()
with tf.Session() as sess:
    for i in range(3):
        print(sess.run(next))
```
And the output of above recipe is 
```python
[[0 0 0]
 [1 0 0]
 [2 2 0]
 [3 3 3]]
[[4 4 4 4 0 0 0]
 [5 5 5 5 5 0 0]
 [6 6 6 6 6 6 0]
 [7 7 7 7 7 7 7]]
[[ 8  8  8  8  8  8  8  8  0  0  0]
 [ 9  9  9  9  9  9  9  9  9  0  0]
 [10 10 10 10 10 10 10 10 10 10  0]
 [11 11 11 11 11 11 11 11 11 11 11]]
```
> The Dataset.padded_batch transformation allows you to set different padding for each dimension of each component, and it may be variable-length (signified by None in the example above) or constant-length. 
> It is also possible to override the padding value, which defaults to 0.
> []

## 4. Training workflows
### 4.1 Processing multiple epochs
> The `tf.data` API offers two main ways to process multiple epochs of the same data.
> * The simplest way to iterate over a dataset in multiple epochs is to use the `Dataset.repeat()` transformation.
>   * Applying the `Dataset.repeat()` transformation with no arguments will repeat the input indefinitely.
>   * `dataset.repeat(3).batch(128)`: The `Dataset.repeat` transformation concatenates its arguments without signaling the end of one epoch and the beginning of the next epoch. [因为 `repeat` 会将 elements 自动串联起来。]
>   * `dataset.batch(128).repeat(3)`: 每一个 epoch 完成之后重新开始。
> * If you would like to perform a custom computation (e.g. to collect statistics) at the end of each epoch then it's simplest to restart the dataset iteration on each epoch.
> [通过简单的 for loop 多次计算。]
```python
epochs = 3
dataset = titanic_lines.batch(128)
for epoch in range(epochs):
    for batch in dataset:
        print(batch.shape)
    print("End of epoch: ", epoch)
```

> A repeat before a shuffle mixes the epoch boundaries together.
> [先进行 repeat，再进行 shuffle 的话，会消除边界的限制，也就是多个 epoches 混合在一起，再进行 shuffle。]

### 4.2 Randomly shuffling input data
> The `Dataset.shuffle()` transformation maintains a fixed-size buffer and chooses the next element uniformly at random from that buffer.
> Since the buffer_size is 100, and the batch size is 20, the first batch contains no elements with an index over 120.
> [通常 `buffer_size` 要足够大，才能保证性能。参考 Ref3]


## 5. Preprocessing data
> The Dataset.map(f) transformation produces a new dataset by applying a given function f to each element of the input dataset.
> The function `f` takes the tf.Tensor objects that represent a single element in the input, and returns the tf.Tensor objects that will represent a single element in the new dataset.

### 5.1 Decoding image data and resizing it
Example: `dataset.map(parse_image)`

### 5.2 Applying arbitrary Python logic
* **Exampel**
> For performance reasons, use TensorFlow operations for preprocessing your data whenever possible. 
> However, it is sometimes useful to call external Python libraries when parsing your input data. You can use the tf.py_function() operation in a Dataset.map() transformation.

### 5.3 Parsing `tf.Example` protocol buffer messages
> Many input pipelines extract `tf.train.Example protocol buffer messages from a TFRecord format. 
> Each `tf.train.Example` record contains one or more "features", and the input pipeline typically converts these features into tensors.
> [每个 `tf.train.Example` 包含一个 `features` (结尾有s)，而这个 `features` 又包含一个 `feature`，这个 `feature` 是dict形式表示的。]
```python
raw_example = next(iter(dataset))
parsed = tf.train.Example.FromString(raw_example.numpy())

feature = parsed.features.feature
raw_img = feature['image/encoded'].bytes_list.value[0]
img = tf.image.decode_png(raw_img)
plt.imshow(img)
plt.axis('off')
_ = plt.title(feature["image/text"].bytes_list.value[0])

```
### 5.4 Time series windowing (skip for now)

### 5.5 Resampling
> When working with a dataset that is very **class-imbalanced**, you may want to resample the dataset. `tf.data` provides two methods to do this.
> [当训练数据非常不平衡的时候，可以通过 resample 进行处理。]

> A common approach to training with an imbalanced dataset is to balance it. `tf.data` includes a few methods which enable ths workflow.
> [即不平衡就想办法平衡它。]

#### Datasets sampling (!!!)
> One approach to resampling a dataset is to use `sample_from_datasets`. This is more applicable when you have a separate `data.Dataset` for each class.
> One problem with the above `experimental.sample_from_datasets` approach is that **it needs a separate `tf.data.Dataset` per class**. 
> Using `Dataset.filter` works, but results in all the data being loaded twice.

#### Rejection resmapling (!!!)
> The `data.experimental.rejection_resample` function can be applied to a dataset to rebalance it, while only loading it once. 
> Elements will be dropped from the dataset to achieve balance.
> `data.experimental.rejection`_resample takes a `class_func` argument. 
> This `class_func` is applied to each dataset element, and is used to determine which class an example belongs to for the purposes of balancing.

## 6. Iterator Checkpointing (!!!)
训练的过程和参数可以存在 checkpoint 文件中，以便可以 restore 继续进行训练。
> It could be useful if you have a large dataset and don't want to restart the dataset from the begining on each restart.
> Since transformations such as `shuffle` and `prefetch` require buffering elements within the iterator.
> To include your iterator in a checkpoint, pass the iterator to the `tf.train.Checkpoint` constructor.
> [所以可以考虑将 iterator 也包含在一个 checkpoint 中。]

## 7. Using high-level APIs (skip)
### tf.keras

### tf.estimator


## Reference:
1. [tf.data: Build TensorFlow input pipeline](https://www.tensorflow.org/guide/data)
2. [TFRecord and tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord)
3. [Importance of buffer_size in shuffle()](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle/48096625#48096625)
4. [Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)