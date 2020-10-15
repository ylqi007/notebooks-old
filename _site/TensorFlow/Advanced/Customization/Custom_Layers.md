# [Custom Layers](https://www.tensorflow.org/tutorials/customization/custom_layers)
> We recommend using `tf.keras` as a high-level API for building neural networks. That said, most TensorFlow APIs are usable with eager execution.


## 1. Layers: Common sets of useful operations
> Most of the time when writing code for machine learning models you want to operate at a higher level of abstraction than individual operations and manipulation of individual variables.          
> [通常情况下，在机器学习和深度学习中，用到 higher level 的操作要更多，而不是单独的操作。]

> Many machine learning models are expressible as the composition and stacking of relatively simple layers, and TensorFlow provides both a set of many common layers as a well as easy ways for you to write your own application-specific layers either from scratch or as the composition of existing layers.         
> [很多机器学习模型可以表示为相对简单层的组合和堆积。]

> TensorFlow includes the full Keras API in the `tf.keras` package, and the Keras layers are very useful when building your own models.           
> [The full list of pre-existing layers](https://www.tensorflow.org/api_docs/python/tf/keras/layers)        
> Layers have many useful methods. For example, you can inspect all variables in a layer using `layer.variables` and trainable variables using `layer.trainable_variables`.
> In this case a fully-connected layer will have variables for weights and biases.          
> Add also `layer.kernel` and `layer.bias`


## 2. Implementing custom layers
> The best way to implement your own layer is extending the tf.keras.Layer class and implementing:
> 1. `__init__` , where you can do all input-independent initialization; [与 input 无关的初始化操作都在这里；如果在这里 create variables 的话，需要显式指定 variables 的shape。]
> 2. `build`, where you know the shapes of the input tensors and can do the rest of the initialization; [与 input shape 有关的初始化操作；]
> 3. `call`, where you do the forward computation; [前向操作]
> 
> Note that you don't have to wait until `build` is called to create your variables, you can also create them in `__init__`. 
> However, the advantage of creating them in `build` is that it enables late variable creation based on the shape of the inputs the layer will operate on. 
> On the other hand, creating variables in `__init__` would mean that shapes required to create the variables will need to be explicitly specified.


## 3. Models: Composing layers [组合各种层]
> Many interesting layer-like things in machine learning models are implemented by composing existing layers.       
> For example, each residual block in a resnet is a composition of `convolutions`, `batch normalizations`, and a `shortcut`.         
> Layers can be nested inside other layers.         
> [大多数模型都可以使用现有的层来组建，层也可以包含在其他的层中。]

> Typically you inherit from `keras.Model` when you need the model methods like: `Model.fit`, `Model.evaluate`, and `Model.save` (see [Custom Keras layers and models](https://www.tensorflow.org/guide/keras/custom_layers_and_models) for details).
> One other feature provided by `keras.Model` (instead of` keras.layers.Layer`) is that in addition to tracking variables, a `keras.Model` also tracks its internal layers, making them easier to inspect.

> Much of the time, however, models which compose many layers simply call one layer after the other. This can be done in very little code using `tf.keras.Sequential`.          
> [一层一层的创建。]




