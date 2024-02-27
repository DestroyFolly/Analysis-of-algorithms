from dataclasses import dataclass
from random import randint

@dataclass
class ARR:

    msg = "\n\nВыберете тип входного массива:\n" + \
          "1 - отсортированный\n" + \
          "2 - отсортированный в обратном порядке\n" + \
          "3 - случайный\n" + \
          "Выбор: "
    
    sorted = 1
    reversed = 2
    rand = 3



def input_arr():

    size = int(input("Введите размер массива: "))
    arr = []

    print("Введите элементы массива:")
    for i in range(size):
        arr.append(int(input()))

    return arr


def sort_arr(sort_type):

    arr = input_arr()
    arr = sort_type(arr, len(arr))
    
    print("\nОтсортированный массив:")
    print(arr)


def get_sorted_arr(size):
    arr = []

    for i in range(size):
        arr.append(i)
    
    return arr


def get_reversed_arr(size):
    arr = []

    for i in range(size):
        arr.append(size - i)

    return arr


def get_random_arr(size):
    arr = []
    for i in range(size):
        arr.append(randint(1, 2000))
    return arr
