import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = mp.loadtxt("data.dat")

x = data[:,0]
y = data[:,1]
z = data[:,2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs, c=c, marker=m)
plt.show()
