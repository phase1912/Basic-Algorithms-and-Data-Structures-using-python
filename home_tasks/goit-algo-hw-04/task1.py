import random
import timeit
import pandas as pd
import ace_tools_open as tools

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def timsort(arr):
    return sorted(arr)

def test_sorting_algorithms():
    sizes = [10**3, 10**4, 10**5]
    results = []

    for size in sizes:
        arr = [random.randint(0, 10**6) for _ in range(size)]

        # Test Merge Sort
        merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)

        # Test Insertion Sort (only on smaller arrays due to its inefficiency)
        insertion_sort_time = "N/A" if size > 10 ** 4 else timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)

        # Test Timsort
        timsort_time = timeit.timeit(lambda: timsort(arr.copy()), number=1)

        results.append((size, merge_sort_time, insertion_sort_time, timsort_time))

    return results


def main():
    try:
        results = test_sorting_algorithms()

        columns = ["Array Size", "Merge Sort Time (s)", "Insertion Sort Time (s)", "Timsort Time (s)"]
        df = pd.DataFrame(results, columns=columns)
        tools.display_dataframe_to_user(name="Sorting Algorithm Performance Analysis", dataframe=df)

        print("Analysis complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()