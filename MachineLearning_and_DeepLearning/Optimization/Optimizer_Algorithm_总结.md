在深度学习中，需要不停地迭代学习更新网络的参数，参数的更新过程是基于梯度的反向传播。但是关于又如何计算每层的参数的梯度，就有多种方法和算法。

## 0. 梯度下降的理解
首先要明确梯度下降的目标是优化模型？到底什么是所谓的优化模型？
* 模型是由一层一层的、相互递进的参数表示的。如果用`theta_i`表示第i层的参数，则有`f1=f1(theta_1, x)`, `f2=f2(theta_2, f1)`...。
即每一层的输出作为下一层的输入。
* 模型的好坏如何度量？如果模型越好，则其输出的结果越接近我们想要的，也就是越接近真实的结果，i.e. `prediction`与`truth`越接近。
* 那么又如何度量所谓的预测与真实的**接近程度**呢？这就是需要`loss function`来量化**接近程度**。如果`prediction`和`truth`大部分都是
匹配的，也就预测结果接近真实结果，`loss`就小；如果预测结果与真是结果相差很远，则`loss`就很大。

损失函数(`loss`)是每个样本损失函数的叠加求平均。那么影响`loss`的因素都有哪些呢？
* 训练集合中每个sample肯定会影响最终的`loss`，这是由dataset决定的，我们暂时不多考虑。
* 如果`loss`是批量sample的`loss`的叠加球平均，则`Batch`的大小和选择都会影响`loss`。

那么**梯度下降**又是干什么的呢？
* 既然模型有了，度量模型好坏的方式(loss)也有了。那么优化模型就是尽可能的减小`loss`。
* `loss`既然是一些参数(i.e. thetas)的函数，那么`loss`就可以表示为一个参数空间上的曲面，则相应的就存在极小值点，优化的目标就是找到能让
`loss`达到最小点的一系列参数`thetas`。
* 既然想让`loss`移动到最小值点，就要让`loss`沿着梯度、向着`loss`下降的方向移动，这就是所谓的梯度下降。

## 1. 基本的梯度下降算法
首先梯度下降的最常见三种基本算法是：BGD，SGD和MBGD。这三种的差别取决于用多少个sample来计算`loss`，然后用该`loss`去计算梯度并更新参数`thetas`。

### 1.1 Batch Gradient Descent(BGD)
BGD是基于整个dataset中的所有sample的loss叠加然后求平均表示最终的`loss`，也就是基于整个dataset来更新参数`thetas`。       

|  BGD update equation  |
|:---------------------:|
| ![1-1](./images/BGD_equation.png) |

缺点：
每一次的更新都要对整个dataset计算loss，然后计算梯度，则计算会非常缓慢；
遇到规模比较大的dataset，则会很慢；
不能添加新的sample，也就不能及时更新哦模型。

BGD对于凸函数可以收敛到全集极小值，对于非凸函数也可以收敛到局部极小值。

定义迭代次数`epoch`，即对整个dataset进行几次的全部计算，也就是更新几次`thetas`参数。

### 1.2 Stochastic Gradient Descent(SGD)
SGD是基于dataset中的每个sample的loss进行参数更新，也就是整体数据集是个循环，其中对每个样本进行一次参数更新。SGD每次只对一个sample进行计算，更新速度快；并且可以随时新增样本。

|  SGD update equation  |
|:---------------------:|
| ![1-1](./images/SGD_equation.png) |

冗余：对于很大的dataset而言，其中可能有相似、甚至一样的sample，那么相似的或一样的sample的loss就重复出现，也就是冗余。[有疑问？对于相同的dataset，SGD不也有吗？]

缺点：
SGD更新频繁，经常会有较严比较大的波动；
BGD 可以收敛到局部极小值，当然 SGD 的震荡可能会跳到更好的局部极小值处；
SGD相对与BGD而言，噪声会比较多，因为在BGD中少量的noise会被整体淹没掉，这就使得DGD每次的更新并不一定都朝向最优化的方向；
相比与BGD虽然训练速度快了，但是准确度会有所下降；
如果是非凸函数，则不一定能找到全局最优。

SGD虽然包含一定的随机性，但是从整体期望上来看，基本是正确的梯度，也就是整体上是朝正确方向下降的。

### 1.3 Mini-Batch Gradient Descent
SGD 和 BGD 是两个极端，SGD 每次是用一个sample，BGD 每次是用整个dataset。MBGD 则是介于两者之间，每次使用一小批量的samples，也就是n个样本进行计算。
每次更新都是基于n个samples，降低了噪声的影响，收敛更稳定；另一方面可以充分地利用深度学习库中高度优化的矩阵操作来进行更有效的梯度计算。

|  MBGD update equation  |
|:---------------------:|
| ![1-1](./images/MBGD_equation.png) |

每个batch中样本的个数n，是个超参数，一般取值在50～256。

缺点：
1. 不过 Mini-batch gradient descent 不能保证很好的收敛性，learning rate 如果选择的太小，收敛速度会很慢，如果太大，loss function 就会在极小值处不停地震荡甚至偏离。
对于非凸函数，还要避免陷于局部极小值处，或者鞍点处，因为鞍点周围的error是一样的，所有维度的梯度都接近于0，SGD 很容易被困在这里。
2. SGD对所有参数更新时应用同样的 learning rate，如果我们的数据是稀疏的，我们更希望对出现频率低的特征进行大一点的更新。LR会随着更新的次数逐渐变小。[???]

* 鞍点就是：一个光滑函数的鞍点邻域的曲线，曲面，或超曲面，都位于这点的切线的不同边。

## References
1. [深度学习——优化器算法Optimizer详解（BGD、SGD、MBGD、Momentum、NAG、Adagrad、Adadelta、RMSprop、Adam）](https://www.cnblogs.com/guoyaohua/p/8542554.html)
2. [Sebastian Ruder](https://arxiv.org/pdf/1609.04747.pdf)
3. [为什么数学概念中，将凸起的函数称为凹函数？](https://www.zhihu.com/question/20014186)