#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;


int main(int argc, char* argv[]) {

    system("pause");

    int n = 300;

    for ( ; n <= 10000; n *= 2) {

        float a, b;
        int row, col;
        vector<double> arr(n);
        double runtime = 0;
        double start;

        cout << "For n=" << n << ":\n\n";

        for (int threadNum = 1; threadNum <= 32; threadNum *= 2) {
            start = omp_get_wtime();


            #pragma omp parallel for num_threads(threadNum) shared(arr) private(col) shared(row)
            for (row = 0; row < n; row++) {
                if (n == 300) {
                    cout << "Thread #" << omp_get_thread_num() << " row #" << row << "\n";
                }
                for (col = 0; col < n; col++) {

                    a = (0.3*sqrt(row)) / (cos(col) + 5);
                    b = (row * sqrt(sin(row)))/2;

                    arr[row] += a * b;
                } 
            }


            cout << "Time for " << threadNum << " threads - " << (omp_get_wtime() - start) << "s\n";
        }
    }
    return 0;
}