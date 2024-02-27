import matplotlib.pyplot as plt
from comparison import get_time


def get_graph_result():
    results, n = get_time()

    labels = ["Стандартный алгоритм",
              "Алгоритм Винограда",
              "Оптимизированный алгоритм\n \
               Винограда"]

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    k = [size for size in range(10, 110, 10)]
    plot.plot(k, results[0], label=labels[1])
    plot.plot(k, results[1], label=labels[0])
    plot.plot(k, results[2], label=labels[2])

    plt.legend()
    plt.grid()
    plt.title("Замеры времени")
    plt.ylabel("Затраченное время(c)")
    plt.xlabel("Размер")

    plt.show()

