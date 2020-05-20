
## Goals
* Learn how to use `tf.data`


## 1. An overview of `tf.data`
> The `Dataset` API allows you to build an asynchronous, highly optimized data pipeline to prevent your GPU from data starvation. 
> It loads data from the disk (images or text), applies optimized transformations, creates batches and sends it to the GPU. 
> Former data pipelines made the GPU wait for the CPU to load the data, leading to performance issues.  
> [`Dataset` API 可以构建异步的、高度优化的数据管道(data pipeline)，防止训练时 GPU 出现数据不足的情况。
> 在之前的 data pipeline 中，GPU 需要等待 CPU 去加载数据，因而导致性能发挥不出来的问题。]

仅仅创建一个 `Dataset` object 并不能直接用于读取数据。因为 `Dataset` object 只是 Graph 中的一个包含一些指令的 Node。
如果想要读取数据，需要初始化 Graph，然后通过 evaluate 这个 node 去读取数据。
这要的操作看起来复杂，实则不然。此时 `Dataset` object 是 Graph 中的一部分，就需需要考虑如何将数据输入模型的细节。

此外，要想读取 `Dataset` object 中的数据，还需要两步：
创建一个 `iterator` object；
通过 `next_element = iteraotr.get_next()` 读取数据，`next_element` 是 Graph 中的一个包含下一个数据的 node。


Some more advanced tricks:
* You can easily apply transformations to your dataset. 例如，splitting words by space.
* You can shuffle, batch and pre-fetch data easily.

Why we use initializable iterators?
* We can choose to "restart" from the beginning by `sess.run(iterator.initializer)`. 
As we use only one sess over the different epochs, we need to be able to restart the iterator. 
* Some other approaches (like `tf.Estimator`) alleviate the need of using `initializable iterators` by creating a new session at each epoch. 
But this comes at a cost: the weights and the graph must be re-loaded and re-initialized with each call to `estimator.train()` or `estimator.evaluate()`.


## 2. Building an image data pipeline
我们需要根据下面的步骤进行训练：
> 1. Create the dataset from slices of the filenames and labels [从文件名和label创建 `dataset`]
> 2. Shuffle the data with a buffer size equal to the length of the dataset. This ensures good shuffling (cf. Ref 2) [shuffle 数据的时候，buffer_size 要和 length of dataset 一致！]
> 3. Parse the images from filename to the pixel values. Use multiple threads to improve the speed of preprocessing [将图像从文件中解析为像素值。可以使用多线程提高预处理速度]
> 4. (Optional for training) Data augmentation for the images. Use multiple threads to improve the speed of preprocessing [数据增强]
> 5. Batch the images [将数据批量处理]
> 6. Prefetch one batch to make sure that a batch is ready to be served at all time [预取一个批次以确保可以随时提供一个批次]
```python
dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
dataset = dataset.shuffle(len(filenames))
dataset = dataset.map(parse_function, num_parallel_calls=4)
dataset = dataset.map(train_preprocess, num_parallel_calls=4)
dataset = dataset.batch(batch_size)
dataset = dataset.prefetch(1)
```

1.其中 `parse_function` 会做下面这些事：
* read the content of the file [从 file 中直接读取出来的数据一般是 bytes 文件]
* decode using jpeg format [将 bytes 数据进行解码得到表示像素的数字数据]
* convert to float values in `[0, 1]` [数据类型转换]
* resize to size `(64, 64)` [转换成正确的图像 size]
```python
def parse_function(filename, label):
    image_string = tf.read_file(filename)

    #Don't use tf.image.decode_image, or the output shape will be undefined
    image = tf.image.decode_jpeg(image_string, channels=3)

    #This will convert to float values in [0, 1]
    image = tf.image.convert_image_dtype(image, tf.float32)

    image = tf.image.resize_images(image, [64, 64])
    return resized_image, label
```

2.其中 `train_preprocess` 是可选的，一般用于进行 `data augmentation`
* Horizontally flip
* Apply random brightness and saturation
```python
def train_preprocess(image, label):
    image = tf.image.random_flip_left_right(image)

    image = tf.image.random_brightness(image, max_delta=32.0 / 255.0)
    image = tf.image.random_saturation(image, lower=0.5, upper=1.5)

    #Make sure the image is still in [0, 1]
    image = tf.clip_by_value(image, 0.0, 1.0)

    return image, label
```


## 3. Building a text data pipeline (Skip for now)
Look at the TensorFlow `seq2seq` tutorial using the `tf.data` pipeline.
### Files Format
### Zip dataset together
### Creating the vocabulary
### Creating padding batches
### Computing the sentence’s size
### Advanced use - extracting characters


## 4. Best Practices
> One general tip mentioned in the performance guide is to put all the data processing pipeline on the CPU to make sure that the GPU is only used for training the deep neural network model:
```python
with tf.device('/cpu:0'):
    dataset = ...
```

### Shuffle and repeat
* Repeat: We need to repeat it for multiple epochs. [因为需要多次的训练。]
* Shuffle: The bigger it is, the longer it is going to take to load the data at the beginning. However a low buffer size can be disastrous for training.
[Buffer size 要足够大，太小的 buffer size 对于训练而言会是一个灾难。]
    * The best way to avoid this kind of error might be to split the dataset into `train / dev / test` in advance and already shuffle the data there
    [提前将 dataset shuffle 并分成 `train/dev/test`]
* In general, it is good to have the shuffling and repeat at the beginning of the pipeline. For instance if the input to the dataset is a list of filenames, if we directly shuffle after that the buffer of `tf.data.Dataset.shuffle()` will only contain filenames, which is very light on memory.
[通常，在 pipeline 开始之前进行 shuffle 和 repeat。`tf.data.Dataset.shuffle()` 的buffer应该只包含 filenames，因此不会需要太多的 memory。]
* Ordering between `shuffle` and `repeat`
    * Shuffle then repeat: We shuffle the dataset in a certain way, and repeat this shuffling for multiple epochs. For example, `[1, 3, 2, 1, 3, 2]` 
    [dataset 被 shuffle 之后形成的序列，这个 shuffle 之后的序列会被多次重复。]
    * repeat then shuffle： We repeat the dataset for multiple epochs and then shuffle. [1, 2, 1, 3, 3, 2]
    [这时候会在更大的范围内进行 shuffle。]
    * The second method provides a better shuffling, but you might wait multiple epochs without seeing an example.
    * You can also use `tf.contrib.data.shuffle_and_repeat()` to perform shuffle and repeat.

### Parallelization: using multiple threads
We only need to add a num_parallel_calls argument to every dataset.map() call.
[只用在每次调用 `dataset.map()` 的时候加入 `num_parallel_calls` 参数即可。]
```python
num_threads = 4
dataset = dataset.map(parse_function, num_parallel_calls=num_threads)
```

### Prefetch data
> When the GPU is working on forward / backward propagation on the current batch, we want the CPU to process the next batch of data so that it is immediately ready. 
> As the most expensive part of the computer, we want the GPU to be fully used all the time during training. 
> We call this consumer / producer overlap, where the consumer is the GPU and the producer is the CPU.
> [GPU 进行 forward/backward 训练；CPU 在 GPU 进行 training 的同时处理数据，就像流水线一样。
> GPU ==> Consumer; CPU ==> Producer]

> With `tf.data`, you can do this with a simple call to `dataset.prefetch(1)` at the end of the pipeline (after batching). 
> This will always prefetch one batch of data and make sure that there is always one ready.
> [在 data pipeline 之后，调用 `dataset.prefetch(1)` 保证总有 1 batch 的 data 准备就绪。]
```java 
dataset = dataset.batch(64)
dataset = dataset.prefetch(1)
```

### Order of the operation
> To summarize, one good order for the different transformations is:
> 1. create the dataset
> 2. shuffle (with a big enough buffer size) 3, repeat
> 3. map with the actual work (preprocessing, augmentation…) using multiple parallel calls
> 4. batch
> 5. prefetch


## Reference:
1. [Building a data pipeline](https://cs230.stanford.edu/blog/datapipeline/)
2. [Importance of buffer_size in shuffle()](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle/48096625#48096625)
3. [document of text data pipeline](https://www.tensorflow.org/tutorials/)
4. [seq2seq tutorial](https://github.com/tensorflow/nmt/)



