import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000
in_circle = 0
pi = []

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.plot([0, 1, 1, 0, 0], [1, 1, 0, 0, 1])
x = np.linspace(0, 1, 100)
plt.plot(x, np.sqrt(1 - x**2))

for i in range(n):
    x0 = random.random()
    y0 = random.random()

    if (x0**2 + y0**2 <= 1):
        in_circle += 1
        plt.plot(x0, y0, 'ro', markersize=3)
    else:
        plt.plot(x0, y0, 'bo', markersize=3)

    pi.append(4 * in_circle / (i + 1))

plt.axis('equal')


plt.subplot(122)
plt.plot([0, n], [np.pi, np.pi], 'r')
plt.plot(np.arange(n) + 1, pi)
ax = plt.gca()
ax.set_title(r'$\pi=$' + str(pi[-1]))


plt.suptitle('Геометрический алгоритм Монте-Карло')
plt.show()