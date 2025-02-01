import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2

# Метод Монте-Карло для обчислення інтегралу
N = 10000
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand < f(x_rand)
monte_carlo_result = (under_curve.sum() / N) * (b * f(b))

# Аналітичний розрахунок інтеграла
quad_result, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Метод quad: {quad_result} (похибка: {error})")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=1, alpha=0.5)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()