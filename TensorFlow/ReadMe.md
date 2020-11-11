## Menu
| 日期 |文件 | 解释 |
| :------------- | :------------- |:------------- |
| 20201025 | [tf_Variables](tf_Variables.md) |  |
| 20201025 | [tf_Sharing_Variables](tf_Sharing_Variables.md) |  |

## TODO


---
* `tf.data.Dataset.map()` use function with additional argument
    * [demo2_map_func_with_argument.py](./data/codes/demo2_map_func_with_argument.py)
    * [demo3_dataset_with_map_flat_map.py](./data/codes/demo3_dataset_with_map_flat_map.py)
    
* [TensorBoard](TensorBoard/)
    * [Displaying_Image_Data_in_TensorBoar](TensorBoard/Displaying_Image_Data_in_TensorBoard.md)
    * [Inroduction_to_TensorBoard](TensorBoard/Inroduction_to_TensorBoard.md)



To Read:
- [ ] [Difference between `tf.data.Dataset.map()` and `tf.data.Dataset.apply()`](https://stackoverflow.com/questions/47091726/difference-between-tf-data-dataset-map-and-tf-data-dataset-apply)
- [ ] [Returning dataset from tf.data.Dataset.map() causes 'TensorSliceDataset' object has no attribute 'get_shape' error](https://stackoverflow.com/questions/50809257/returning-dataset-from-tf-data-dataset-map-causes-tensorslicedataset-object)
- [ ] [How do you send arguments to a generator function using tf.data.Dataset.from_generator()?](https://stackoverflow.com/questions/52443273/how-do-you-send-arguments-to-a-generator-function-using-tf-data-dataset-from-gen)
- [ ] [How can parse_fn be put into tf.data.map without arguments? ](https://github.com/tensorflow/tensorflow/issues/23322)
- [ ] [tf.data: Build TensorFlow input pipelines](https://s0www0tensorflow0org.icopy.site/guide/data)


* [保存在TensorFlow中后生成的.index和.data-00000-of-00001文件代表什么？](https://stackoom.com/question/32ufU/%E4%BF%9D%E5%AD%98%E5%9C%A8TensorFlow%E4%B8%AD%E5%90%8E%E7%94%9F%E6%88%90%E7%9A%84-index%E5%92%8C-data-of-%E6%96%87%E4%BB%B6%E4%BB%A3%E8%A1%A8%E4%BB%80%E4%B9%88)

* [[442]tf.Graph().as_default()](https://blog.csdn.net/xc_zhou/article/details/84794226)
  * 图就是呈现这些画的纸，你可以利用很多线程生成很多张图，但是默认图就只有一张。
  * tf.Graph().as_default() 表示将这个类实例，也就是新生成的图作为整个 tensorflow 运行环境的默认图，如果只有一个主线程不写也没有关系，tensorflow 里面已经存好了一张默认图，可以使用tf.get_default_graph()来调用（显示这张默认纸）
  * 当你有多个线程就可以创造多个tf.Graph()，就是你可以有一个画图本，有很多张图纸，这时候就会有一个默认图的概念了。
* [【tensorflow】重置/清除计算图](https://blog.csdn.net/u014636245/article/details/84073239?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.edu_weight)
  * 当在搭建网络查看计算图时，如果重复运行程序会导致重定义报错。为了可以在同一个线程或者交互式环境中（ipython/jupyter）重复调试计算图，就需要使用这个函数来重置计算图。
  * `tf.reset_default_graph()`,这个函数需要在with tf.session()外部调用。
* [Do not use tf.reset_default_graph() to clear nested graphs](https://stackoverflow.com/questions/46893824/do-not-use-tf-reset-default-graph-to-clear-nested-graphs)
  * The error message will display when you call `tf.reset_default_graph()` in one of the following scenarios(在以下的三种情况中，调用该函数会报错):
    1. Inside a `with graph.as_default():` block;
    2. Inside a `with tf.Session():` block;
    3. Between creating a `tf.InteractiveSession` and calling `sess.close()`.
* []()

* [mumu0419/TensorFlow_profile](https://github.com/mumu0419/TensorFlow_profile)
