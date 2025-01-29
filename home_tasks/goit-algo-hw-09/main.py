import timeit

def find_coins_greedy(sum):
    coins = [50, 25, 10, 5, 2, 1]

    tmp_sum = sum
    result = {}

    for coin in coins:
        count_of_coins = 0

        while coin <= tmp_sum:
            count_of_coins += 1
            tmp_sum -= coin
            
        
        if count_of_coins > 0:
            result[coin] = count_of_coins

    return result

def find_min_coins(sum, coins, i, lookup = None):
    lookup = {} if lookup is None else lookup

    if sum <= 0:
        return lookup
    elif coins[i] > sum:
        return find_min_coins(sum, coins, i + 1, lookup)
    else:
        if coins[i] in lookup:
          lookup[coins[i]] = lookup[coins[i]] + 1
        else:
            lookup[coins[i]] = 1

        sum -= coins[i]

        return find_min_coins(sum, coins, i, lookup)


def main():
    try:
        print(find_coins_greedy(113))
        print(find_min_coins(113, [50, 25, 10, 5, 2, 1], 0))

        greedy_alg_time = timeit.timeit(lambda: find_coins_greedy(113), number=1)

        dinamic_alg_time = timeit.timeit(lambda: find_min_coins(113, [50, 25, 10, 5, 2, 1], 0), number=1)

        print(f"greedy alg time:{greedy_alg_time}, dinamic alg time: {dinamic_alg_time}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()