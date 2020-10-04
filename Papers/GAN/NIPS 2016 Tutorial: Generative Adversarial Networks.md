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
> The basic idea of maximum likelihood is to define a model that provides an estimate of a probability distribution, parameterized by parameter $\theta$.
> The principle of maximum likelihood simply says to choose the parameters for the model that maximize the likelihood of the training data.
> We can also think of maximum likelihood estimation as minimizing the **KL divergence** between the data generating distribution and the model:
> $$\theta^{*}=\argmax_{\theta}D_{KL}(p_{data}(x) || p_{model}(x;\theta))$$

### 2.2 A taxonomy of deep generative models

### 2.3 Explicit density models

#### 2.3.1 Tractable explicit models
> **Fully visible belief networks** or FVBNs are models that use the chain rule of probability to decompose a probability distribution over an n-dimensional vector x into a product of one-dimensional probability distributions:
> * 根据 **the chain rule of probability**，将多维度的概率用单一维度表示。
> $$p_{model}(x) = \prod_{i=1}^{n}p_{model}(x_{i}|x_{1},...,x_{i-1})$$
>
> FVBNs are, as of this writing, one of the three most popular approaches to
generative modeling, alongside GANs and variational autoencoders.
> * Fully visible belief networks
> * GANs
> * Variational Autuencoders

> **Nonlinear independent components analysis** Another family of deep generative models with explicit density functions is based on defining continuous, nonlinear transformations between two different spaces.

#### 2.3.2 Explicit models requiring approximation
> Requiring the use of approximations to maximize the likelihood:
> * Those using deterministic approximations, which almost always means variaional methods
> * Those using stochastic approximations, meaning Markov chain Monte Carlo methods

> **Variational approximations** (变分近似) Variational methods define a lower bound
> $$\mathcal{L(x;\theta)} \leq \log p_{model}(x;\theta)$$
> A learning algorithm that maximizes $\mathcal{L}$ is guaranteed to obtain at least as high a value of the log-likelihood as it does of $\mathcal{L}$.
也就是说,*variaional approximations* 尝试去定义最大的下届。
> * VAE

> **Markov chain approximations**


### 2.4 Implicity density models
> Some models can be trained without even needing to explicitly define a density functions. These models instead offer a way to train the model while interacting only indirectly with pmodel , usually by sampling from it.
> 有些模型不需要明确的定义 density functions。通过 sampling


### 2.5 Comparing GANs to other generative models
> In summary, GANs were designed to avoid many disadvantages associated with
other generative models:
> * They can generate samples in parallel, instead of using runtime propor-
tional to the dimensionality of x. This is an advantage relative to FVBNs.
> * The design of the generator function has very few restrictions. This is
an advantage relative to Boltzmann machines, for which few probability
distributions admit tractable Markov chain sampling, and relative to non-
linear ICA, for which the generator must be invertible and the latent code
z must have the same dimension as the samples x.
> * No Markov chains are needed. This is an advantage relative to Boltzmann
machines and GSNs.
> * No variational bound is needed, and specific model families usable within
the GAN framework are already known to be universal approximators, so
GANs are already known to be asymptotically consistent. Some VAEs are
conjectured to be asymptotically consistent, but this is not yet proven.
> * GANs are subjectively regarded as producing better samples than other
methods.


## 3. How do GANs work?

### 3.1 The GAN framework
> The basic idea of GANs is to set up a game between two players.
> One is called the **generator**. The generator creates samples that are intended to come from the same distribution as the training data. [Generator 的目的是生成 samples，并且这些 samples 符合 training data 的分布。]
> The other is the **discriminator**. The discriminator examines samples to determine whether they are real or fake. [Discriminator 是对这些 samples 进行分类。]
> The generator is trained to fool the discriminator. [Generator 的目标是想方设法愚弄 Discriminator]

> Formally, GANs are a structured probabilistic model containing latent variables $z$ and observed variables $x$.
> It is a model where every latent variable influences every observed variable.

> The two players are represented by two functions, each of which is differentiable both with respect to its input and with respect to its parameters.
  [对输入和参数都是可微的。]
> * The discriminator is a function $D$ that takes $x$ as input and uses $\theta^{(D)}$ as parameters.
> * The generator is defined by a function $G$ that takes $z$ as input and uses $\theta^{(G)}$ as parameters.
>
> Both players have cost functions that are defined in terms of both players' parameters.
  [两个 player 都有相应的 cost function，并且 cost function 都是两个 players 参数的函数]
> The discriminator wishes to minimize $J^{(D)}(\theta^{(D)}, \theta^{(G)})$ and must do so while controlling only $\theta^{(D)}$.
> The generator wishes to minimize $J^{(G)}(\theta^{(D)}, \theta^{(G)})$ and must do so while controlling only $\theta^{(G)}$.
>
> Because each player's cost depends on the other player's parameters, this scenorio is most straightforward to describe as a game rather than as an optimization problem.
> * 也就是 cost function 对双方的 parameter 都有依赖，但是只能控制自己本身的参数。因此更像一个 Game，而不是一个 Optimization problem。

> **The solution to an optimization problem** is a (local) minimum, a point in parameter space where all neighboring points have greater or equal cost.
> **The solution to a game** is a Nash equilibrium. Here, we use the terminology of local differential Nash equilibria. In this context, a Nash equilibrium is a tuple $(\theta^{(D)}, \theta^{(G)})$, that is a local minimum of $J^{(D)}$ with respect to $\theta^{(D)}$ and a local minimum of $J^{(G)}$ with respect to $\theta^{G}$.
> * 也就是最终结果 $(\theta^{(D)}, \theta^{(G)})$ 分别是想对于 $\theta^{D}$ 和 $\theta^{D}$ 的 local minimum.

> **The training process**
![Training process](images/NIPS_2016_Tutorial_Training_Process.png)
* 训练过程包含同步的 SGD。
* On each step, two minibatches are sampled:  
  * a minibatch of $x$ values from the dataset
  * a minibatch of $z$ values from drawn from the model's prior over latent variables.
* 减小 $J^{(D)}$ 和 $J^{(D)}$ 是同时进行的。
* In both cases, it it possible to use the gradient-based optimization algorithm. Adam is usually a good choice.
* 有些人认为要对某个 player 多运行几步，但是作者认为最好的实践是同步的梯度下降, with one step for each player.

### 3.2 Cost functions

#### 3.2.1 The discriminator's cost, $J^{(D)}$
> The cost used for the discriminator is:
$$J^{(D)}(\theta^{D}, \theta^{G})=-\frac{1}{2} \mathbb E_{x \sim p_{data}} \log D(x) -\frac{1}{2} \mathbb E_{x \sim p_{data}} \log (1- D(G(z))) $$
> * This is just the standart cross-entropy cost that is minimized when training a start binary classifier with a sigmoid output.
>
> All versions of the GAN game encourage the discriminator to minimize the above equation.

#### 3.2.2 Minimax
> * The simplest version of the game is **zero-sum game**, in this version of the game:
> $$J^{(G)}=-J^{(D)}$$
>
> Zero-sum games are also called **minimax** games because their solution involves minimization in an outer loop and maximization in an inner loop:
> $$\theta^{(G)*}=\arg \min_{\theta ^{(D)}} \max_{\theta^{(G)}}V(\theta^{(D)}, \theta^{(G)})$$


#### 3.2.3 Heuristic, non-saturating game
> In the minimax game, the discriminator minimizes a cross-entropy, but the
generator maximizes the same cross-entropy.
> The cost for the generator then becomes:
> $$J^{(G)}=-\frac{1}{2}\mathbb E_{z} \log D(G(z))$$


#### 3.2.4 Maximum likelihood game
> We might like to be able to do maximum likelihood learning with GANs, which would mean minimizing the KL divergence between the data and the model
> * the data: 我觉的应该指的是 training data
> * the model: 我觉得应该是 generator 生成的 sample


#### 3.2.5 Is the choice of divergence a distinguishing feature of GANs?
> The KL divergence is not symmetric; minimizing $D_{DL}(p_{data}||p_{model})$ is different from minimizing $D_{DL}(p_{model}||p_{data})$. Maximum likehihood estimation performs the former; minimizing the Jensen-Shannon divergence is somewhat more similar to the latter.
>
> Some newer evidence suggests that the use of the Jensen-Shannon divergence does not explain why GANs make sharper samples:
> * It is now possible to train GANs using maximum likelihood, as describe in section 3.2.4.
> * GANs often choose to generate from very few modes; fewer than the limitation imposed by the model capacity. The reverse KL prefers to generate from as many modes of the data distribution as the model is able to; it does not prefer fewer modes in general. This suggests that the mode collapse is driven by a factor other than the choice of divergence.


#### 3.2.6 Comparison of cost functions
> The learning process differs somewhat from tranditional reinforcement learning because
> * The generator is able to observe not just the output of the reward function but also its gradients. [generator 既可以 observe reward function 的输出，也可以 observe its gradients]
> * The reward function is non-stationary; the reward is based on the discriminator which learns in response to changes in the generator's policy.


### 3.3 The DCGAN architecture
> DCGAN stands for "deep, convolution GAN"
> Prior to DCGANs, LAPGANs were the only version of GAN that had been able to scale to high resolution images.
> LAPGANs were the first GAN model to learn generate high resolution images in a gingle shot.


### 3.4 How do GANs relate to noise-constrastive estimation and maximum likelihood? (GAN与噪声对比估计和最大似然有何关系？)
![](images/NIPS_2016_GAN-NCE-MLE.png)


## 4. Tips and Tricks
To learn about tips and tricks not included in this tutorial, check out the GitHut repository associated with Soumith's talk: https://github.com/soumith/ganhacks

### 4.1 Train with labels

### 4.2 One-sided label smoothing

### 4.3 Virtual batch normalization

### 4.4 Can one balance G and D?


## 5. Research frontiers
### 5.1 Non-convergence

#### 5.1.1 Model collapse
> Mode collapse, also known as the Helvetica scenario, is a problem that occurs when the generator learns to map several different input z values to the same output point.

#### 5.1.2 Other games

### 5.2 Evaluation of generative models
> Another highly important research area related to GANs is that it is not clear how to quantitatively evaluate generative models.

### 5.3 Discrete outputs
> The only real requirement imposed on the design of the generator by the GAN framework is that the generator must be differentiable. Unfortunately, this means that the generator cannot produce discrete data, such as one-hot word or character representations.

### 5.4 Semi-supervised learning

### 5.5 Using the code

### 5.6 Developing connections to reinforcement learning


## 6. Plug and Play Generative Networks (即插即用的生成网络)


---
## 7. Exercises

### 7.1 The optimal discriminator strategy

### 7.2 Gradient descent for games

### 7.3 Maximum likelihood in the GAN framework


---
## 8. Solutions to Exercises

### 8.1 The optimal discriminator strategy

### 8.2 Gradient descent for games

### 8.3 Maximum likelihood in the GAN framework


---
## 9. Conclusion
