---
@翻译
---

[TOC]
## Sharing Variables (共享变量)
When building complex models you often need to share large sets of variables and you might wan to
initialize all of them in one place.            
当创建复杂的模型的时候，我们可能需要共享一大部分变量或者对一系列变量一次性赋值。

### The Problem
Imagine you create a simple model for image filters with only 2 convolutions. If you just use `tf
.Variable`, your model might look like this:
```python
def my_image_filter(input_images):
    conv1_weights = tf.Variable(tf.random_normal([5, 5, 32, 32]), name="conv1_weights")
    conv1_biases = tf.Variable(tf.zeros([32]), name="conv1_biases")
    conv1 = tf.nn.conv2d(input_images, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
    relu1 = tf.nn.relu(conv1 + conv1_biases)

    conv2_weights = tf.Variable(tf.random_normal([5, 5, 32, 32]), name="conv2_weights")
    conv2_biases = tf.Variable(tf.zeros([32]), name="conv2_biases")
    conv2 = tf.nn.conv2d(relu1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv2 + conv2_biases)
```
As you can easily imagine, models quickly get much more complicated than this one, and even here 
we already have different variables: `conv1_weights`, `conv1_biases`, `conv2_weights` and 
`conv2_biases`.         
如果以这种方式创建模型，模型会很快变得复杂。在此处，我们就需要四个变量：两个 weights，两个 biases。

The problem arises when you want to reuse this model. Assume you want to apply your image filter to 
2 different images, `image1` and `image2`. You want both images processed by the same filter with 
the same parameters. You can call `my_image_filter()` twice, but this will create two set of 
variables.          
当我们想重新使用这个模型的时候，会有问题出现。假设我们想把模型应用在两张不同的 images 上, `image1` and `image2`.
我们希望在这两张 images 上的 filter 使用相同的参数。如果我们在处理每张 image 的时候调用 `my_image_filter()`，
则会有两套参数生成。
```python
# First call creates one set of variables.
result1 = my_image_filter(image1)
# Another set is created in the second call.
result2 = my_image_filter(image2)
```

A common way to share variables is to create them in a separate piece of code and pass them to 
function that use them. For example, by using a dictionary:
```python
variables_dict = {
    "conv1_weights": tf.Variable(tf.random_normal([5, 5, 32, 32]),
        name="conv1_weights")
    "conv1_biases": tf.Variable(tf.zeros([32]), name="conv1_biases")
    ... etc. ...
}

def my_image_filter(input_images, variables_dict):
    conv1 = tf.nn.conv2d(input_images, variables_dict["conv1_weights"],
        strides=[1, 1, 1, 1], padding='SAME')
    relu1 = tf.nn.relu(conv1 + variables_dict["conv1_biases"])

    conv2 = tf.nn.conv2d(relu1, variables_dict["conv2_weights"],
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv2 + variables_dict["conv2_biases"])

# The 2 calls to my_image_filter() now use the same variables
result1 = my_image_filter(image1, variables_dict)
result2 = my_image_filter(image2, variables_dict)
```
* 这种方法在一个地方生成参数，并保存在 dict 中，这种生成操作只有一次。
* 两次调用 `my_image_filter()` 函数，都只是调用保存在 dict 中的参数，故而两次调用 `my_image_filter()` 使用
的是相同的参数。

While convenient, creating variables like above, outside of the code, breaks encapsulation:
* The code the builds the graph must document the names, types, and shapes of variables to create.
* When the code changes, the callers may have to create more, or less, or different variables.          
像上述方法，在 code 之外创建变量，尽管很方便，但是这样会破坏封装：
* 构建图的代码必须记录要创建的变量的名称，类型和形状。
* 当代码更改时，调用者可能必须创建更多或更少或不同的变量。

One way to address the problem is to use classes to create a model, where the classes take care of
managing the variables they need. For a lighter solution, not involving classes, TensorFlow provides
a `Variable Scope` mechanism that allows to easily share named variables while constructing a graph.
解决该问题的一种方法是使用类创建模型，其中类负责管理所需的变量。 对于不涉及类的更轻松的解决方案，TensorFlow 提供
了一种变量作用域机制，该机制允许在构建图形时轻松共享命名变量。

### Variable Scope Example
Variable Scope mechanism in TensorFlow consists of 2 main functions:
* `tf.get_variable(<name>, <shape>, <initializer>)`: Creates or returns a variable with a given
 name.
* `tf.variable_scope(<scope_name>)` : Manages namespaces for names passed to `tf.get_variable()`.

The function `tf.get_variable()` is used to get or create a variable instead of a direct call to 
`tf.Variable()`, as in `tf.Variable()`. An initializer is a function that takes the shape and
 provides a tensor with that shape.         
函数 `tf.get_variable（）`用于获取或创建变量，而不是直接调用 `tf.Variable`。 像 `tf.Variable`一样，
它使用初始化方法而不是直接传递值。 初始化器是采用形状并为该形状提供张量的函数。

Here are some initializers available in TensorFlow:
* `tf.constant_initializer(value)` initializes everything to the provided value,
* `tf.random_uniform_initializer(a, b)` initializes uniformly from [a, b],
* `tf.random_normal_initializer(mean, stddev)` initializes from the normal distribution with the
 given mean and standard deviation.
 
To see how `tf.get_variable()` solves the problem discussed before, let's refactor the code that
 created one convolution into a separate function, named `conv_relu`:
```python
def conv_relu(input, kernel_shape, bias_shape):
    # Create variable named "weights".
    weights = tf.get_variable("weights", kernel_shape,
        initializer=tf.random_normal_initializer())
    # Create variable named "biases".
    biases = tf.get_variable("biases", bias_shape,
        initializer=tf.constant_initializer(0.0))
    conv = tf.nn.conv2d(input, weights,
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv + biases)
```
This function uses short names `weights` and `biases`. We'd like to use for both `conv1` and
 `conv2`, but the variables need to have different names. This is where `tf.variable_scope
 ()` comes into play: it pushes a namespaces for variables.         
此函数使用短名称 `weights` 和 `biases`。 我们想同时使用 `conv1` 和 `conv2`，但是变量需要使用不同的名称。 
这就是 `tf.variable_scope()` 起作用的地方：它为变量添加名称空间。

```python
def my_image_filter(input_images):
    with tf.variable_scope("conv1"):
        # Variables created here will be named "conv1/weights", "conv1/biases".
        relu1 = conv_relu(input_images, [5, 5, 32, 32], [32])
    with tf.variable_scope("conv2"):
        # Variables created here will be named "conv2/weights", "conv2/biases".
        return conv_relu(relu1, [5, 5, 32, 32], [32])
```

Now, let's see what happens when we call `my_image_filter()` twice:
```python
result1 = my_image_filter(image1)
result2 = my_image_filter(image2)
# Raises ValueError(... conv1/weights already exists ...)
```
As you can see, `tf.get_variable()` checks that already existing variables are not shared by
 accident. If you want to share them, you need to specify it by setting `reuse_variables()` as
  follows:
```python
with tf.variable_scope("image_filters") as scope:
    result1 = my_image_filter(image1)
    scope.reuse_variables()
    result2 = my_image_filter(image2)
```
This is a good way to share variables, lightweight and safe.


### How Does Variable Scope Work?
#### Understanding `tf.get_variable()`
To understand variable scope it is necessary to first fully understand how `tf.get_variable
()` works. Here is how `tf.get_variable()` is usually called.           
要想明白 variable scope 如何工作，首先要明白 `tf.get_variable()` 是如何工作的。
```python
v = tf.get_variable(name, shape, dtype, initializer)
```
This call does one of two things depending on the scope it is called in. Here are the two options:

* **Case 1:** The scope is set for creating new variables, as evidenced by `tf.get_variable_scope
().reuse == False`. 
这种情况下，明确的设置 `tf.get_variable_scope().reuse = False`.
    
In this case, `v` will be a newly created `tf.Variable` with the provided shape and data type. 
The full name of the created variable will be set to `the current variable scope name` + `the 
provided name` and a check will be performed to ensure that no variable with this full name
exists yet. If a variable with the full name already exists, the function will raise a
`ValueError`. If a new variable is created, it will be initialized to the value `initializer
(shape)`.     
在这种情况下，`v` 是一个根据指定 shape 和 data type 的新创建的 `tf.Variable` 变量。The full name 就是提供的 
scope name + variable name。这个过程会检查是否已有变量使用这个名字，如果有的话，则会报错。
```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
assert v.name = "foo/v:0"
```

* **Case 2:** The scope is set for reusing variables, as evidenced by `tf.get_variable_scope
() == True`. 第二种情况就是 `tf.get_variable_scope() == True`。

In this case, the call full search for an already existing variable with name equal to `the 
current scope name` + `the provided name`. If no such variable exists, a `ValueError` will be raised. 
If the variable is found, it will be returned.          
在这种情况下，调用函数会全名搜索是否存在一个 current scope name + provided name 的变量。如果没有这个变量存在，
则会报错；如果有的话，则返回该变量。
```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v", [1])
assert v1 == v
```

#### Basics of `tf.variable_scope()`
Knowing how `tf.get_variable()` works makes it easy to understand variable scope. The primary 
function of variable scope is to carry a name that will be used as prefix for variable names and 
reuse-flag to distinguish the two cases described above. Nesting variable scopes appends their 
names in a way analogous to how directories work:       
知道了 `tf.get_variable()` 如何工作，理解 variable scope 就变得简单了。variable scope 的主要功能是提供
一个 name，作为变量名的前缀，和一个 reuse-flag 去区分上述的两种情况。
嵌套变量作用域以类似于目录工作方式的方式附加其名称：
```python
with tf.variable_scope("foo"):
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
assert v.name == "foo/bar/v:0"
```
The current variable scope can be retrieved using `tf.get_variable_scope()` and the `reuse` flag of 
the current variable scope can be set to `True` by calling `tf.get_variable_scope
().reuse_variable()`:           
如果想要获得当前 variable scope，可以使用 `tf.get_variable_scope()` 函数。
当前 variable scope 的 `reuse` flag 可以通过调用 `tf.get_variable_scope()` 函数设置为 `True`。
```python
with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1])
    tf.get_variable_scope().reuse_variables()   # reuse-flag == True
    v1 = tf.get_variable("v", [1])
assert v1 == v
```
Note that you **cannot** set the `reuse` flag to `False`. The reason behind this is to allow to 
compose functions that create models. Imagine you write a function `my_image_filter(inputs)` as 
before. Someone calling the function in a variable with `reuse = True` would expect all inner 
variable to be reused as well. Allowing to force `reuse = False` inside the function would break 
this contract and make it hard to share parameters in this way.         
需要注意的是，无法将 `reuse` flag 设置为 `False`。如果我们调用一个函数，并且设置 `reuse = True`，则会预期
在这个 scope 范围内的 variable 都将被 reuse。如果强制 `reuse = False`，则在函数内部会打破契约，使得这种方式
的共享参数变得复杂。

Even though you cannot set `reuse` to `False` explicitly, you can enter a reusing variable scope 
and then exit it, going back to a non-reusing one. This can be done using a `reuse = True` 
parameter when opening a variable scope. Note also that, for the same reason as above, the `reuse` 
parameter is inheriated. So when you oepn a reusing variable scope, all sub-scopes will be reusing
too.
```python
with tf.variable_scope("root"):
    # At start, the scope is not reusing.
    assert tf.get_variable_scope().reuse == False
    with tf.variable_scope("foo"):
        # Opened a sub-scope, still not reusing.
        assert tf.get_variable_scope().reuse == False
    with tf.variable_scope("foo", reuse=True):
        # Explicitly opened a reusing scope.
        assert tf.get_variable_scope().reuse == True
        with tf.variable_scope("bar"):
            # Now sub-scope inherits the reuse flag.
            assert tf.get_variable_scope().reuse == True
    # Exited the reusing scope, back to a non-reusing one.
    assert tf.get_variable_scope().reuse == False
```

#### Capturing variable scope
In all examples presented above, we shared parameters only because their names agreed, that is, 
because we opened a reusing variable scope with exactly the same string. In more complex cases, 
it might be useful to pass a `VariableScope` object rather than rely on getting the names right. 
To this end, variable scopes can be captured and used instead of names when opening a new variable 
scope.          
在上述的例子中，因为变量的名字相同，所以我们可以共享变量。在更复杂的情况下，我们可以传递一个 `VariableScope` 
变量，而不是通过名字相同共享变量。最后，variable scope 可以被捕获并代替 names 去打开一个新的 variable scope。
```python
with tf.variable_scope("foo") as foo_scope:
    v = tf.get_variable("v", [1])
with tf.variable_scope(foo_scope)
    w = tf.get_variable("w", [1])
with tf.variable_scope(foo_scope, reuse=True)
    v1 = tf.get_variable("v", [1])
    w1 = tf.get_variable("w", [1])
assert v1 == v
assert w1 == w
```

When opening a variable scope using a previously existing scope we jump out of the current variable 
scope prefix to an entirely different one. This is fully independent of where we do it.         
当用已经存在变量域打开一个新的变量域的时候，我们或跳出当前的变量域进入一个不同的变量域。这与我们在哪里调用它无关。
```python
with tf.variable_scope("foo") as foo_scope:
    assert foo_scope.name == "foo"
with tf.variable_scope("bar")
    with tf.variable_scope("baz") as other_scope:
        assert other_scope.name == "bar/baz"
        with tf.variable_scope(foo_scope) as foo_scope2:
            assert foo_scope2.name == "foo"  # Not changed.
``` 
* 在上面的例子中，`foo_scope2.name == "foo"` 而没有 `"bar/baz"` 的前缀。

#### Initializers in variable scope
Using `tf.get_variable()` allows to write functions that create or reuse variables and can be 
transparently called from outside. But what if we wanted to change the initializer of the created 
variables? Do we need to pass an extra argument to every function that creates variables? What 
about the most common case, when we want to set the default initializer for all variables in one 
place, on top of all functions? To help with these cases, variable scope can carry a default 
initializer. It is inherited by sub-scopes and passed to each `tf.get_variable(0` call. But it will 
be overridden if another is specified explicily.        
使用tf.get_variable（）允许编写创建或重用变量的函数，并且可以从外部透明地调用它们。 但是，如果我们想更改
所创建变量的初始化程序该怎么办？ 我们是否需要为每个创建变量的函数传递一个额外的参数？ 
在最常见的情况下，当我们要在所有功能之上的所有位置将所有变量的默认初始化程序设置为一个时，该怎么办？ 
为了帮助解决这些情况，变量作用域可以带有默认的初始化程序。 它由子作用域继承，并传递给每个 `tf.get_variable()`
调用。 但是，如果显式指定另一个初始化程序，它将被覆盖。
```python
with tf.variable_scope("foo", initializer=tf.constant_initializer(0.4)):
    v = tf.get_variable("v", [1])
    assert v.eval() == 0.4  # Default initializer as set above.
    w = tf.get_variable("w", [1], initializer=tf.constant_initializer(0.3)):
    assert w.eval() == 0.3  # Specific initializer overrides the default.
    with tf.variable_scope("bar"):
        v = tf.get_variable("v", [1])
        assert v.eval() == 0.4  # Inherited default initializer.
    with tf.variable_scope("baz", initializer=tf.constant_initializer(0.2)):
        v = tf.get_variable("v", [1])
        assert v.eval() == 0.2  # Changed default initializer.
```

### Names of ops in `tf.variable_scope()`
Name scopes can be opened in addition to a variable scope, and then they will only affect the names 
of the ops, but not of varialbes.           
除了**变量作用域**之外，还可以打开**名称作用域**，然后它们将仅影响操作的名称，而不影响变量的名称。
```python
with tf.variable_scope("foo"):
    with tf.name_scope("bar"):
        v = tf.get_variable("v", [1])
        x = 1.0 + v
assert v.name == "foo/v:0"
assert x.op.name == "foo/bar/add"
```
* 创建一个名称作用域(`bar`)，名称作用域不会响应变量名称，但是会影响变量操作的名称。

When opening a variable scope using a captured object instead of a string, we do not alter the 
current name scopes for ops.

### Examples of Use
Here are pointers to a few files that make use of variable scope. In particular, it is heavily used for recurrent neural networks and sequence-to-sequence models.

| File	| What's in it? |
|: --- :|: --- :|
| models/image/cifar10.py |	Model for detecting objects in images. |
| models/rnn/rnn_cell.py  | Cell functions for recurrent neural networks.   |
| models/rnn/seq2seq.py	  | Functions for building sequence-to-sequence models. |


## References
* [Sharing Variables](https://chromium.googlesource.com/external/github.com/tensorflow/tensorflow/+/r0.7/tensorflow/g3doc/how_tos/variable_scope/index.md)
