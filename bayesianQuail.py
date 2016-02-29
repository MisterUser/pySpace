# from mpl_toolkits.mplot3d import axes3d
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gs
# import pudb; pu.db
locationx = 3
locationy = 5
location = [locationx, locationy]  # Where Quail is


# ---2D plot of Quail location along with chirps (noise) and guess from
# averaging
figLoc = plt.figure(1)
grid = gs.GridSpec(3, 1, height_ratios=[4, 1, 1])

plt.subplot(grid[0])
plt.plot(location[0], location[1], 'ro', label='Quail')
plt.axis([0, 7, 0, 10])
x_randoms = [np.random.normal(locationx, 1.0, None) for _ in range(100)]
y_randoms = [np.random.normal(locationy, 1.0, None) for _ in range(100)]

noises = list(zip(x_randoms, y_randoms))
# print('noises: {}'.format(noises))

noise_array = np.array(noises)
# print('noise arrays: {}'.format(noise_array))

x_noise_array, y_noise_array = noise_array.T
# print('x_noise_array: {}'.format(x_noise_array))

plt.plot(x_noise_array, y_noise_array, 'k.', label='Chirps')

simpleAvX = np.mean(x_randoms)
simpleAvY = np.mean(y_randoms)
plt.plot(simpleAvX, simpleAvY, 'go', label='Simple Average')
# ------------------


# -------two linear plots of x and y guesses around location

it_guess = noise_array[0]


# ---x
# fig2 = plt.figure(2)
# plt.subplot(312)
plt.subplot(grid[1])
plt.title('x movement')
plt.axis([0, 100, 0, 10])
plt.plot([0, 100], [locationx, locationx], 'r--')
plt.plot(1, it_guess[0], 'k.')

# ---y
# plt.subplot(313)
plt.subplot(grid[2])
plt.title('2d Plot 2')
plt.axis([0, 100, 0, 10])
plt.plot([0, 100], [locationy, locationy], 'b--')
plt.plot(1, it_guess[1], 'k.')

# ---now iterate over noise data
it_guess_old = it_guess
for n in range(2, 100):
    it_guess = (n-1)/n * it_guess_old + 1/n * noise_array[n-1]
    plt.subplot(grid[1])
    plt.plot(n, it_guess[0], 'k.')
    plt.subplot(grid[2])
    plt.plot(n, it_guess[1], 'k.')
    plt.subplot(grid[0])
    plt.plot(it_guess[0], it_guess[1], 'b+')
    it_guess_old = it_guess

plt.subplot(grid[0])
plt.plot(it_guess[0], it_guess[1], 'bo', label='Iterative Guess')
# ------------------------------------------------------------

# ------- Bayesian plot

likeLH_const = 1/(np.sqrt(np.power((2*np.pi), 2)*16))
invK = np.linalg.inv(np.matrix('4 0 ; 0 4'))
Sa = np.arange(2, 4.1, 0.1)
Sb = np.arange(4, 6.1, 0.1)
# Sa = np.array([2, 3, 4])
# Sb = np.array([4, 5, 6])

L = Sa.size
Pr = np.ones((L, L))
Pr = Pr/(np.sum(Pr))
Po = np.ones((L, L))
Po = Po/(np.sum(Po))

b_guess = noise_array[0]

'''
fig3d = plt.figure(2)
ax = fig3d.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                       cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
plt.title('Location guess')
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig3d.colorbar(surf, shrink=0.5, aspect=5)
'''

# xn is array with [x y]
for xn_array in noise_array[1:]:
    Pr = Po
    m = np.zeros((L, L))
    for i in range(L):
        for j in range(L):
            # print('observations xn_array[n]:')
            # print(xn_array)
            # print('xn as matrix')
            xn = np.matrix(xn_array)
            # print(xn)
            # print('xn.T')
            # print(xn.T)
            me = np.matrix([[Sa[i]], [Sb[j]]])
            # print('me')
            # print(me)
            xMinMe = (xn.T - me)[:, 0]
            # print('xMinMe')
            # print(xMinMe)
            # print('xMinMe.T')
            # print(xMinMe.T)
            # print('likeLH_const')
            # print(likeLH_const)
            m[i, j] = likeLH_const * np.exp(-(xMinMe).T * invK * (xMinMe) / 2)
            m[i, j] = m[i, j] * Pr[i, j]
            # print('m')
            # print(m)
    Po = m / np.sum(m)
    # print(Po)
    # print(np.argmax(Po))

    index_of_Max = np.argmax(Po)
    # print('biggest element of Po: {}'.format(index_of_Max))
    b_guess = [Sa[int(index_of_Max/L)], Sb[int(index_of_Max % L)]]
    # print(b_guess)
    plt.figure(1)
    plt.subplot(grid[0])
    plt.plot(b_guess[0], b_guess[1], 'm+')

plt.plot(b_guess[0], b_guess[1], 'mo', label='Bayes Estimate')
plt.legend()
plt.show()
