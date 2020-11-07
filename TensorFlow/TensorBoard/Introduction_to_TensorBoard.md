[Introduction to TensorBoard](https://www.easy-tensorflow.com/tf-tutorials/basics/introduction-to-tensorboard)

> In Google’s words: “The computations you'll use TensorFlow for (like training a massive deep neural network) can be complex and confusing. To make it easier to understand, debug, and optimize TensorFlow programs, we've included a suite of visualization tools called TensorBoard.”        
> TensorBoard was created as a way to help you understand the flow of tensors in your model so that you can debug and optimize it. 
> It is generally used for two main purposes:
> * Visulizing the Graph
> * Writing Summaries to Visulize Learning 

## 1. Visulizing the Graph
> To make our TensorFlow program `TensorBoard-activated`, we need to add a very few lines of code to it. 
> This will export the TensorFlow operations into a file, called `event file` (or event log file). 
> TensorBoard is able to read this file and give insight into the model graph and its performance. 
>
> 要想用 TensorBoard 图像化一个程序，首相要得到这个程序的 log files(i.e. event files)。To write event files, we first need to create a `writer` for those logs, using this code:
> `writer = tf.summary.FileWriter([logdir], [graph])`
> * `[logdir]` is the folder where you want to store those log files;
> * '[graph]' is the graph of the program we are working on. 
>
> There are two ways to get the graph:
> 1. `Call the graph using `tf.get_default_graph()`, which returns the default graph of the program;
> 2. Set it as `sess.graph` which returns the session's graph (note that this requires us to already have created a session).
>

## 2. Writing Summaries to Visualize Learning
> `Summary` is a special TensorBoard operation that takes in regular tensor and outputs the summarized data to disk (i.e. in the event file).
> Basically, there are three main types of summaries:
> 1. tf.summary.scalar: used to write a single scalar-valued tensor (like classificaion loss or accuracy value)
> 2. tf.summary.histogram: used to plot histogram of all the values of a non-scalar tensor (like weight or bias matrices of a neural network)
> 3. tf.summary.image: used to plot images (like input images of a network, or generated output images of an autoencoder or a GAN) 

### 2.1 tf.summary.scalar
> It's for writing the values of a scalar tensor that changes over time or iterations. 
> In the case of neural networks (say a simple network for classification task), it's usually used to monitor the changes of loss function or classification accuracy.  
> [在分类任务的网络中，`tf.summary.scalar` 常用了记录像 `loss function`, `classification accuracy` 这些信息。]

> [demo code](codes/demo_2.py)      
> 上述代码中记录了一个 tensor 变量的变化，通过 100 次的 `sess.run(init)` 得到 100 次初始化的 `x_scalar`，并记录其变化。

### 2.2 tf.summary.histogram
> It's for plotting the histogram of the values of a non-scalar tensor. 
> This gives us a view of how does the histogram (and the distribution) of the tensor values change over time or iterations. 
> In the case of neural networks, it's commonly used to monitor the changes of weights and biases distributions. 
> It's very useful in detecting irregular behavior of the network parameters (like when many of the weights shrink to almost zero or grow largely).         
> [`tf.summary.histogram` 用来记录非标量的张量信息。根据张量的直方图(i.e. 分布)来记录张量随 iteration 的变化。
> 通常在神经网络中用来监控 `weights` and `biases` 分布的变化。用来检测是否有不正常的变化，比如快速衰减到0, 或是增长特别快。]

![histogram res](images/tensorboard_3_7.png)
* The `Distributions` tab contains a plot that shows the distribution of the values of the tensor (y-axis) through steps (x-axis).You might ask what are the light and dark colors?     
The answer is that each line on the chart represents a percentile in the distribution over the data. For example, the bottom line (the very light one) shows how the minimum value has changed over time, and the line in the middle shows how the median has changed. Reading from top to bottom, the lines have the following meaning: [maximum, 93%, 84%, 69%, 50%, 31%, 16%, 7%, minimum]        
[我的理解是，每一条线都展示了不同值的变化。比如最下面那条线体现的是最小值的变化，最上面的那条线表现的是最大值的变化。从图中可以看出，经过 tf 初始化后生成的张量数据分布还算均衡。
其中每条线的含义是[maximum, 93%, 84%, 69%, 50%, 31%, 16%, 7%, minimum].
These percentiles can also be viewed as standard deviation boundaries on a normal distribution: [maximum, μ+1.5σ, μ+σ, μ+0.5σ, μ, μ-0.5σ, μ-σ, μ-1.5σ, minimum] so that the colored regions, read from inside to outside, have widths [σ, 2σ, 3σ] respectively. ]
* Similarly, in the `histogram` panel, each chart shows temporal "slices" of data, where each slice is a histogram of the tensor at a given step. It's organized with the oldest timestep in the back, and the most recent timestep in front. 
![histogram res](images/tensorboard_3_8.png)

> As it was shown in the code, you need to run each summary (e.g. sess.run([scalar_summary, histogram_summary])) and then use your writer to write each of them on the disk. 
> In practice, you might use tens and hundreds of such summaries to track different parameters in your model. 
> This makes running and writing the summaries extremly inefficient. 
> The way around it is to merge all summaries in your graph and run them at once inside your session. This can be done using `tf.summary.merge_all()` method.  
> [如果要想记录每个 summary，首先要 run each summary，然后用 FileWiter 将每个 summary 写入 event file 中。
> 但是如果有成千上万个 summary，每一都要 run，岂不是要累死人啊。所以可以通过 `tf.summary.merge_all()` 将所有 summary 合并到一起。]
[demo code](codes/demo_4.py)

### 2.3 tf.summary.image
> As its name shows, this type of summary is for writing and visualizing tensors as images. 
> In the case of neural networks, this is usually used for tracking the images that are either fed to the network (say in each batch) or the images generated in the output (such as the reconstructed images in an autoencoder; or the fake images made by the generator model of a Generative Adverserial Network). 
> However, in general, this can be used for plotting any tensor. For example, you can visualize a weight matrix of size 30x40 as an image of 30x40 pixels. 
`tf.summary.image(name, tensor, max_outputs=3)`
>* `name` is the name for the generated node (i.e. operation);
>* `tensor` is the desired tensor to be written as an image summary, 
> The tensor that you feed to `tf.summary.image` must be a 4-D tensor of shape `[batch_size, height, width, channels]` where batch_size is the number of images in the batch, height and width determines the size of the image and channel is: 1: for Grayscale images. 3: for RGB (i.e. color) images. 4: for RGBA images (where A stands for alpha; see RGBA). 
>* `max_outputs` is the maximum number of elements from tensor to generate images for.

>[demo code](codes/demo_5.py)
![image res](images/tensorboard_3_9.png)

