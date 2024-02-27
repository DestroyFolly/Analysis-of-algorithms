from time import process_time
from matrix import standard_mult, winograd_mult, optimized_winograd_mult, random_matrix


def get_time_alg(alg, A, B):
    start = process_time()
    alg(A, B)
    result = process_time() - start

    return result


def time_test(size_type):
    algorithms = [standard_mult,
                  winograd_mult,
                  optimized_winograd_mult]
    results = [[], [], []]

    if size_type == 1:
        start = 11
        stop = 111
    else:
        start = 10
        stop = 110

    for alg in enumerate(algorithms):
        for n in range(start, stop, 10):
            result = 0
            A = random_matrix(n)
            B = random_matrix(n)

            for _ in range(10):
                result += get_time_alg(alg[1], A, B)

            results[alg[0]].append(result / 10)

    return results


def get_time():
    print("Выберите тип размера:\n" + \
          "  1 - нечетный;\n" + \
          "  2 - четный.")
    size_type = int(input("Выбор: "))

    results = time_test(size_type)

    return results, size_type


def print_time():
    results, size_type = get_time()
    msgs = ["нечетного",
            "четного"]

    print("\n\nРезультаты замеров времени для " + msgs[size_type - 1] + " размера:\n")

    i = 0

    if size_type == 1:
        start = 11
        stop = 111
    else:
        start = 10
        stop = 110

    for size in range(start, stop, 10):
        print(" %4d & %.4f & %.4f & %.4f \\\\ \n \\hline" % (size, \
                                                             results[1][i] * 1000, \
                                                             results[0][i] * 1000, \
                                                             results[2][i] * 1000))

        i += 1
