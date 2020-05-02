import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 400
A = 300
R = np.sqrt(2 * (N / 2)**2)
area = np.zeros((N, N))

X = 0
Y = 100
bacteria = [[X, Y], [X, Y]]
V = 2


for i in range(N):
    for j in range(N):
        r1 = i - N / 2
        r2 = j - N / 2
        r = np.sqrt(r1**2 + r2**2)
        area[i, j] = A * (1 - r / R)

# Распределение 1

# for i in range(N):
#     for j in range(N):
#         area[i, j] = A * j / N



def time(dr, ro):
    if dr >= 0:
        ans = 3 * A / R * 1.1**(-dr / 3) / V**0.6 \
            * 4 * 1.1**(-ro/15) # Делаем бактерию поумней
    else:
        ans = (3 * A / R / V**0.6 - dr/10) \
            * 4 * 1.1**(-ro/15) # Делаем бактерию поумней

    return ans




fig = plt.figure()
plane = plt.matshow(area, fignum=0)
line, = plt.plot([], [], 'w')
dot, = plt.plot([], [], 'ro', markersize=3)
plt.axis('off')


def update(frame):
    old_ro = area[bacteria[-2][1], bacteria[-2][0]]
    delta_ro = area[bacteria[-1][1], bacteria[-1][0]] - old_ro
    t = time(delta_ro, area[bacteria[-1][1], bacteria[-1][0]])
    angle = random.random() * 2 * np.pi
    old_x = bacteria[-1][0]
    old_y = bacteria[-1][1]
    delta_x = int(V * t * np.sin(angle))
    delta_y = int(V * t * np.cos(angle))
    
    if (0 <= old_x + delta_x <= N - 1) and \
            (0 <= old_y + delta_y <= N - 1):
        bacteria.append([old_x + delta_x, old_y + delta_y])
    
    if (len(bacteria) > 10000):
        bacteria.pop(0)

    line.set_data([d[0] for d in bacteria], [d[1] for d in bacteria])
    dot.set_data(bacteria[-1][0], bacteria[-1][1])


ani = FuncAnimation(fig, update, interval=1)
plt.show()