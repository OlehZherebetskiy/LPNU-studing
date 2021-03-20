#include <omp.h>
#include <iostream>
#include <vector>
#include <windows.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

double f1(double x) {
	return (log(1+x*x))/(0.5*sqrt(x*(1+x)*(1+x)));
}

double f2(double x) {
	return (x*x*x)/(x*x - 0.42*0.42);
}

omp_lock_t lock;
	
int main()
{
    ofstream file;
    file.open("lab3.txt");


	double step, n1, n2, a1, b1, a2, b2;

    for (int n = 1; n <= 100; n *= 10) {

        step = 0.000002/n;
        a1 = 0;
        b1 = 1;
        a2 = 0.5;
        b2 = 2.5;

        n1 = floor(((b1 - a1) / step));
        

        for (int threads = 1; threads <= 16; threads *= 2) {
            double res1 = 0;
            double res2 = 0;
            double sum = 0;
            double start = omp_get_wtime();
            omp_init_lock(&lock);

            #pragma omp parallel num_threads(threads) private(res1, res2) shared(sum)
                {
                    #pragma omp single
                    file << "\n\n\n\n Lab #3 Завантаження та синхронізація в OpenMP Kn-308 Zherebetskiy Oleh var #10" << endl;
                    #pragma omp single
                    file << "step:"<< step << "           numThread: "<< threads << endl;

                    int id = omp_get_thread_num();
                    int numt = omp_get_num_threads();

                    


                    while (!omp_test_lock(&lock)) {
                        #pragma omp critical
                        file << "The section is closed, thred num :" << id << endl;
                        Sleep(2);
                    }
                    file << "The beginning of the closed section, thred num : " << id << endl;

                    for (int x = id + 1; x <= n1; x = x + numt)
                        res1 += f1((a1 + step * x) - step / 2);
                    
                    //for (int x = id + 1; x <= n2; x = x + numt)
                    //    res2 += f2((a2 + step * x) - step / 2);

                    res1 *= step;
                    //res2 *= step;

                    sum += res1;
                    file << "The end of the closed section, thred num : " << id << endl;
                    omp_unset_lock(&lock);


                }

                omp_destroy_lock(&lock);
		        double finish = omp_get_wtime();

                file << " \ntime: "<< finish - start << "\n";
                file << " \nres: "<< sum << "\n";
        } 

    }
    file.close();
}
