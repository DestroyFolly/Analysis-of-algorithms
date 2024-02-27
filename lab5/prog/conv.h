#ifndef CONVEYOR_H
#define CONVEYOR_H

#include <random>
#include <vector>
#include <iostream>
#include <queue>
#include <thread>
#include <chrono>
#include <ctime>
#include <mutex>

#include "matrix.h"


#define STEP_SIZE 100
#define STEP_COUNT 5


struct queues_s
{
    std::queue<int> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;
};

using queues_t = struct queues_s;


// Funcs

void linear_execution(int count, size_t size, bool is_print);
void parallel_execution(int count, size_t size, bool is_print);
void time_measure();

#endif