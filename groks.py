import time
import random
from function import str_inverse


def sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_recursive(arr[1:])


def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    cur_max = find_max(arr[1:])
    return arr[0] if arr[0] > cur_max else cur_max


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        base_el = arr[0]
        less_base = [i for i in arr[1:] if i <= base_el]
        greater_base = [i for i in arr[1:] if i > base_el]
        return quick_sort(less_base) + [base_el] + quick_sort(greater_base)


def main():
    sum_arr = [random.randint(1, 200) for _ in range(99)]
    print(sum_recursive(sum_arr))
    print(find_max(sum_arr))
    tick = time.perf_counter()
    print(quick_sort(sum_arr))
    tock = time.perf_counter()
    print(f'Execution time: {tock-tick:0.8f} seconds')
    print(sum_arr)
    print(str_inverse(sum_arr))


main()
