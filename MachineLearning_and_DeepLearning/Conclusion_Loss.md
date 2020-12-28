[toc]

* [ ] 还未涉及更精细的 loss，更 advanced loss

## Introduction

DL 模型会尝试将训练数据集中的输入（比如图像，语音等）映射到特定的输出（比如图像中的物体，语音表示的文字等）。但是模型的参数众多，并且有太多的未知因素，因此无法直接计算模型的参数。故而，我们需要让模型自己需学习参数，使模型达到最好的效果。

> Typically, a neural network model is trained using the **stochastic gradient descent optimization** algorithm and weights are updated using the **backpropagation** of error algorithm.

训练网络的过程，实际上就是一个 optimization problem。



## What is loss functoin and loss?

> In the context of an optimizatoin algorithm, the function used to evaluate a candidate solution (i.e. a set of weights) is referred to as the objective function.
>
> We may seek to maximize or minimize the objective function, meaning that we are searching for a candidate solution that has the highest or lowest score respectively.
>
> Typically, with neural networks, we seek to minimize the error. As such, the objective function is often referred to as a cost function or a loss function and the value calculated by the loss function is referred to as simple "loss".

有多种函数可以评估 error of neural network。

> Under the framework maximum likelihood, the error between two probability distributions is measured using [cross-entropy](https://machinelearningmastery.com/cross-entropy-for-machine-learning/).

> Importantly, the choice of loss function is directly related to the activation function used in the output layer of your neural network. These two design elements are connected.
>
> Think of the configuration of the output layer as a choice about the framing of your prediction problem, and the choice of the loss function as the way to calculate the error for a given framing of your problem.

* **loss function 的选择**与 **output layer 的 activation function** 选择有关。
* Activation function of the output layer: 设计预测的模型
* Loss function: 计算给定模型的 error

### Regression Problem

> A problem where you predict a real-value quantity.
>
> * **Output Layer Configuration:** One node with a linear activation unit.
> * **Loss Function:** Mean Square Error (MSE)

### Binary Classification Problem

> A problem where you classify an example as belonging to one of two classes.
>
> The problem is framed as **predicting the likelihood of an example  belonging to class one**, e.g. the class that you assign the integer value 1, whereas the other class is assigned the value 0.
>
> - **Output Layer Configuration**: One node with a sigmoid activation unit.
> - **Loss Function**: Cross-Entropy, also referred to as Logarithmic loss.

### Multi-Class Classification Problem

> A problem where you classify an example as belonging to one of more than two classes.
>
> The problem is framed as predicting the likelihood of an example belonging to each class.
>
> - **Output Layer Configuration**: One node for each class using the softmax activation function.
> - **Loss Function**: Cross-Entropy, also referred to as Logarithmic loss.



## How to Implement Loss Functions?

### Mean Squared Error Loss (MSE)

> **Mean Squared Error loss**, or MSE for short, is calculated as **the  average** of the squared differences between **the predicted** and **actual  values**.
>
> The result is always positive regardless of the sign of the predicted and actual values and a perfect value is 0.0. The loss value is  minimized, although it can be used in a maximization optimization  process by making the score negative.

```python
# calculate mean squared error
def mean_squared_error(actual, predicted):
	sum_square_error = 0.0
	for i in range(len(actual)):
		sum_square_error += (actual[i] - predicted[i])**2.0		# sum of squared error
	mean_square_error = 1.0 / len(actual) * sum_square_error	# the average
	return mean_square_error
```

Scikit-learn [mean_squared_error() function](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)

Scikit-lean [3.3.4.4. Mean squared error](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error)

### Cross-Entropy Loss (or Log Loss)

> **Cross-entropy loss** is often simply referred to as “*cross-entropy*,” “*logarithmic loss*,” “*logistic loss*,” or “*log loss*” for short.
>
> **Each predicted probability** is compared to **the actual class output  value (0 or 1)** and **a score is calculated that penalizes the probability  based on the distance from the expected value.** The penalty is  logarithmic, offering a small score for small differences (0.1 or 0.2)  and enormous score for a large difference (0.9 or 1.0).
>
> Cross-entropy loss is minimized, **where smaller values represent a  better model than larger values.** A model that predicts perfect  probabilities has a cross entropy or log loss of 0.0.
>
> Cross-entropy for a binary or two class prediction problem is  actually calculated as the average cross entropy across all examples.

* Cross-entropy loss, cross-entropy, logarithmic loss, logistic loss, or los loss
* The predicted probability compared with the actual class output value (**0 or 1**). The **score** is calculated that penalizes the probability based on the distance from the expected value. **score** 用以计算预测的 probability 与 actual value 之间的差异。
* Cross-entropy loss: a smaller value represents a better model than larger values. 

```python
from math import log
# Binary class
# calculate binary cross entropy
def binary_cross_entropy(actual, predicted):
	sum_score = 0.0
	for i in range(len(actual)):
		sum_score += actual[i] * log(1e-15 + predicted[i])
	mean_sum_score = 1.0 / len(actual) * sum_score
	return -mean_sum_score
```

* Add a very small value (1e-15) to the predicted probabilities to avoid calculating the `log(0.0)`.



> Cross-entropy can be calculated for multiple-class classification. The  classes have been one hot encoded, meaning that there is a binary  feature for each class value and the predictions must have predicted  probabilities for each of the classes. The cross-entropy is then summed  across each binary feature and averaged across all examples in the  dataset.

* Cross-entropy can be used for multiple-class classification.
* The classes have been one-hot encoded.

```python
from math import log
# Multi-class 
# calculate categorical cross entropy
def categorical_cross_entropy(actual, predicted):
	sum_score = 0.0
	for i in range(len(actual)):
		for j in range(len(actual[i])):
			sum_score += actual[i][j] * log(1e-15 + predicted[i][j])
	mean_sum_score = 1.0 / len(actual) * sum_score
	return -mean_sum_score
```

* `actual[i]` is one-hot encoded class representation of sample i.

Scikit-learn [log_loss() function](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)

Scikt-learn [3.3.2.12. Log loss](https://scikit-learn.org/stable/modules/model_evaluation.html#log-loss)



## Reference

[Loss and Loss Functions for Training Deep Learning Neural Networks](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/)

