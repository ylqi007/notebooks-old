# [Custom training: basics](https://www.tensorflow.org/tutorials/customization/custom_training)
> TensorFlow also includes `tf.keras`—a high-level neural network API that provides useful abstractions to reduce boilerplate and makes TensorFlow easier to use without sacrificing flexibility and performance. 
> We strongly recommend the `tf.Keras` API for development


## 1. Variables
> TensorFlow has stateful operations built-in, and these are often easier than using low-level Python representations for your state. Use `tf.Variable` to represent weights in a model.          
> [TF 有一些内建的操作是有状态表示的。]
> A `tf.Variable` object stores a value and implicitly reads from this stored value. There are operations (`tf.assign_sub`, `tf.scatter_update`, etc.) that manipulate the value stored in a TensorFlow variable.         

## 2. Fit a linear model
> Let's use the concepts you have learned so far—`Tensor`, `Variable`, and `GradientTape`—to build and train a simple model. This typically involves a few steps:
> 1. Define the model.
> 2. Define a loss function.
> 3. Obtain training data.
> 4. Run through the training data and use an "optimizer" to adjust the variables to fit the data.

### 2.1 Define the model

### 2.2 Define a loss function

### 2.3 Obtain training data

### 2.4 Define a training loop
> With the network and training data, train the model using **gradient descent** to update the weights variable (`W`) and the bias variable (`b`) to reduce the loss. 
> There are many variants of the gradient descent scheme that are captured in `tf.train.Optimizer`—our recommended implementation. 
> But in the spirit of building from first principles, here you will implement the basic math yourself with the help of `tf.GradientTape` for automatic differentiation and tf.assign_sub for decrementing a value (which combines `tf.assign` and `tf.sub`).
>

## 3. Next Steps







