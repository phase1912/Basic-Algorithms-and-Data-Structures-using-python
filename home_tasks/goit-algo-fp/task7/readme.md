﻿## Результати
В ході симуляції було проведено 100 000 кидків.  
Нижче наведена таблиця порівняння ймовірностей (у відсотках):

| Сума | Ймовірність (Монте-Карло) | Аналітична ймовірність |
|------|--------------------------|------------------------|
| 2    | 2.80%                    | 2.78%                 |
| 3    | 5.51%                    | 5.56%                 |
| 4    | 8.32%                    | 8.33%                 |
| 5    | 11.22%                   | 11.11%                |
| 6    | 14.10%                   | 13.89%                |
| 7    | 16.48%                   | 16.67%                |
| 8    | 13.88%                   | 13.89%                |
| 9    | 11.17%                   | 11.11%                |
| 10   | 8.24%                    | 8.33%                 |
| 11   | 5.49%                    | 5.56%                 |
| 12   | 2.79%                    | 2.78%                 |

## Висновки
- Отримані за методом Монте-Карло результати дуже близькі до аналітичних значень.
- Відхилення мінімальні, що підтверджує точність методу при великій кількості ітерацій.
- Метод Монте-Карло є ефективним для оцінки ймовірностей складних подій, особливо у випадках, коли аналітичні обчислення є складними або неможливими.

## Візуалізація
Програма будує графік отриманих ймовірностей, що дозволяє наочно порівняти їх з аналітичними значеннями.