## [matplotlib](https://matplotlib.org/3.3.1/index.html)
### [Saving a figure after invoking pyplot.show() results in an empty file](https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file)
* The reason that `plt.savefig()` doesn't work after calling `plt.show()` is that the current figure
has been reset.
* `plotpy(plt)` keeps track of which figures, axes, etc are "current" (i.e. have not yet been displayed
with `plt.show()`) behind-the-scenes. `plt` 跟踪**还未展示的** figures，axes。
* `gcf` and `gca` **g**et the **c**urrent **f**igure and **c**urrent axes instances, respectively.
* `plt.savefig()` does `plt.gcf().savefig()`, in other words, get the current figure instance and call
its `savefig()` method.
* `plt.plot()` does `plt.gca().plot()`.
* After `show()` is called, the list of "current" figures and axes is empty. 在运行过 `show()` 之后，figures 
and axes 都会被 reset，因此都变成 empty。
* In general, you're better off directly using the **figure** and **axes** instances to plot/save/show/etc,
rather than using `plt.plot()`, etc, to implicitly get the current **figure/axes** and plot on it. 
直接使用 `figure` and `axes` instance 去做图/保存/展示等等，而不是通过 `plt.plot()` 隐含地拿到当前的 `figure/axes`
并在上面做图。
* Use `plt.subplots()` to generate a figure and an/more axes object(s), and then use the figure or axes
method directly, (e.g. `ax.plot(x, y)` instead of `plt.plot(x, y)` etc).
* The "recommended" way of doing things:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig('fig1.pdf')
plt.show()
fig.savefig('fig2.pdf')
```

### [matplotlib：先搞明白plt. /ax./ fig再画](https://zhuanlan.zhihu.com/p/93423829)
* `plt.***` 和 `ax.***` 的区别 
    * `plt.***` 系列
    * `fig, ax = plt.subplots()`
* 名词解释 in matplotlib            

| ![official doc](https://matplotlib.org/1.5.1/_images/fig_map.png) |
|:---:| 
| *Figure 1: Relation between fig and axes.* |
    1. Figure `fig = plt.figure()`: 可以解释为画布。
    2. Axes `ax = fig.add_subplot(1,1,1)`
        如果想要知道 axes 是什么东西，就需要先知道 axis 是什么。axis 指的就是 x 坐标轴，y 坐标轴等，代表的是一根坐标轴。
        而 axes 在英文里是 axis 的复数形式，也就是说，axes 代表的其实是 figure 当中的一套坐标轴。之所以说一套而不是两个坐标轴，
        是因为如果你画三维的图，axes 就代表 3 根坐标轴了。所以，在一个 figure 当中，每添加一次 subplot ，其实就是添加了一套坐标轴，
        也就是添加了一个 axes，放在二维坐标里就是你添加了两根坐标轴，分别是 x 轴和 y 轴。
        所以当你只画一个图的时候，http://plt.xxx 与 http://ax.xxx 其实都是作用在相同的图上的。
    3. Axis `ax.xaxis/ax.yaxis`: 对，这才是你的xy坐标轴。

* 图像的各个部位名称 (Parts of a Figure) 

| ![Parts of a Figure](https://matplotlib.org/_images/anatomy.png) |
|:---:| 
| *Figure 1: Relation between fig and axes.* |

### References:
#### API of `matplotlib`
* [matplotlib.pyplot](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)
* [matplotlib.pyplot.subplot](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)
* [matplotlib.pyplot.subplots](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots)
* [matplotlib.figure.Figure](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)
* [matplotlib.axes](https://matplotlib.org/3.3.1/api/axes_api.html#matplotlib.axes.Axes)
* [matplotlib.axes](https://matplotlib.org/3.3.1/api/axes_api.html#axis-labels-title-and-legend)
* [matplotlib.axes.Axes.barh](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh)
* [matplotlib.pyplot.rc](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc)
    * 将一些 attributes 包含在一个 group 中，集中设置，比如 `rc('lines', linewidth=2, color='r')` 集中设置 line 的宽度和颜色，
    而不用分开设置，比如 `rcParams['lines.linewidth'] = 2, rcParams['lines.color'] = 'r'`
* []()
* []()
* []()
* []()
* []()
* []()
* []()

#### Normal Problems and References
* [Saving a figure after invoking pyplot.show() results in an empty file](https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file)
* [Save plot to image file instead of displaying it using Matplotlib](https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib)
* [How do you change the size of figures drawn with matplotlib?](https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib)
* [* matplotlib：先搞明白plt. /ax./ fig再画](https://zhuanlan.zhihu.com/p/93423829)
* [50题matplotlib从入门到精通](https://www.kesci.com/home/project/5de9f0a0953ca8002c95d2a9)
* [matplotlib.pyplot的使用总结大全（入门加进阶）](https://zhuanlan.zhihu.com/p/139052035)
* [python如何使用Matplotlib画图（基础篇）](https://zhuanlan.zhihu.com/p/109245779)
* [Python-matplotlib画图(莫烦笔记)](https://zhuanlan.zhihu.com/p/33270402)
* [安利 5 个拍案叫绝的 Matplotlib 骚操作！](https://zhuanlan.zhihu.com/p/260516843)
* [matplotlib绘图：figure和axes有什么区别？](https://blog.csdn.net/qq_31347869/article/details/104794515)

## [seaborn](https://seaborn.pydata.org/index.html)
* [`xkcd` produces a set of 954 named colors, which you can now reference in seaborn using the xkcd_rgb dictionary](http://man.hubwiz.com/docset/Seaborn.docset/Contents/Resources/Documents/tutorial/color_palettes.html)
* [Adding value labels on a matplotlib bar chart](https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()


