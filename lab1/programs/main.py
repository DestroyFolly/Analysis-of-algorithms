import matplotlib.pyplot as plt
import string
from time import process_time
from random import choice
from algorythms import damerau_levenstein_recursive, levenstein_cache_matrix, levenstein_matrix, levenstein_recursive

MSG = "\n      Меню \n 1) Рекурсивный алгоритм Левенштейна  \n 2) Алгоритм Левенштейна с использованием матрицы \n 3) Рекурсивный алгоритм Левенштейна с кешем \n 4) Рекурсивный алгоритм Дамерау-Левенштейна \n 5) Сравнение времени \n 0) Выход \n\n Введите номер пункта: "


def get_random_string(size):
    letters = string.ascii_letters
    result = "".join(choice(letters) for i in range(size))

    return result


def get_process_time(func, size):
    time_res = 0

    for i in range(100):
        str1 = get_random_string(size)
        str2 = get_random_string(size)

        time_start = process_time()
        func(str1, str2, output=False)
        time_end = process_time()

        time_res += (time_end - time_start)

    time_res /= 100
    return time_res


def graph(time_lev_rec, time_lev_cache, time_dam_lev_rec, time_lev_mat):
    sizes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig1 = plt.figure(figsize=(10, 10))
    plot1 = fig1.add_subplot()
    plot1.plot(sizes, time_lev_rec, label="Левенштейн (рекурсия)")
    plot1.plot(sizes, time_lev_cache, label="Левенштейн (рекурсия + кеш)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


    fig2 = plt.figure(figsize=(10, 10))
    plot2 = fig2.add_subplot()
    plot2.plot(sizes, time_lev_mat, label="Левенштейн (матричный)")
    plot2.plot(sizes, time_lev_cache, label="Левенштейн (кеш)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


    fig3 = plt.figure(figsize=(10, 10))
    plot3 = fig3.add_subplot()
    plot3.plot(sizes, time_lev_rec, label="Левенштейн (рекурсия)")
    plot3.plot(sizes, time_dam_lev_rec, label="Дамерау-Левенштейн (рекурсия)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина")

    plt.show()


def test_time_algos():
    time_lev_rec = []
    time_lev_mat = []
    time_lev_cache = []
    time_dam_lev_rec = []

    for num in range(10):
        time_lev_rec.append(get_process_time(levenstein_recursive, num))
        time_lev_mat.append(get_process_time(levenstein_matrix, num))
        time_lev_cache.append(get_process_time(levenstein_cache_matrix, num))
        time_dam_lev_rec.append(get_process_time(damerau_levenstein_recursive, num))

    print("\n\nЗамер времени для алгоритмов: \n")

    ind = 0

    for num in range(10):
        print(" %4d lev (rec) %.4f lev (matrix) %.4f lev (cache) %.4f dam-lev (rec) %.4f \\\\ \n \\hline" % (num, \
                                                                    time_lev_rec[ind] * 1000, \
                                                                    time_lev_mat[ind] * 1000, \
                                                                    time_lev_cache[ind] * 1000, \
                                                                    time_dam_lev_rec[ind] * 1000))

        ind += 1

    graph(time_lev_rec, time_lev_cache, time_dam_lev_rec, time_lev_mat)


def input_str():
    str1 = input("\nВведите 1-ую строку:\t")
    str2 = input("Введите 2-ую строку:\t")
    return str1, str2


def main():
    option = -1

    while (option != 0):
        option = int(input(MSG))

        if (option == 1):

            str1, str2 = input_str()
            print("\nРезультат: ", levenstein_recursive(str1, str2))

        elif (option == 2):

            str1, str2 = input_str()
            print("\nРезультат: ", levenstein_matrix(str1, str2))

        elif (option == 3):

            str1, str2 = input_str()
            print("\nРезультат: ", levenstein_cache_matrix(str1, str2))

        elif (option == 4):

            str1, str2 = input_str()
            print("\nРезультат: ", damerau_levenstein_recursive(str1, str2))

        elif (option == 5):

            test_time_algos()

        else:
            print("\nВведите номер пункта от 0 до 5\n")


if __name__ == "__main__":
    main()