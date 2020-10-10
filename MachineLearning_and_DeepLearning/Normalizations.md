[TOC]

## Normalization (标准化)
* 标准化的方法有很多，还有归一化，规范化等，具体都可以在网上找到答案。

### Min-max normalization, 离差标准化
$x^{*} = \frac{x - min}{max - min}$

### Zero-mean normalization (z-score 标准化)
$x^{*} = \frac{x - \mu}{\sigma}$
* $\mu$ 是所有样本数据的**均值**;
* $\sigma$ 是所有样本的标准差。
* Z-score 用 python 实现的两种方法：
  1. `sklearn.preprocessing.scale()`
  2. `sklearn.preprocessing.StandardScaler`

### 总结：什么是 Normalization
* 统一映射到一个特定区间里，比如 [-1,1] or [0,1]
* 统一映射到某种特定分布里，比如均值为0、方差为1


## Reference
* [CNN 入门讲解：什么是标准化(Normalization)？](https://zhuanlan.zhihu.com/p/35597976)