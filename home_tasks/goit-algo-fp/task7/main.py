import numpy as np
import matplotlib.pyplot as plt

N = 100000

dice1 = np.random.randint(1, 7, N)
dice2 = np.random.randint(1, 7, N)
sums = dice1 + dice2

unique, counts = np.unique(sums, return_counts=True)
probabilities = counts / N

analytical_probs = { 2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36 }

print("Сума | Ймовірність (Монте-Карло) | Аналітична ймовірність")
for s in range(2, 13):
    print(f" {s:2}  | {probabilities[s-2]:.4f}                   | {analytical_probs[s]:.4f}")

plt.bar(unique, probabilities, width=0.5, label="Монте-Карло", alpha=0.7)
plt.plot(list(analytical_probs.keys()), list(analytical_probs.values()), "ro-", label="Аналітичні")
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Ймовірність")
plt.xticks(range(2, 13))
plt.title("Ймовірність сум при киданні двох кубиків")
plt.legend()
plt.grid()
plt.show()