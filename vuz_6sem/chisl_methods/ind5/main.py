import math
import matplotlib.pyplot as plt


def method(alpha, T0, TL, ux):
    dx = 0.1
    dt = 0.05
    #dx = 0.05
    #dt = 0.0125
    x_c = int((1 / dx)) + 1
    # 1
    #x_t = int((2 / dt)) + 1
    # 2
    # x_t = int((1 / dt)) + 1
    # 3
    x_t = int((1 / dt) + 1)
    print(x_c, x_t)
    x = [0] * x_c
    t = [0] * x_t
    temp_x = 0
    temp_t = 0
    for i in range(len(x)):
        x[i] = temp_x
        temp_x += dx
    for i in range(len(t)):
        t[i] = temp_t
        temp_t += dt
    u = [[0 for i in range(len(x))] for j in range(len(t))]
    for i in range(len(x)):
        #1 2
        #u[0][i] = ux(x[i])
        # 3
        u[0][i] = ux(x[i])
    for i in range(len(t)):
        u[i][0] = T0
    for i in range(len(t)):
        u[i][-1] = TL
    for j in range(len(t) - 1):
        for i in range(1, len(x) - 1):
            #1 2
            #u[j + 1][i] = u[j][i] + alpha * dt / dx ** 2 * (u[j][i + 1] - 2 * u[j][i] + u[j][i - 1]) + dt * f(x[i])
            # 3
            u[j + 1][i] = u[j][i] + alpha * dt / dx**2 * (u[j][i + 1] - 2 * u[j][i] + u[j][i - 1]) + dt * f(x[i])
    return u, x, t, dx, dt


def to4no(x, t):
    u = [[0 for i in range(len(x))] for j in range(len(t))]
    for j in range(len(t)):
        for i in range(len(x)):
            # 1
            #u[j][i] = math.exp(-alpha * math.pi ** 2 * t[j]) * math.sin(math.pi * x[i])
            # 2
            # u[j][i] = math.exp(-alpha * math.pi ** 2 * t[j]) * math.cos(math.pi*x[i])
            # 3
            u[j][i] = -(x[i] ** 4) / 12 + (x[i] ** 3) / 6 - x[i] / 12
    for i in range(len(t)):
        u[i][0] = T0
    for i in range(len(t)):
        u[i][-1] = TL
    return u


# 1
#alpha = 0.1
#T0 = 0
#TL = 0
# 2
# alpha = 0.01
# T0 = 1
# TL = -1
# 3
alpha = 0.1
T0 = 0
TL = 0


def f(x):
    # 3
    return x ** 2 - x


def ux(x):
    # 1
    #return math.sin(math.pi * x)
    # 2
    # return math.cos(math.pi * x)
    # 3
    return x ** 2 - x
    ...


u, x, t, dx, dt = method(alpha, T0, TL, ux)
#to4noe = to4no(x, t)
for i in range(len(t)):
    for j in range(len(x)):
        print(u[i][j] * 0.1, end=' ')
        #print(to4noe[i][j], end=' ')
    print()
plt.figure(figsize=(10, 6))
for i in range(0, len(t)):
    #plt.plot(x, to4noe[i])
    plt.plot(x, u[i])
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.title("Решение уравнения теплопроводности")
plt.grid(True)
plt.show()
