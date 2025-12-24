import numpy as np

def f(x):
    return x**2

def trapezoidal(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    result = h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1]))
    return result

a = 0
b = 1
exact = 1/3

print("Интеграл ∫x²dx от 0 до 1")
print(f"Точное значение: {exact:.10f}")
print("=" * 50)

for n in [5, 10, 20, 50, 100]:
    approx = trapezoidal(a, b, n)
    error = abs(approx - exact)
    print(f"n = {n:3d}: {approx:.10f}, ошибка = {error:.10f}")
