import math
import matplotlib.pyplot as plt


def method(alpha, T0, TL, f):
    dx = 0.1
    dt = 0.05
    #dx = 0.05
    #dt = 0.0125
    x_c = int((1 / dx)) + 1
    x_t = int((2 / dt)) + 1
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
    for i in range(len(t)):
        u[i][0] = T0
    for i in range(len(t)):
        u[i][-1] = TL
    for j in range(len(t) - 1):
        for i in range(1, len(x) - 1):
            u[j + 1][i] = u[j][i] + alpha * dt / dx**2 * (u[j][i + 1] - 2 * u[j][i] + u[j][i - 1]) + dt * f(x[i])
    return u, x, t, dt


def to4no(x, t, dt):
    u = [[0 for i in range(len(x))] for j in range(len(t))]
    for j in range(len(x)):
        u[0][j] = f(x[j])
    for j in range(len(t) - 1):
        for i in range(1, len(x) - 1):
            #1
            #u[j + 1][i] = math.exp(-0.1 * math.pi **2 * t[j]) * math.sin(math.pi*x[i])
            #2
            u[j + 1][i] = math.exp(-0.1 * math.pi ** 2 * t[j + 1]) * math.cos(math.pi*x[i])
            #3
            #u[j + 1][i] = math.exp(-0.1 * math.pi**2 / 2 * t[j + 1]) * math.sin(x[i]/2)
    for i in range(len(t)):
        u[i][0] = T0
    for i in range(len(t)):
        u[i][-1] = TL
    return u

alpha = 1
#alpha = 2
T0 = 0
TL = 0
def f(x):
    #1
    #return math.sin(math.pi * x)
    #2
    return math.cos(math.pi * x)
    #3
    #return math.sin(x / 2)
    ...


u, x, t, dt = method(alpha, T0, TL, f)
#to4noe = to4no(x, t, dt)
for i in range(len(t)):
    for j in range(len(x)):
        print(u[i][j], end=' ')
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