#include "parallel.h"

double time_now = 0;
int q2_recevied = 0;
int q2_handled = 0;
int q3_recevied = 0;
int q3_handled = 0;

void linear_execution(int count, size_t size, bool is_print)
{
    time_now = 0;
    for (int i = 0; i < count; i++)
    {
        matrix_t matrix = matrix_generate(size);
        matrix.det = matrix_determinant(matrix, 0, matrix.size, 1);
        matrix_dump(matrix);
    }
}


void stage1_parallel(std::queue<int> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;

    std::mutex m;

    while(!q1.empty())
    {
        m.lock();
        int size = q1.front();
        m.unlock();
        std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
        double start_res_time = time_now, res_time = 0;
        time_start = std::chrono::system_clock::now();
        std::cout << fixed;
        matrix_t matrix = matrix_generate(size);
        time_end = std::chrono::system_clock::now();
        res_time = (std::chrono::duration_cast<std::chrono::nanoseconds> (time_end - time_start).count()) / 1e9;
        time_now = start_res_time + res_time;
        m.lock();
        q2.push(matrix);
        q1.pop();
        m.unlock();
    }
}


void stage2_parallel(std::queue<int> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;

    std::mutex m;

    while((!q2.empty() || !q1.empty()) && q2_handled <= q2_received)
        if (!q2.empty())
        {
            m.lock();
            matrix_t matrix = q2.front();
            m.unlock();
            std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
            double start_res_time = time_now, res_time = 0;
            time_start = std::chrono::system_clock::now();
            std::cout << fixed;
            matrix.det = matrix_determinant_parallel(matrix);
            time_end = std::chrono::system_clock::now();
            res_time = (std::chrono::duration_cast<std::chrono::nanoseconds> (time_end - time_start).count()) / 1e9;
            time_now = start_res_time + res_time;
            q3.push(matrix);
            q2.pop();
            q2_handled++;
            m.unlock();
        }
}


void stage3_parallel(std::queue<int> &q1, std::queue<matrix_t> &q2, std::queue<matrix_t> &q3, bool is_print)
{
    int task_num = 1;
    std::mutex m;
    while((!q3.empty() || !q2.empty() || !q1.empty()) && q3_handled <= q3_received)
        if (!q3.empty())
        {
            m.lock();
            matrix_t matrix = q3.front();
            m.unlock();
            std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
            double start_res_time = time_now, res_time = 0;
            time_start = std::chrono::system_clock::now();
            std::cout << fixed;
            matrix_dump(matrix);
            time_end = std::chrono::system_clock::now();
            res_time = (std::chrono::duration_cast<std::chrono::nanoseconds> (time_end - time_start).count()) / 1e9;
            time_now = start_res_time + res_time
            m.lock();
            q3.pop();
            q3_handled++;
            m.unlock();
        }
}


void parallel_execution(int count, size_t size)
{
    std::queue<int> q1;
    std::queue<matrix_t> q2;
    std::queue<matrix_t> q3;
    queues_t queues = {.q1 = q1, .q2 = q2, .q3 = q3};
    for (int i = 0; i < count; i++)
        q1.push(size);
    std::thread threads[3];
    threads[0] = std::thread(stage1_parallel, std::ref(q1), std::ref(q2), std::ref(q3));
    threads[1] = std::thread(stage2_parallel, std::ref(q1), std::ref(q2), std::ref(q3));
    threads[2] = std::thread(stage3_parallel, std::ref(q1), std::ref(q2), std::ref(q3));
    q2_recevied = count;
    q3_recevied = count;
    for (int i = 0; i < 3; i++)
        threads[i].join();
}


void time_measure()
{
    for (int m_size = 2; m_size < 11; m_size++)
        for (int m_count = 1; m_count < 5; m_count++)
        {
            std::chrono::time_point<std::chrono::system_clock> time_start_lin, time_end_lin, time_start_par, time_end_par;
            time_start_lin = std::chrono::system_clock::now();
            for (int i = 0; i < 3; i++)
                linear_execution(m_count, m_size, false);
            time_end_lin = std::chrono::system_clock::now();
            double res_time_lin = (std::chrono::duration_cast<std::chrono::nanoseconds>
                    (time_end_lin - time_start_lin).count()) / 1e9 / 3;
            time_start_par = std::chrono::system_clock::now();
            for (int i = 0; i < 3; i++)
                parallel_execution(m_count, m_size, false);
            time_end_par = std::chrono::system_clock::now();
            double res_time_par = (std::chrono::duration_cast<std::chrono::nanoseconds>
                    (time_end_par - time_start_par).count()) / 1e9 / 3;
            std::cout << "M size:  " << m_size << "  M count:  " << m_count << "   Linear:  " << res_time_lin << "   Parallel:  " << res_time_par << std::endl;
        }
}