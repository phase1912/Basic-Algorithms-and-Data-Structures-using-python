def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    count_of_iterations = 0

    mid_value = None

    while low <= high:

        count_of_iterations += 1

        mid = (high + low) // 2

        if arr[mid] == x:
            mid_value = arr[mid]
            return count_of_iterations, mid_value
        elif arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1
            mid_value = arr[mid]

    if low < len(arr):
        mid_value = arr[low]

    return count_of_iterations, mid_value

def main():
    try:
        arr = [2.1, 3.4, 4.5, 4.6, 4.7, 10.1, 10.2, 10.3, 40.5]
        x = 10.3
        count_of_iterations, result = binary_search(arr, x)
        if result != -1:
            print(f"Count of iterations: {count_of_iterations}, fount element: {result}")
        else:
            print(f"Element not found, count of iterations: {count_of_iterations}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()