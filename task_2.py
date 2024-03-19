import numpy as np
import scipy.integrate as integrate

def f(x):
    """Функція, інтеграл якої обчислюється."""
    return x ** 3 + x ** 2

def monte_carlo_integrate(func, a, b, num_points=1000000):
    """Обчислення інтеграла методом Монте-Карло."""
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(min(func(x)), max(func(x)), num_points)
    under_curve = y < func(x)
    area = (b - a) * (max(func(x)) - min(func(x))) * np.mean(under_curve)
    return area

if __name__ == "__main__":
    a, b = -1, 1  # Межі інтегрування
    result, err = integrate.quad(f, a, b)  # Аналітичне обчислення інтегралу
    mc_result = monte_carlo_integrate(f, a, b)  # Метод Монте-Карло
    
    print(f"Результат функції quad: {result}, з похибкою {err}")
    print(f"Результат методу Монте-Карло: {mc_result}")
    print(f"Різниця між результатами: {abs(result - mc_result)}")
