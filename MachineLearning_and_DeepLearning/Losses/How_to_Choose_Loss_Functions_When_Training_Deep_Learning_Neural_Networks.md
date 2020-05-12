# [How to Choose Loss Functions When Training Deep Learning Neural Networks](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)

Neural network models learn a mapping from inputs to outputs from examples and the choice of loss function must match the framing of the specific predictive modeling problem, such as classification and regression.
Further, the configuration of the output layer must also be appropriate for the chosen loss function.
[`loss function` 的选择必须要与问题(是 classification 还是 regression)匹配。此外，configuration of output layer 也要与选择的 `loss` 函数匹配。]

## 1. Regression Loss functions
A regression predictive modeling problem involves predicting a real-valued quantity. 
[即 `A regression predictive model` 预测一个 `real-valued quantity`。]

Neural networks generally perform better when the real-valued input and output variables are to be scaled to a sensible range.

### 1.1 Mean Squared Error Loss
The `Mean Squared Error, or MSE`, loss is the default loss to use for regression problems. Mathematically, it is the preferred loss function under the inference framework of maximum likelihood if the distribution of the target variable is Gaussian. [`MSE` 是 regression problem 的默认 loss function。在 `maximum likelihood` 框架下，如果目标变量服从 `Gaussian` 分布，则 `MSE` 是 preferred loss。]

`Mean squared error` is calculated as the average of the squared differences between the predicted and actual values. The result is always positive regardless of the sign of the predicted and actual values and a perfect value is 0.0. The squaring means that larger mistakes result in more error than smaller mistakes, meaning that the model is punished for making larger mistakes.
[用 实际值-预测值，然后平方之后，求平均值的和。] 


### 1.2 Mean Squared Logarithmic Error Loss (L2 Loss, 均方误差)
There may be regression problems in which the target value has a spread of values and when predicting a large value, you may not want to punish a model as heavily as mean squared error.     
[可能存在回归问题，其中目标值具有分散的值，并且在预测大值时，您可能不希望像均方误差那样对模型进行严厉的惩罚。]

Instead, you can first calculate the natural logarithm of each of the predicted values, then calculate the mean squared error. This is called the Mean Squared Logarithmic Error loss, or MSLE for short.     
[相反，您可以首先计算每个预测值的自然对数，然后计算均方误差。 这称为均方对数误差损失，或简称为MSLE。]

It has the effect of relaxing the punishing effect of large differences in large predicted values.
As a loss measure, it may be more appropriate when the model is predicting unscaled quantities directly. Nevertheless, we can demonstrate this loss function using our simple regression problem.     
[它具有缓解较大预测值中较大差异的惩罚效果的作用。作为一种损失度量，当模型直接预测未缩放的数量时，它可能更合适。 但是，我们可以使用简单的回归问题来证明这种损失函数。]

### 1.3 Mean Absolute Error Loss (L1 Loss, 平均绝对误差)
On some regression problems, the distribution of the target variable may be mostly Gaussian, but may have outliers, e.g. large or small values far from the mean value.
The Mean Absolute Error, or MAE, loss is an appropriate loss function in this case as it is more robust to outliers. It is calculated as the average of the absolute difference between the actual and predicted values.    
[在某些回归问题上，目标变量的分布可能大部分是高斯分布，但可能有离群值，例如 远离平均值的大或小值。
在这种情况下，平均绝对误差或MAE损失是一种适当的损失函数，因为它对异常值更为稳健。 计算为实际值和预测值之间的绝对差的平均值。]
* 存在 outliers, e.g. large or small values far from the mean value.

### 1.4 总结
对于回归问题(regression problem)，通常预测的目标是一个实数值(real-valued quantity)。
对此可以有三种不同的`loss`：
1. `Mean Squared Error Loss`: 是 regression problem 的默认 loss 函数。
2. `Mean Squared Logarithmic Loss`： 当预测给出一个较大的值，但是并不像严厉惩罚的话，可以考虑先将预测值做对数处理，然后再求解 MSE。
3. `Mean Absolute Error Loss`： 对异常值更健壮(it is more robust to outliers)。

* 简而言之， 使用平方误差更容易求解，但使用绝对误差对离群点更加鲁棒。
* 和以MAE为损失的模型相比，以MSE为损失的模型会赋予更高的权重给离群点。
* L1损失对异常值更加稳健，但其导数并不连续，因此求解效率很低。L2损失对异常值敏感，但给出了更稳定的闭式解（closed form solution）（通过将其导数设置为0）
* 如果`L1`和`L2`都不能很好的满足需求呢？ ==> Huber Loss
* Since, the difference between `an incorrectly predicted target value` and `original target value` will be quite large and squaring it will make it even larger.
As a result, L1 loss function is more robust and is generally not affected by outliers.

[如何选择合适的损失函数，请看......](https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/80730722)        
[L1 vs. L2 Loss function](http://rishy.github.io/ml/2015/07/28/l1-vs-l2-loss/)

## 2. Binary Classification Loss Functions
Binary Classification are those predictive modeling problems where examples are assigned one of two labels.
The problem is often framed as predicting a value of 0 or 1 for the first or second class and is often implemented as predicting the probability of the example belonging to class value 1.

### 2.1 Binary Cross-Entropy
Cross-entropy is the default loss function to use for binary classification problems. It is intended for use with binary
classification where the target values are in the set {0, 1}.

Cross-entropy will calculate a score that summarizes **the average difference** between **the actual and predicted probability distribution** for predicting class 1. 
The score is minimized and a perfect cross-entropy value is 0.

| Binary Cross-Entropy Loss |
|:-------------------------:|
| ![Binary Cross-Entropy Loss](./images/Binary-Classification-Problem.png) |

The plot shows that the training process converged well. The plot for loss is smooth, given the continuous nature of the error between the probability distributions, whereas the line plot for accuracy shows bumps, given examples in the train and test set can ultimately only be predicted as correct or incorrect, providing less granular feedback on performance.
[上图显示训练过程可以很好的收敛。`loss` 的曲线是很 smooth 的，因为概率分布之间的错误率是连续性的；而 accuracy 曲线显示了一些波动，因为给定的例子是有限的、且只能被预测为正确或是不正确，从而提供较少的粒度，这也就体现在波动中。]

### 2.2 Hinge Loss
An alternative to cross-entropy for binary classification problems is the hinge loss function, primarily developed for use with **Support Vector Machine (SVM) models**.
It is intended for use with binary classification where the target values are in the set {-1, 1}.
[它适用于目标值位于集合{-1，1}中的二进制分类。]     
The hinge loss function encourages examples to have the correct sign, assigning more error when there is a difference in the sign between the actual and predicted class values.
[`Hinge Loss Function` 鼓励prediction 与 actual 有相同的 sign。]

### 2.3 Squared Hinge Loss
The hinge loss function has many extensions, often the subject of investigation with SVM models.
[`cross-entropy` 具有许多扩展，通常是使用 SVM 模型进行研究的主题。]

A popular extension is called the squared hinge loss that simply calculates the square of the score hinge loss. It has the effect of smoothing the surface of the error function and making it numerically easier to work with.
If using a hinge loss does result in better performance on a given binary classification problem, is likely that a squared hinge loss may be appropriate.
[如果 cross-entropy 在 binary-classification problem 中可以有较好的 performance，则 squared hinge loss 可能会合适。]


## 3. Multi-Class Classification Loss Functions
Multi-Class classification are those predictive modeling problems where examples are assigned one of more than two classes.
The problem is often framed as predicting an integer value, where each class is assigned a unique integer value from 0 to (num_classes – 1). The problem is often implemented as predicting the probability of the example belonging to each known class.
[模型会预测 integer value，每一个 class 是 [0,...,n-1] 之间的一个整数。 Problem 要建模成预测 example 属于每一个 class 的probabilities。]

### 3.1 Multi-Class Cross-Entropy Loss
Cross-entropy is the default loss function to use for multi-class classification problems.
In this case, it is intended for use with multi-class classification where the target values are in the set {0, 1, 3, …, n}, where each class is assigned a unique integer value.
Mathematically, it is the preferred loss function under the inference framework of maximum likelihood. It is the loss function to be evaluated first and only changed if you have a good reason.
Cross-entropy will calculate a score that summarizes the average difference between the actual and predicted probability distributions for all classes in the problem. The score is minimized and a perfect cross-entropy value is 0.

### 3.2 Sparse Multiclass Cross-Entropy Loss
A possible cause of frustration when using cross-entropy with classification problems with a large number of labels is the one hot encoding process.
For example, predicting words in a vocabulary may have tens or hundreds of thousands of categories, one for each label. This can mean that the target element of each training example may require a one hot encoded vector with tens or hundreds of thousands of zero values, requiring significant memory.
Sparse cross-entropy addresses this by performing the same cross-entropy calculation of error, without requiring that the target variable be one hot encoded prior to training.

### 3.3 Kullback Leibler Divergence Loss
Kullback Leibler Divergence, or KL Divergence for short, is a measure of how one probability distribution differs from a baseline distribution.
A KL divergence loss of 0 suggests the distributions are identical. In practice, the behavior of KL Divergence is very similar to cross-entropy. It calculates how much information is lost (in terms of bits) if the predicted probability distribution is used to approximate the desired target probability distribution.
As such, the KL divergence loss function is more commonly used when using models that learn to approximate a more complex function than simply multi-class classification, such as in the case of an autoencoder used for learning a dense feature representation under a model that must reconstruct the original input. In this case, KL divergence loss would be preferred. Nevertheless, it can be used for multi-class classification, in which case it is functionally equivalent to multi-class cross-entropy.








