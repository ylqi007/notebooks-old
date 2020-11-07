# [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)

## 1. The Iris classification problem


## 2. Import and parse the training dataset
> Download the dataset file and convert it into a structure that can be used by this Python program.
> 1. Download the dataset
> 2. Inspect the data
> 3. Create a `tf.data.Dataset`

## 3. Select the type of model
> A **model** is a relationship between features and the label.
> 
> The activation function determines the output shape of each node in the layer. 
> These **non-linearities** are important—without them the model would be equivalent to a single layer. 
> There are many `tf.keras.activations`, but `ReLU` is common for hidden layers.
> 
> * [activation functions](https://developers.google.com/machine-learning/crash-course/glossary#activation_function)
> * [tf.keras.activations](https://www.tensorflow.org/api_docs/python/tf/keras/activations)


## 4. Train the model
> The Iris classification problem is an example of `supervised machine learning`: the model is trained from examples that contain labels. 
> In `unsupervised machine learning`, the examples don't contain labels. Instead, the model typically finds patterns among the features.

### 4.1 Define the loss and gradient function
> Both training and evaluation stages need to calculate the model's loss. This measures how off a model's predictions are from the desired label, in other words, how bad the model is performing. We want to minimize, or optimize, this value.

### 4.2 Training loop
> With all the pieces in place, the model is ready for training! A training loop feeds the dataset examples into the model to help it make better predictions. The following code block sets up these training steps:
> 1. Iterate each epoch. An epoch is one pass through the dataset.
> 2. Within an epoch, iterate over each example in the training Dataset grabbing its features (x) and label (y).
> 3. Using the example's features, make a prediction and compare it with the label. Measure the inaccuracy of the prediction and use that to calculate the model's loss and gradients.
> 4. Use an optimizer to update the model's variables.
> 5. Keep track of some stats for visualization.
> 6. Repeat for each epoch.
>
> The `num_epochs` variable is the number of times to loop over the dataset collection. Counter-intuitively, training a model longer does not guarantee a better model. 
> `num_epochs` is a **hyperparameter** that you can tune. Choosing the right number usually requires both experience and experimentation:

### 4.3 Visualize the loss function over time
> While it's helpful to print out the model's training progress, it's often more helpful to see this progress. 
> `TensorBoard` is a nice visualization tool that is packaged with TensorFlow, but we can create basic charts using the `matplotlib` module.

## 5. Evaluate the model's effectiveness

### 5.1 Setup the test dataset

### 5.2 Evaluate the model on the test dataset


## 6. Use the training model to make predictions
> We've trained a model and "proven" that it's good—but not perfect—at classifying Iris species. 
> Now let's use the trained model to make some predictions on **unlabeled examples**; that is, on examples that contain features but not a label.
>
### 6.1 Create an optimizer
> An optimizer applies the computed gradients to the model's variables to minimize the loss function. 
> You can think of the loss function as a curved surface and we want to find its lowest point by walking around.

## References:
1. [Framing: Key ML Terminology](https://developers.google.com/machine-learning/crash-course/framing/ml-terminology)











