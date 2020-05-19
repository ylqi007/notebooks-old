
## Goals
* Learn how to use `tf.data`


## An overview of `tf.data`
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

## Reference:
1. [Building a data pipeline](https://cs230.stanford.edu/blog/datapipeline/)