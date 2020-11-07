[TOC]

## Variables: Creation, Initialization, Saving, and Loading
When you train a model, you use `variables` to hold and update parameters. Variables are in-memory 
buffers containing tensors. They must be explicitly initialized and can be saved to disk during 
and after training. You can later restore saved values to exercise or analyse the model.        
训练模型时，可以使用变量来保存和更新参数。 变量是包含张量的内存缓冲区。 必须对它们进行显式初始化，并且可以在培
训期间和之后将其保存到磁盘。 您以后可以恢复保存的值以执行或分析模型。

### Creation
When you create a `Variable` you pass a `Tensor` as its initial value to the `Variable()` 
constructor. TensorFlow 提供了一系列操作生成 tensors 用于初始化操作 [constant or random values](https://chromium.googlesource.com/external/github.com/tensorflow/tensorflow/+/r0.7/tensorflow/g3doc/api_docs/python/constant_op.md)
Note that all these ops required you to specify the shape of the tensors. That shape automatically 
becomes the shape of the variable. Variables generally have a fixed shape, but TensorFlow provides 
advanced mechanisms to reshape variables.
```python
# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")
```
* 上述两个变量中用的到初始化变量函数 (`tf.random_normal()` and `tf.zeros()`) 都有固定的 shape。

Calling `tf.Variable()` adds several ops to the graph:
* A `variable` op that holds the variable value;
* An initializer op that sets the value to its initial value. This is actually a `tf.assign.op`.
* The ops for the initial value, such as the `zero` op for the `biases` variable in the example 
are also added to the graph.

The value returned by `tf.Variable()` value is an instance of the Python class `tf.Variable`.

### Initialization
**Variable initializers must be run explicitly before other ops in your model can be run.** The 
easiest way to do that is to add an op that runs all the variable initializers, and run that op 
before using the model.         
You can alternativley restore values from a checkpoint file.            
Use `tf.initialize_all_variables()` to add an op to run variable initializers. **Only run that op 
after you have fully constructed you model and launched it in a session.**
```python
# Create two variables.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([200]), name="biases")
...
# Add an op to initialize the variables.
init_op = tf.initialize_all_variables()

# Later, when launching the model
with tf.Session() as sess:
  # Run the init operation.
  sess.run(init_op)
  ...
  # Use the model
  ...
```

#### Initialization from another Variable
You sometimes need to initialize a variable from the initial value fo another variable. As the op 
added by `tf.initialize_all_variables()` initializes all variables in parallel you have to be 
careful when this is needed.        
当你需要对某个变量从另一个变量开始初始化的时候，需要注意。

To initialize a new variable from the value of another variable use other variable's 
`initialized_value()` property. You can use the initialized value directly as the initial value 
for the new variable, or you can use it as any other tensor to compute a value for the new variable.
```python
# Create a variable with a random value.
weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                      name="weights")
# Create another variable with the same value as 'weights'.
w2 = tf.Variable(weights.initialized_value(), name="w2")
# Create another variable with twice the value of 'weights'
w_twice = tf.Variable(weights.initialized_value() * 2.0, name="w_twice")
```

#### Custom Initialization
The convenience function `tf.initialize_all_variables()` adds on op to initialize **all variables** 
in the model. You can also pass it an explicit list of variables to initialize.

### Saving and Restoring
The easiest way to save and restore a model is to use a `tf.train.Saver` object. **The constructor 
adds `save` and `restore` ops to the graph for all, or a specified list, of the variables in the 
graph.** The saver object provides methods to run these ops, specifying paths for the checkpoint 
files to write to or read from.
 
#### Checkpoint Files
Variables are saved in binary files that, roughly, contain a map from variable names to tensor 
values.

When you create a `Saver` object, you can optionally choose names for the variables in the 
checkpoint files. By default, it uses the value of the Variable.name property for each variable.

#### Saving Variables
Create a Saver with tf.train.Saver() to manage all variables in the model.
```python
# Create some variables.
v1 = tf.Variable(..., name="v1")
v2 = tf.Variable(..., name="v2")
...
# Add an op to initialize the variables.
init_op = tf.initialize_all_variables()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, save the
# variables to disk.
with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.
  ..
  # Save the variables to disk.
  save_path = saver.save(sess, "/tmp/model.ckpt")
  print("Model saved in file: %s" % save_path)
```

#### Restoring Variables
The same `Saver` object is used to restore variables. Note that when you restore variables from 
a file you do not have to initialize them beforehand.
```python
# Create some variables.
v1 = tf.Variable(..., name="v1")
v2 = tf.Variable(..., name="v2")
...
# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, "/tmp/model.ckpt")
  print("Model restored.")
  # Do some work with the model
  ...
```

#### Choosing which Variables to Save and Restore
If you do not pass any argument to `tf.train.Saver(0` the saver handles all variables in the graph. 
Each one of them is saved under the name that was passed when the variable ware created.        

It is sometimes useful to explicitly specify names for variables in the checkpoint files. 
For example, you may have trained a model with a variable named "weights" whose value you want 
to restore in a new variable named "params".        
想将 "weights" 变量中的变量重新存到 "params" 中。

** It is also sometimes useful to only save or restore a subset of the variables used by a model.**
For example, you may have trained a neural net with 5 layers, and you now want to train a new 
model with 6 layers, restoring the parameters from the 5 layers of the previously trained model 
into the first 5 layers of the new model.       
只部分重新加载变量。

You can easily specify the names and variables to save by passing to the `tf.train.Saver()` 
constructor a Python dictionary: **keys are the names to use, values are the variables to manage.**

Notes:
* You can create as many saver objects as you want if you need to save and restore different 
subsets of the model variables. The same variable can be listed in multiple saver objects, 
its value is only changed when the saver `restore()` method is run.     
* If you only restore a subset of the model variables at the start of a session, you have to 
run an initialize op for the other variables. See `tf.initialize_variables()` for more information.
```python
# Create some variables.
v1 = tf.Variable(..., name="v1")
v2 = tf.Variable(..., name="v2")
...
# Add ops to save and restore only 'v2' using the name "my_v2"
saver = tf.train.Saver({"my_v2": v2})
# Use the saver object normally after that.
...
```

## References
* [Variables: Creation, Initialization, Saving, and Loading](https://chromium.googlesource.com/external/github.com/tensorflow/tensorflow/+/r0.7/tensorflow/g3doc/how_tos/variables/index.md)