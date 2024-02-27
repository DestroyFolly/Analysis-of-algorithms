
#include <iostream>

#include "parallel.h"
#include "matrix.h"



void print_menu()
{
    printf("\n\n Вычисление детерминанта матрицы методом миноров\
        \n\t1. Линейная обработка \
        \n\t2. Параллельная обработка \
        \n\t3. Провести тестирование по времени \
      \n\n\t0. Выход\n\n");
}


int main(void)
{

    system("chcp 65001");
    int option = -1;

    while (option != 0)
    {
        print_menu();

        std::cout << "Выберите команду: ";
        std::cin >> option;

        if (option == 1)
        {
            int size = 0, count = 0;

            std::cout << "\n\nРазмер матрицы: ";
            std::cin >> size;

            std::cout << "Количество матриц: ";
            std::cin >> count;

            linear_execution(count, size, false);
        }
        else if (option == 2)
        {
            int size = 0, count = 0;

            std::cout << "\n\nРазмер матрицы: ";
            std::cin >> size;

            std::cout << "Количество матриц: ";
            std::cin >> count;

            parallel_execution(count, size, false);
        }
        else if (option == 3)
            time_measure();
        else
            printf("\nНеправильный номер команды\n");
    }
    return 0;
}

