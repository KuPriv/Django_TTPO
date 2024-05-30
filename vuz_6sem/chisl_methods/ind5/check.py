import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
L = 1.0  # Длина стержня
T = 1.0  # Время моделирования
Nx = 100  # Количество узлов по пространству
Nt = 1000  # Количество узлов по времени
dx = L / Nx  # Шаг по пространству
dt = T / Nt  # Шаг по времени
alpha = 1.0  # Коэффициент температуропроводности

# Функция источника тепла
def f(x):
    return x**2 - x

# Явная схема
def explicit_scheme(f, Nx, Nt, dx, dt, alpha):
    u = np.zeros((Nt, Nx))
    x = np.linspace(0, L, Nx)

    # Граничные условия
    u[:, 0] = 0
    u[:, -1] = 0

    # Начальное условие
    u0 = np.zeros(Nx)
    u[0, :] = u0  # Можно изменить на другую функцию
    # Основной цикл
    for n in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            u[n + 1, i] = u[n, i] + alpha * dt / dx**2 * (
                u[n, i + 1] - 2 * u[n, i] + u[n, i - 1]
            ) + dt * f(x[i])
    return u

# Точное решение
def exact_solution(x):
    return -x**4 / 12 + x**3 / 6 - x / 12

# Вычисление численного решения
u_numerical = explicit_scheme(f, Nx, Nt, dx, dt, alpha)

# Вычисление точного решения
x_exact = np.linspace(0, L, Nx)
u_exact = exact_solution(x_exact)

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.plot(x_exact, u_numerical[-1, :], label="Численное решение")
plt.plot(x_exact, u_exact, label="Точное решение")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Уравнение теплопроводности")
plt.legend()
plt.grid(True)
plt.show()