import heapq

def calculate_costs(heap):
    arr = []
    while bool(heap):
        val = heapq.heappop(heap)
        val2 = 0

        if len(arr) == 0:
            val2 = heapq.heappop(heap)
        else:
            val2 = arr[len(arr) - 1]

        sum = val + val2

        arr.append(sum)

    sum = 0

    for i in arr:
        sum += i

    return sum

def merge_k_lists(lists):
    l, *k = lists

    mlist = list(heapq.merge(l, *k))

    return mlist

def main():
    try:
        heap = [5, 6, 10, 15, 20, 11]

        heapq.heapify(heap)

        print(f"sum: {calculate_costs(heap)}")

        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        merged_list = merge_k_lists(lists)
        print("Відсортований список:", merged_list)


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()