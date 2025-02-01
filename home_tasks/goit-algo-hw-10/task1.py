from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total_Production"

model += (2 * lemonade + fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

model.solve()

print(f"Оптимальна кількість Лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість Фруктового соку: {fruit_juice.varValue}")