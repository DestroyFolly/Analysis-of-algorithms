from matrix import multiplicate, optimized_winograd_mult, standard_mult, winograd_mult
from graph import get_graph_result
from comparison import print_time




MSG = "\nМЕНЮ:\n" + \
          "  1 - Уумножение матриц с помощью стандартного алгоритма;\n" + \
          "  2 - Умножение матриц c помощью алгоритма Винограда;\n" + \
          "  3 - Умножение матриц с помощью оптимизированного алгоритма Винограда;\n" + \
          "  4 - Построение графиков;\n" + \
          "  5 - Замер времени;\n" + \
          "  0 - Выход.\n" + \
          "Выбор: "

exit = 0
std = 1
winograd = 2
optimized = 3
plot = 4
c_time = 5

def main():
    command = -1

    while (command != exit):
            command = int(input(MSG))

            if command == std:
                multiplicate(standard_mult)
            elif command == winograd:
                multiplicate(winograd_mult)
            elif command == optimized:
                multiplicate(optimized_winograd_mult)
            elif command == plot:
                get_graph_result()
            elif command == c_time:
                print_time()
            else:
                print("\nПовторите ввод\n")


if __name__ == "__main__":
    main()


