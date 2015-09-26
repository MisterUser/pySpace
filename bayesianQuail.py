from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
# import random

locationx = 3
locationy = 5
location = [locationx, locationy]  # Where Quail is

figLoc = plt.figure(1)
plt.plot(location[0], location[1], 'ro')
plt.axis([0, 10, 0, 10])
x_randoms = [np.random.normal(locationx,2.0,None) for _ in range(100)]
y_randoms = [np.random.normal(locationy,2.0,None) for _ in range(100)]

noises = zip(x_randoms,y_randoms)
print(noises)
for x,y in noises:
    plt.plot(x, y, 'ko')

'''
fig = plt.figure(2)
ax = fig.gca(projection = '3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
plt.title('Location guess')

fig2 = plt.figure(3)
plt.subplot(211)
plt.title('2d Plot 1')
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
plt.plot(x1, y1, 'ko-')
plt.subplot(212)
plt.title('2d Plot 2')
t1 = np.arange(0.0, 5.0, 0.1)
plt.plot(t1, t1*2, 'b-.')

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
'''
plt.show()
