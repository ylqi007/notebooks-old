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


### References:
* [matplotlib.pyplot](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)
* [matplotlib.pyplot.subplot](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)
* [matplotlib.pyplot.subplots](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots)
* [matplotlib.figure.Figure](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)
* [matplotlib.axes](https://matplotlib.org/3.3.1/api/axes_api.html#matplotlib.axes.Axes)
* [matplotlib.axes](https://matplotlib.org/3.3.1/api/axes_api.html#axis-labels-title-and-legend)
* 
* [Saving a figure after invoking pyplot.show() results in an empty file](https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file)


## 
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()


