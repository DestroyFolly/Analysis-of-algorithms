from funcs import standart, asinchron, comprasion


import numpy as np

from concurrent.futures import ThreadPoolExecutor
from sklearn.feature_extraction.text import TfidfTransformer
#
# transformer = TfidfTransformer(smooth_idf=False)
# tfidf = transformer.fit_transform(X)
# print(tfidf.shape)






MSG = "\nМЕНЮ:\n" + \
          "  1 - Кластеризация алгоритмом К-средних;\n" + \
          "  2 - Распараллеленный алгоритм кластеризации;\n" + \
          "  3 - Сравнение по времени;\n" + \
          "  0 - Выход.\n" + \
          "Выбор: "

exit = 0
std = 1
asinc = 2
timec = 3



def main():
    command = -1

    while (command != exit):
            command = int(input(MSG))

            if command == std:
                standart()
            elif command == asinc:
                asinchron()
            elif command == timec:
                comprasion()
            else:
                print("\nПовторите ввод\n")


if __name__ == "__main__":
    main()

#
# #
# # loop = asyncio.get_event_loop()  # event loop
# # executor = ThreadPoolExecutor(max_workers=40)  # thread pool
# #
# #
# # def multi(A, B):
# #     if len(B) != len(A[0]):
# #         print("Different dimension of the matrics")
# #         return
# #
# #     n = len(A)
# #     m = len(A[0])
# #     t = len(B[0])
# #
# #     answer = [[0 for i in range(t)] for j in range(n)]
# #     for i in range(n):
# #         for j in range(m):
# #             for k in range(t):
# #                 answer[i][k] += A[i][j] * B[j][k]
# #     return answer
# #
# #
# # async def get_row(row, tmp):
# #     return [sum(starmap(mul, zip(row, column))) for column in tmp]
# #
# #
# # async def multi_async(A, B):
# #     tmp = tuple(zip(*B))
# #
# #     results = await asyncio.gather(*[get_row(row, tmp) for row in A])#выполнение задач одновременно
# #     return results
# #
# #
# # def random_matrix(n, m):
# #     return [[randint(0, 100) for i in range(m)] for j in range(n)]
# #
# #
# # def async_mtr(A, B):
# #     if len(B) != len(A[0]):
# #         print("Different dimension of the matrics")
# #         return
# #
# #     start_time = time.time()
# #     result = loop.run_until_complete(multi_async(A, B))
# #     end_time = time.time()
# #     print("Async Completed in {:.6f} seconds".format(end_time - start_time))
# #     return result
# #
# # def normal_mtr(A, B):
# #     if len(B) != len(A[0]):
# #         print("Different dimension of the matrics")
# #         return
# #     start_time = time.time()
# #     result = multi(A, B)
# #     end_time = time.time()
# #     print("Normal completed in {:.15f} seconds".format(end_time - start_time))
# #     return result
# #
# # def printMatrix(a):
# #     for i in range(0, len(a)):
# #         for j in range(0, len(a[i])):
# #             print(a[i][j], end = " ")
# #         print("\n")
# #
# #
# #
# # if __name__ == '__main__':
# #     A = random_matrix(100, 100)
# #     B = random_matrix(100, 100)
# #     # A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# #     # B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
# #     C1 = async_mtr(A, B)
# #     # printMatrix(C1)
# #     C2 = normal_mtr(A, B)
# #     # printMatrix(C2)
# #     print("Are the matrices equal: ", C1 == C2)