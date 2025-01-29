class Item:
    def __init__(self, cost, calories, name=None):
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost
        self.name = name
    
    def __str__(self):
        return f"name: {self.name}, cost: {self.cost}, calories: {self.calories}"

def greedy_algorithm(items: list[Item], total_cost: int):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    choosed_items = []
    for item in items:
        if total_cost >= item.cost:
            total_cost -= item.cost
            total_calories += item.calories
            choosed_items.append(item)
    return (total_calories, total_cost, choosed_items)

def dynamic_programming(budget, items):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    total_cost = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]
            total_cost += costs[i - 1]
    rest_money = budget - total_cost
    
    return dp[n][budget], rest_money, selected_items

def main():
    budget = 110
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    print("greedy_algorithm")

    items_list = [Item(name=name, cost=details["cost"], calories=details["calories"]) for name, details in items.items()]

    total_calories, rest_money, chosen_items = greedy_algorithm(items_list, budget)

    print(f"Total calories: {total_calories}, rest money: {rest_money}")
    print("Items:")

    for item in chosen_items:
        print(item)

    print("dynamic_programming")

    max_calories, rest_money, chosen_items = dynamic_programming(budget, items)
    print(f"Total calories: {max_calories}")
    print(f"Rest money: {rest_money}")
    print(f"Selected items: {chosen_items}")


if __name__ == "__main__":
    main()