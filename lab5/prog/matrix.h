#ifndef MATRIX_H
#define MATRIX_H

#include <random>
#include <vector>
#include <iostream>
#include <fstream>
#include <queue>
#include <thread>
#include <math.h>
#include <string>
#include <experimental/random>

using namespace std;


typedef struct matrix
{
    std::vector<std::vector<int>> data;
    int size;
    int det;
} matrix_t;

// Funcs
matrix_t matrix_generate(size_t size);
void matrix_print(matrix_t matrix);
void matrix_dump(matrix_t matrix);
void matrix_WithoutRowAnColumn(matrix_t &matrix, int row, int col);
int matrix_determinant(matrix_t &matrix, int start, int end, int newDegree);
int matrix_determinant_parallel(matrix_t &matrix);
matrix_t matrix_copy(matrix_t matrix);
void matrix_dump(matrix_t matrix);

#endif