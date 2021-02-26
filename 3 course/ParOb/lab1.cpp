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
            int count = 0;


            #pragma omp parallel for num_threads(threadNum) shared(arr) private(col) shared(row) private(a) private(b) shared(count)
            for (row = 0; row < n; row++) {
                count++;
                if (n == 300 && omp_get_thread_num()>6) {
                    //cout << "Thread #" << omp_get_thread_num() << " row #" << row << "\n";
                }
                for (col = 0; col < n; col++) {

                    a = (0.3*sqrt(row)) / (cos(col) + 5);
                    b = (row * sqrt(sin(row)))/2;

                    arr[row] += a * b;
                }
            }
            

            cout << "Time for " << threadNum << " threads - " << (omp_get_wtime() - start) << "s\n";
            //cout << "Size " <<  sizeof(arr) << "\n";
            //cout << "Count " <<  count << "\n";
            

            if (n == 300) { 
                //for (int i=0; i<n; i++) printf("%d ", arr[i]);
                cout << "\n"; 
            }
        }
    }
    return 0;
}