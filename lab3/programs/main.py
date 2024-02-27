from dataclasses import dataclass

from arr import sort_arr
from sort import *
from graph_result import get_graph_result
from time_test import print_time

@dataclass
class Menu:
    """
        Константы необходимые в меню.
    """
    msg = "\n\nМЕНЮ:\n" + \
          "1. Сортировка выбором\n" + \
          "2. Блочная сортировка \n" + \
          "3. Cортировка бусинами\n" + \
          "4. Построить графики\n" + \
          "5. Замерить время\n" + \
          "0. Выход\n" + \
          "Выбор: "

    exit = 0
    selection = 1
    bucket = 2
    bead = 3
    plot = 4
    measure = 5


def process():

    process = True

    while process:
        command = int(input(Menu.msg))

        if command == Menu.selection:
            sort_arr(selection_sort)
        elif command == Menu.bucket:
            sort_arr(bucket_sort)
        elif command == Menu.bead:
            sort_arr(bead_sort)
        elif command == Menu.plot:
            get_graph_result()
        elif command == Menu.measure:
            print_time()
        else:
            process = False
            

if __name__ == "__main__":
    process()
