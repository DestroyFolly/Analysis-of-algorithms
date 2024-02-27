from dataclasses import dataclass
from time import process_time

from sort import *
from arr import ARR, get_sorted_arr, get_reversed_arr, get_random_arr

@dataclass
class TimeTest:
    to_ms = 1000
    start_size = 100
    end_size = 1100
    step = 100
    iters = 500


def get_time_sort(sort, arr, size):
    start = process_time()
    sort(arr, size)
    result = process_time() - start

    return result


def time_test(arr_type):

    results = [[], [], []]
    sorts = [selection_sort, bucket_sort, bead_sort]

    for sort in enumerate(sorts):
        for size in range(TimeTest.start_size, TimeTest.end_size, TimeTest.step):
            result = 0

            for _ in range(TimeTest.iters):
                arr = arr_type(size)
                result += get_time_sort(sort[1], arr, size)

            results[sort[0]].append(result / TimeTest.iters)
    
    return results


def measure_time():

    arr_type = int(input(ARR.msg))

    if arr_type == ARR.sorted:
        results = time_test(get_sorted_arr)
    elif arr_type == ARR.reversed:
         results = time_test(get_reversed_arr) 
    elif arr_type == ARR.rand:
         results = time_test(get_random_arr)
    
    return results, arr_type

    
def print_time():

    results, arr_type = measure_time()

    if arr_type == ARR.sorted:
        msg = "отсортированного массива"
    elif arr_type == ARR.reversed:
        msg = "отсортированного в обратном порядке массива"
    elif arr_type == ARR.randomed:
        msg = "массива случайных чисел"

    print("\n\nРезультаты замеров времени для " + msg)

    i = 0

    for size in range(TimeTest.start_size, TimeTest.end_size, TimeTest.step):
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" %(size, \
            results[0][i] * TimeTest.to_ms, \
            results[1][i] * TimeTest.to_ms, \
            results[2][i] * TimeTest.to_ms))
        i += 1
