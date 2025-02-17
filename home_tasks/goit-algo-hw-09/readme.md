﻿# Оптимізація видачі решти: Жадібний алгоритм vs Динамічне програмування

## Опис завдання
Ця програма реалізує два алгоритми для визначення оптимального способу видачі решти покупцеві:

1. **Жадібний алгоритм (`find_coins_greedy`)** – вибирає найбільші доступні номінали монет, поки не буде досягнута задана сума.
2. **Алгоритм динамічного програмування (`find_min_coins`)** – шукає найменшу кількість монет, необхідних для формування заданої суми.

## Результати виконання

### Вихідні дані:
- Набір монет: `[50, 25, 10, 5, 2, 1]`
- Сума для видачі решти: `113`

### Отримані результати:

**Жадібний алгоритм (`find_coins_greedy`):**  
Результат: `{50: 2, 10: 1, 2: 1, 1: 1}`  
Час виконання: `4.4000043999403715e-06` секунд  

**Алгоритм динамічного програмування (`find_min_coins`):**  
Результат: `{50: 2, 10: 1, 2: 1, 1: 1}`  
Час виконання: `4.6000059228390455e-06` секунд  

## Висновки

- Обидва алгоритми повернули однаковий набір монет для суми `113`, що свідчить про їхню коректність для цього конкретного випадку.
- Жадібний алгоритм працює трохи швидше (`4.400e-06` с) порівняно з алгоритмом динамічного програмування (`4.600e-06` с). Це очікувано, оскільки жадібний підхід має меншу складність у порівнянні з динамічним програмуванням.
- Динамічне програмування є більш ефективним для випадків, коли набір монет ускладнений, наприклад, якщо номінали монет не дозволяють жадібному алгоритму знайти оптимальне рішення.

Таким чином, жадібний алгоритм є ефективнішим для стандартних наборів монет, але для складніших випадків (наприклад, з нестандартними номіналами) метод динамічного програмування може забезпечити кращі результати.