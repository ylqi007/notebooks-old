import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

k,b=np.mgrid[1:3:3j,4:6:3j]
f_kb=3*k**2+2*b+1

# k.shape=-1,1
# b.shape=-1,1
# f_kb.shape=-1,1 #统统转成9行1列
#
# fig=p.figure()
# ax=p3.Axes3D(fig)
# ax.scatter(k,b,f_kb,c='r')
# ax.set_xlabel('k')
# ax.set_ylabel('b')
# ax.set_zlabel('ErrorArray')
# p.show()

ax=plt.subplot(111,projection='3d')
ax.plot_surface(k,b,f_kb,rstride=1,cstride=1)
ax.set_xlabel('k')
ax.set_ylabel('b')
ax.set_zlabel('ErrorArray')
p.show()
