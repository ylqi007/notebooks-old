# [Loss and Loss Functions for Training Deep Learning Neural Networks](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/)
Neural networks are trained using stochastic gradient descent and require that you choose a loss function when designing and configuring your model.


## 1. Neural Network Learning as Optimization
A deep learning neural network learns to map a set of inputs to a set of outputs from training data.

A neural network model is trained using the stochastic gradient descent optimization algorithm and weights are updated using the backpropagation or error algorithm. The 'gradient' in gradient descent refers to an error gradient. The gradient descent algorithm seeks to change the weights so that the next evaluation reduces the error, meaning the optimization algorithm is navigating down the gradient (or slope) of error.    
[本质上，模型是通过**梯度下降**和**反向传播**进行weights的更新，weights的更新就是为了将model prediction的错误率降低。那么如何去定义和度量model的错误率呢？这就需要一个合适的loss function。]


## 2. What Is a Loss Function and Loss?
In the context of an optimization algorithm, the function used to evaluate a candidate solution (i.e. a set of weights) is referred to as the **objective function**. **We may seek to maximize or minimize the objective function**, meaning that we are searching for a candidate solution that has the highest or lowest score respectively. Typically, with neural networks, we seek to minimize the error. As such, the objective function is often referred to as a cost function or a loss function and the value calculated by the loss function is referred to as simply **"loss"**.

The cost of loss function has an important job in that it must faithfully distill (提取) all aspects of the model down into a single number in such a way that improvements in that number are a sign of a better model.
> "The cost function reduces all the various good and bad aspects of a possibly complex system down to a single number, a scalar value, which allows candidate solutions to be ranked and compared."  
--Page 155, Neural Smithing: Supervised Learning in Feedforward Artificial Neural Networks, 1999.   

[我们需要一个model去度量一个model的好坏，这个度量要能够代表model的好与坏的各个方面。]

In calculating the error of the model during the optimization process, a loss function must be choose.


## 3. Maximum Likelihood
We prefer a function where the space of candidate solutions maps onto a smooth (but high-dimensional) landscape that the optimization algorithm can reasonably navigate via iterative updates to the model weights.   
[我们更倾向一个function，它可以将candidate solutions的space map到一个平滑的、高纬度的space，以便optimization algorithm可以通过iteratively updates the model weights。]

* Maximum Likelihood Estimation, or MLE, is a framework for inference for **finding the best statistical estimates of parameters from historical training data**: exactly what we are trying to do with the neural network.

* Given input, the model is trying to make predictions that match the data distribution of the target variable. Under maximum likelihood, a loss function estimates how closely the distribution of predictions made by a model matches the distribution of target variables in the training data. [A loss function 用来评估 distribution of prediction 与 distribution of target variables 之间的接近程度。]

* Advantage: As the number of examples in the training dataset is increased, the estimates of the model parameters improves. This is called the property of **"consistency"**. [一致性，intuitively，data 越多越能反映真是的 distribution。As the number of training examples approaches infinity, the maximum likelihood estimates of a parameter converges to the true value of the parameter.]


## 4. Maximum Likelihood and Cross-Entropy
Under the framework maximum likelihood, the error between two probability distribution is measured using **cross-entropy**.

当对一个 classification 问题进行建模的时候，我们想要将 input variables 映射到一个 class label，我们可以将问题建模成一个 example 属于每个 class 的 probabilities。
In a binary classification, 预测 example 属于第一个 class 的probability；
In the case of multiple-class classification, 预测 example 属于每个 class 的 probability。

Under maximum likelihood estimation, we would seek a set of model weights that minimize **the difference** between the **model's prediction probability distribution** given the dataset and the **distribution of probabilities** in the training dataset. This is called the cross-entropy.

Technically, `cross-entropy` comes from the field of information theory and has the unit of `bits`. It is used to estimate the difference between an estimated and predicted probability distribution. [即**交叉熵**是两个distribution之间的difference。]

In the case of regression problems where a quantity is predicted, it is common to use the mean square error(MSE) loss function instead. [在 **regression problem** 中，如果要预测 **quantity**，通常是用 `MSE`] [为什么在中文的参考中，看到的是`MSE`用在线性分类问题。]

> A few basic functions are very commonly used. The **mean squared error** is popular for function approximation (regression) problems […] The **cross-entropy error function** is often used for classification problems when outputs are interpreted as probabilities of membership in an indicated class.
--— Page 155-156, Neural Smithing: Supervised Learning in Feedforward Artificial Neural Networks, 1999.   
[MSE: approximation(regression) problems;
Cross-entropy: probabilities distribution]

When using the framework of maximum likelihood estimation, we will implement a cross-entropy loss function, which often in practice means `a cross-entropy loss function` for **classification problems** and `a mean squared error loss function` for **regression problems**.

Almost universally, deep learning neural networks are trained under the framework of maximum likelihood using cross-entropy as the loss function.

The `maximum likelihood approach` was adopted almost universally not just because of theoretical framework, but primarily because of the results it produces. Specifically, neural networks for classification that use a sigmoid or softmax activation function in the output layer learn faster and more robutsly using a cross-entropy loss function. [**什么时候使用sigmoid，什么时候使用softmax，两者区别呢？**]


## 5. What Loss Function to Use?
Importantly, the choice of loss function is directly related to the activation function used in the output layer of neural network. These two design are connected. [**输出层的激活函数** 与 **loss函数** 是相关的。]

> The choice of cost function is tightly coupled with the choice of output unit. Most of the time, we simply use the cross-entropy between the data distribution and the model distribution. The choice of how to represent the output then determines the form of the cross-entropy function.
— Page 181, Deep Learning, 2016.

Review the best practice or default values for each problem type with regard to the output layer and loss function:

* `Regression Problem`: A problem where you **predict a real-value quantity**.
  * Output Layer Configuration: One node with a linear activation unit.
  * Loss Function: Mean Squared Error (MSE).
* `Binary Classification Problem`: A problem where you classify an example as belonging to one of two classes. The problem is framed as predicting the likelihood of an example belonging to class one.
  * Output Layer Configuration: One node with a sigmoid activation unit.
  * Loss Function: Cross-Entropy, also referred to as Logarithmic loss.
* `Multi-Class Classification Problem`: A problem where you classify an example as belonging to one of more than two classes. The problem is framed as predicting the likelihood of an example belongint to each class.
  * Output Layer Configuration: One node for each class using the softmax activation function.
  * Loss Function: Cross-Entropy, also referred to as Logarithmic loss.


## 6. How to Implement Loss Function
### [Mean Squared Error Loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html)
`Mean Squared Error loss`, or MSE for short, is calculated as the average of the squared differences between the predicted and actual values.

### [Cross-Entropy Loss (or Log Loss)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)
`Cross-entropy loss` is often simply referred to as “cross-entropy,” “logarithmic loss,” “logistic loss,” or “log loss” for short.

Each predicted probability is compared to the actual class output value (0 or 1) and a score is calculated that penalizes the probability based on the distance from the expected value. The penalty is logarithmic, oferring a small score for small difference(0.1 or 0.2) and enormourse score for a larg difference(0.9 or 1.0). [a score is calculated based on `predicted probability` and `actual class`]

Cross-entropy loss is minimized, where smaller values represent a better model than larger values. A model that predicts perfect probabilities has a cross entropy or log loss of 0.0.


## 7. Loss Functions and Reported Model Performance
Given a framework of maximum likelihood, we know that we want to use a cross-entropy or mean squared error loss function under stochastic gradient descent.
Nevertheless, we may or may not want to report the performance of the model using the loss function. [在 maximum likelihood 框架下，通常用 `stochastic gradient descent` 方法去训练模型，降低 `cross-entropy loss` or `mean square error loss`。**但是有时候，我们并需想用 `loss function` 去报告模型的性能。**]

For example, logarithmic loss is challenging to interpret, especially for non-machine learning practitioner stakeholders. The same can be said for the mean squared error. Instead, it may be more important to report the accuracy and root mean squared error for models used for classification and regression respectively. [比如 `logarithmic loss` 和 `mean square error` 是难以解释的。我的理解是难以通过这两种 `loss` 来度量目标，比如 `loss` 到什么程度才是好的，达到要求的？ 所以，对 classification problem 而言，`accuracy` 可能更重要；对于 regression problem，`root mean squared error` 可能更重要(`？`)。]

It may also be desirable to choose models based on these metrics instead of loss. This is an important consideration, as the model with the minimum loss may not be the model with best metric that is important to project stakeholders. [通常，我们更希望根据 `metrics` 选择模型，而不是简单的 `loss`。因为最小的 `loss`，并不一定有最好的 `metric` (度量)。]

A good division to consider is to use the loss to evaluate and diagnose how well the model is learning. This includes all of the considerations of the optimization process, such as overfitting, underfitting, and convergence. An alternate metric can then be chosen that has meaning to the project stakeholders to both evaluate model performance and perform model selection.
[一种好的区分方式是，用 `loss` 来 evaluate and diagnose 模型的好坏，包括优化的过程，比如过拟合、欠拟合和收敛性等。而用另一种度量去选择对 project 选择有明确意义的模型，包括 `evaluate model performance` 和 `perform model selection`。]

* `Loss`: Used to evaluate and diagnose model optimization only.
* `Metric`: Used to evaluate and choose models in the context of the project.
