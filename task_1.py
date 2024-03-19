from pulp import *

# Створюємо змінні для кількості "Лимонаду" (x) та "Фруктового соку" (y)
x = LpVariable("Lemonade", lowBound=0, cat='Integer')
y = LpVariable("Fruit Juice", lowBound=0, cat='Integer')

# Створюємо задачу максимізації
problem = LpProblem("Production Optimization", LpMaximize)

# Додаємо функцію максимізації (загальна кількість продуктів)
problem += x + y, "Total Product Quantity"

# Додаємо обмеження ресурсів
problem += 2 * x + y <= 100, "Water Constraint"
problem += x <= 50, "Sugar Constraint"
problem += x <= 30, "Lemon Juice Constraint"
problem += 2 * y <= 40, "Fruit Puree Constraint"

# Розв'язуємо задачу
problem.solve()

# Виводимо результати
print("Optimal Production Plan:")
print(f"Lemonade: {value(x)} units")
print(f"Fruit Juice: {value(y)} units")
print(f"Total Quantity: {value(problem.objective)} units")
