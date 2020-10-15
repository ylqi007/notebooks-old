## `np.mgrid` 用法
```python
np.mgrid[ 第1维，第2维 ，第3维 ， …] 
# dimention 1
a:b:c   # [a,b) with step = c
# dimention 2
a:b:cj  # [a,b] with c points
```
Example
```python
import numpy as np
a = np.mgrid[-2:5:2]
# array([-2,  0,  2,  4])
b = np.mgrid[-4:4:5j]
# array([-4., -2.,  0.,  2.,  4.])
```

[Python的 numpy中 meshgrid 和 mgrid 的区别和使用](https://www.cnblogs.com/shenxiaolin/p/8854197.html)        
[Ref1](https://www.cnblogs.com/wanghui-garcia/p/10763103.html)  

