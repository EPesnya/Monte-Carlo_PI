import random
import numpy as np
import matplotlib.pyplot as plt

L = 2       #расстояние между линиями
r = 5       #длина палочки
T = 590     #количество бросков

n_lines = 10
width = n_lines * L

lines = np.arange(L, (n_lines + 1) * L, L)
intersect = 0
pi = []


fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

for i in range(n_lines):
    ax1.plot([0, width], [lines[i], lines[i]], 'k', linewidth=1)

for i in range(T):
    x0 = r + random.random() * (width - 2 * r)
    y0 = r + random.random() * (L * (n_lines + 1) - 2 * r)
    angle = random.random() * 2 * np.pi
    x1 = x0 + r * np.cos(angle)
    y1 = y0 + r * np.sin(angle)

    ymin = min(y0, y1)
    ymax = max(y0, y1)

    if (ymin % L == 0):
        intersect += 1

    line = int(ymin // L)

    for j in range(n_lines - line):
        if (ymax >= lines[line + j]):
            intersect += 1
        else:
            break

    ax1.plot([x0, x1], [y0, y1])

    if (intersect != 0):
        pi.append([i, i * 2 * r / intersect / L])


ax1.axis('equal')

ax2.plot([0, T], [np.pi, np.pi], 'r')
ax2.plot([i[0] for i in pi], [i[1] for i in pi])
ax2.set_title(r'$\pi=$' + str(pi[-1][1]))

plt.suptitle('Алгоритм Бюффона для определения числа Пи')
plt.show()