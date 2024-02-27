#include "matrix.h"

char *LOG = "dump.txt";


matrix_t matrix_generate(size_t size)
{
    std::vector<std::vector<int>> tmp_data;
    tmp_data.resize(size);
    for (size_t i = 0; i < size; i++)
        tmp_data[i].resize(size);
    matrix_t matrix;
    matrix.size = size;
    matrix.data = tmp_data;
    matrix.det = 0;
    for (size_t i = 0; i < matrix.size; i++)
        for (size_t j = 0; j < matrix.size; j++)
            matrix.data[i][j] = std::experimental::randint(1, 10);
    return matrix;
}


matrix_t matrix_copy(matrix_t matrix)
{
    std::vector<std::vector<int>> tmp_data;
    int size = matrix.size;
    tmp_data.resize(size);
    for (size_t i = 0; i < size; i++)
        tmp_data[i].resize(size);
    matrix_t copy_m;
    copy_m.size = size;
    copy_m.data = tmp_data;
    copy_m.det = matrix.det;
    for (size_t i = 0; i < matrix.size; i++)
        for (size_t j = 0; j < matrix.size; j++)
            copy_m.data[i][j] = matrix.data[i][j];
    return copy_m;
}


void matrix_WithoutRowAnColumn(matrix_t &matrix, int row, int col)
{
    int offsetRow = 0;
    int offsetCol = 0;
    int size = matrix.size;
    std::vector<std::vector<int>> tmp_data;
    tmp_data.resize(size - 1);
    for (size_t i = 0; i < size - 1; i++)
        tmp_data[i].resize(size - 1);
    for(int i = 0; i < size-1; i++)
    {
        if(i == row)
            offsetRow = 1;
        offsetCol = 0;
        for(int j = 0; j < size-1; j++)
        {
            if(j == col)
                offsetCol = 1;
            tmp_data[i][j] = matrix.data[i + offsetRow][j + offsetCol];
        }

    }
    matrix.data = tmp_data;
    matrix.size = size - 1;
}


int matrix_determinant(matrix_t &matrix, int start, int end, int newDegree)
{
    int det = 0;
    int degree = newDegree;
    int size = matrix.size;
    if(size == 1)
        return matrix.data[0][0];
    else if(size == 2)
        return matrix.data[0][0]*matrix.data[1][1] - matrix.data[0][1]*matrix.data[1][0];
    else
    {
        for(int j = start; j < end; j++)
        {
            matrix_t copy = matrix_copy(matrix);
            matrix_WithoutRowAnColumn(copy, 0, j);
            det += degree * matrix.data[0][j] * matrix_determinant(copy, 0, copy.size, 1);;
            degree = -degree;
        }
    }
    return det;
}


void delegator(matrix_t matrix, int start, int end, int &det)
{
    int newDegree = 1;
    if (start % 2 == 1)
        newDegree *= -1;
    det = matrix_determinant(matrix, start, end, newDegree);
}


int matrix_determinant_parallel(matrix_t &matrix)
{
    std::thread threads[2];
    int det1 = 0;
    int det2 = 0;
    threads[0] = std::thread(delegator, matrix, 0, matrix.size / 2, std::ref(det1));
    threads[1] = std::thread(delegator, matrix, matrix.size / 2, matrix.size, std::ref(det2));

    for (int i = 0; i < 2; i++)
        threads[i].join();

    return det1 + det2;
}


void matrix_print(matrix_t matrix)
{
    std::cout << "Matrix print: \n";
    for (size_t i = 0; i < matrix.size; i++)
    {
        for (size_t j = 0; j < matrix.size; j++)
            std::cout << matrix.data[i][j] << " ";
        std::cout << "\n";
    }
}


void matrix_dump(matrix_t matrix)
{
    ofstream logf(LOG, ios::app);
    if (logf.is_open())
    {
        for (size_t i = 0; i < matrix.size; i++)
        {
            for (size_t j = 0; j < matrix.size; j++)
                logf << matrix.data[i][j] << " ";
            logf << "\n";
        }
        logf << "\n\nDet: " << matrix.det << "\n----------\n";
        logf.close();
    }
}
