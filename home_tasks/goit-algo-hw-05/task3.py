import timeit
import pandas as pd
from pathlib import Path

def build_shift_table(pattern):
  """Створити таблицю зсувів для алгоритму Боєра-Мура."""
  table = {}
  length = len(pattern)
  # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
  for index, char in enumerate(pattern[:-1]):
    table[char] = length - index - 1
  # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
  table.setdefault(pattern[-1], length)
  return table

def boyer_moore_search(text, pattern):
  # Створюємо таблицю зсувів для патерну (підрядка)
  shift_table = build_shift_table(pattern)
  i = 0 # Ініціалізуємо початковий індекс для основного тексту

  # Проходимо по основному тексту, порівнюючи з підрядком
  while i <= len(text) - len(pattern):
    j = len(pattern) - 1 # Починаємо з кінця підрядка

    # Порівнюємо символи від кінця підрядка до його початку
    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1 # Зсуваємось до початку підрядка

    # Якщо весь підрядок збігається, повертаємо його позицію в тексті
    if j < 0:
      return i # Підрядок знайдено

    # Зсуваємо індекс i на основі таблиці зсувів
    # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  # Якщо підрядок не знайдено, повертаємо -1
  return -1

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

def test_search_algoritms():
    sizes = [10**3, 10**4, 10**5]
    results = []
    files = ["text1.txt", "text2.txt"]
    search_ex = { files[0]: ["алгоритми", "somenotexisttext"], files[1]: ["Параметри", "somenotexisttext"] }
    data = {}

    for f_name in files:
        txt = Path(f_name).read_text(encoding="utf-8")
        data[f_name] = txt

    for file in data:
        examples = search_ex[file]

        for ex in examples:
            # Boyer Moore search
            boyer_moore_search_time = timeit.timeit(lambda: boyer_moore_search(data[file], ex), number=1)

            # Knut Moris Prat search
            knut_moris_prat_search_time = timeit.timeit(lambda: kmp_search(data[file], ex),number=1)

            # Rabin Karp search
            rabin_karp_search_time = timeit.timeit(lambda: rabin_karp_search(data[file], ex), number=1)

            results.append((file, ex, boyer_moore_search_time, knut_moris_prat_search_time, rabin_karp_search_time))


    return results


def main():
    try:
        results = test_search_algoritms()

        columns = ["File", "Pattern", "Boyer Moore Time (s)", "Knut Morris Pratt Time (s)", "Rabin Karp Time (s)"]
        df = pd.DataFrame(results, columns=columns)

        # Displaying the DataFrame to the user
        print(df.to_string(index=False))

        # Analyzing fastest algorithm overall
        df_melted = df.melt(id_vars=["File", "Pattern"], var_name="Algorithm", value_name="Time (s)")
        fastest_overall = df_melted.groupby("Algorithm")["Time (s)"].mean().idxmin()

        print(f"\nFastest algorithm overall: {fastest_overall}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()