The tutorial describes:
(1) Why generative modeling is a topic worth studying;
(2) how generative models work, and how GANs compare to other generative models;
(3) the details of how GANs work;
(4) research frontiers in GANs;
(5) state-of-the-art image models that combine GANs with other methods.
(6) Finally, the tutorial contains three exercises for readers to complete, and the solutions to these exercises.

In this tutorial, the term “generative model” refers to any model that takes a training set, consisting of samples drawn from a distribution pdata, and learns to represent an estimate of that distribution somehow. The result is a probability distribution P_model.
* In some cases, the model estimates P_model explicitly [有些模型会生成一个分布 distribution];
* In other cases, the model is only able to generate samples from pmodel [有些模型会生成样本 samples];
* Some models are able to do both.

**GANs focus primarily on sample generation**, though it is possible to design GANs that can do both. [GANs 主要集中的生成样本方面。]


## 1. Why study generative modeling?
1. Training and sampling from generative models is an excellent test of our ability to represent and manipulate high-dimensional probability distributions. [从生成模型的进行训练和采样是对表达和操纵高维概率分布能力的一次极好的检验。]
2. Generative models can be incorporated into reinforcement learning in several ways. [生成模型可以通过多种方式融入强化学习。]
3. Generative models can be trained with missing data and can provide predictions on inputs that are missing data. [生成模型可以用缺失数据进行训练，可以对缺失数据的输入进行预判。半监督学习是减少标签数量的一种策略。生成模型，尤其是GANs，能够很好地执行半监督学习。]
4. Generative models, and GANs in particular, enable machine learning to work with multi-modal outputs. [生成模型，特别是GANs，使机器学习能够处理多模态输出。一些传统的机器学习模型训练方法，如最小化期望输出和模型预测输出之间的均方误差，不能训练出能产生多个不同正确答案的模型。]
5. Finally, many tasks intrinsically require realitic generation of samples from some distribution. [最后，许多任务本质上都需要从某个分布中实际生成样本。]

Examples:
* Single image super-resolution: In this task, the goal is to take a low- resolution image and synthesize a high-resolution equivalent.
* Tasks where the goal is to create art.
* Image-to-image translation applications can convert aerial photos into maps or convert sketches to images.


## 2. How do generative models work? How do GANs compare to others?
### 2.1 Maximum likelihood estimation
