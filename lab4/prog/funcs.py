from random import randint
import matplotlib.pyplot as plt
import copy
from time import process_time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from sklearn.feature_extraction.text import TfidfTransformer

MAX_CLUSTER_VAL = 100


def cluster_update(cluster, cluster_content, dim):
	k = len(cluster)
	for i in range(k): #по i кластерам
		for q in range(dim): #по q параметрам
			updated_parameter = 0
			for j in range(len(cluster_content[i])):
				updated_parameter += cluster_content[i][j][q]
			if len(cluster_content[i]) != 0:
				updated_parameter = updated_parameter / len(cluster_content[i])
			cluster[i][q] = updated_parameter
	return cluster

def summing(array, cluster):
    return (array-cluster)**2

def asinc_data_distribution(array, cluster, n, k, dim):
    cluster_content = [[] for i in range(k)]

    for i in range(n):
        min_distance = float('inf')
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(0,dim, 3):
                # pool = ThreadPoolExecutor(3)
                # res1 = pool.submit(summing(array[i][q], cluster[j][q]))
                # res2 = pool.submit(summing(array[i][q+1], cluster[j][q+1]))
                # res3 = pool.submit(summing(array[i][q+2], cluster[j][q+2]))
                # print(res1)

                # distance += res1.result() + res2.result() + res3.result()
                with ThreadPoolExecutor() as executor:
                    res = executor.map(summing(array[i][q], cluster[j][q] ))
                #
                # distance += (array[i][q] - cluster[j][q]) ** 2
                    for num in res:
                        distance += num
            distance = distance ** (1 / 2)
            if distance < min_distance:
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])

    return cluster_content



def data_distribution(array, cluster, n, k, dim):
    cluster_content = [[] for i in range(k)]

    for i in range(n):
        min_distance = float('inf')
        situable_cluster = -1
        for j in range(k):
            distance = 0
            for q in range(dim):
                # transformer = TfidfTransformer(smooth_idf=False)
                # tfidf = transformer.fit_transform(array)
                # print(tfidf)

                distance += (array[i][q] - cluster[j][q]) ** 2

            distance = distance ** (1 / 2)
            if distance < min_distance:
                min_distance = distance
                situable_cluster = j

        cluster_content[situable_cluster].append(array[i])

    return cluster_content

def asinc_clusterization(array, k, size):
    n = len(array)
    dim = len(array[0])
    cluster = [[0 for i in range(dim)] for q in range(k)]
    cluster_content = [[] for i in range(k)]
    start = process_time()
    for i in range(dim):
        for q in range(k):
            cluster[q][i] = randint(0, MAX_CLUSTER_VAL)
    cluster_content = asinc_data_distribution(array, cluster, n, k, dim)
    privious_cluster = copy.deepcopy(cluster)

    while 1:
        cluster = cluster_update(cluster, cluster_content, dim)
        cluster_content = data_distribution(array, cluster,n,k,dim)
        if cluster == privious_cluster:
            break
        privious_cluster = copy.deepcopy(cluster)
    result = process_time() - start
    visualisation_3d(cluster_content)

    # print("Async Completed in {:.6f} seconds".format(end_time - start_time))
    print("Размер исходного массива:{:.0f}      Время выполнения алгоритма кластеризации К-средних: {:.12f}".format(size, result))


def clusterization(array, k, size):
    n = len(array)
    dim = len(array[0])
    cluster = [[0 for i in range(dim)] for q in range(k)]
    cluster_content = [[] for i in range(k)]
    start = process_time()
    for i in range(dim):
        for q in range(k):
            cluster[q][i] = randint(0, MAX_CLUSTER_VAL)
    cluster_content = data_distribution(array, cluster, n, k, dim)
    privious_cluster = copy.deepcopy(cluster)

    while 1:
        cluster = cluster_update(cluster, cluster_content, dim)
        cluster_content = data_distribution(array, cluster,n,k,dim)
        if cluster == privious_cluster:
            break
        privious_cluster = copy.deepcopy(cluster)
    result = process_time() - start
    visualisation_3d(cluster_content)
    # print("Async Completed in {:.6f} seconds".format(end_time - start_time))
    print("Размер исходного массива:{:.0f}      Время выполнения алгоритма кластеризации К-средних: {:.12f}".format(size, result))


def visualisation_3d(cluster_content):
    ax = plt.axes(projection="3d")
    plt.xlabel("x")
    plt.ylabel("y")

    k = len(cluster_content)

    for i in range(k):
        x_coordinates = []
        y_coordinates = []
        z_coordinates = []
        for q in range(len(cluster_content[i])):
            x_coordinates.append(cluster_content[i][q][0])
            y_coordinates.append(cluster_content[i][q][1])
            z_coordinates.append(cluster_content[i][q][2])
        ax.scatter(x_coordinates, y_coordinates, z_coordinates)
    plt.show()

def visualisation_2d(cluster_content):

	k = len(cluster_content)
	plt.grid()
	plt.xlabel("x")
	plt.ylabel("y")

	for i in range(k):
		x_coordinates = []
		y_coordinates = []
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
		plt.scatter(x_coordinates, y_coordinates)
	plt.show()


def standart():
    size = int(input("Введите размер массива: "))
    a = random_arr(size)
    # b = [['кот','свинья','петух'],['кот','свинья','петух'],['кот','свинья','петух'],['кот','свинья','петух'],['кот','свинья','петух'],['кот','свинья','петух']]
    k = int(input("Введите количество кластеров: "))
    clusterization(a, k, size)



def random_arr(size):
    arr = []
    for i in range (size):
        point = []
        point.append(randint(0, MAX_CLUSTER_VAL))
        point.append(randint(0, MAX_CLUSTER_VAL))
        point.append(randint(0, MAX_CLUSTER_VAL))
        arr.append(point)
    return arr




def comprasion():
    print("Выберите типа алгоритма кластеризации:\n" + \
          "  1 - последовательный;\n" + \
          "  2 - параллельный.")
    num = int(input("Выбор: "))

    k = int(input("Введите количество кластеров: "))
    size1 = 100
    size2 = 200
    size3 = 300
    size4 = 400
    size5 = 500

    if (num == 1):
        a = random_arr(size1)
        clusterization(a, k, size1)
        b = random_arr(size2)
        clusterization(b, k, size2)
        c = random_arr(size3)
        clusterization(c, k, size3)
        d = random_arr(size4)
        clusterization(d, k, size4)
        e = random_arr(size5)
        clusterization(e, k, size5)
    if (num == 2):
        a = random_arr(size1)
        asinc_clusterization(a, k, size1)
        b = random_arr(size2)
        asinc_clusterization(b, k, size2)
        c = random_arr(size3)
        asinc_clusterization(c, k, size3)
        d = random_arr(size4)
        asinc_clusterization(d, k, size4)
        e = random_arr(size5)
        asinc_clusterization(e, k, size5)

def asinchron():
    # a = [[25, 45, 89], [30, 78, 40], [90, 80, 45], [73, 77, 39], [3, 25, 15], [73, 62, 99], [63, 44, 50], [93, 20, 66]]
    # size = 8
    size = int(input("Введите размер массива: "))
    a = random_arr(size)
    k = 5
    asinc_clusterization(a, k, size)
