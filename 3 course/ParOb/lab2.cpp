#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

int main()
{
    int n,thrNum,i, chankNum;

    vector <vector<int>> A;
    vector <vector<int>> B;

    cout << "N: " << endl;
    cin >> n;
    //cout << "thread num: " << endl;
   //cin >> thrNum;

    vector <int> C(n);
    vector <int> D(n);


    int count = 0;
    int count1 = 0;

    
    A.resize(n);
    B.resize(n);
    for (i = 0; i < n; i++) {
        A[i].resize(n);
        B[i].resize(n);
        for (int j = 0; j < n; j++) {
            A[i][j] = rand() % 200 - 100;
            B[i][j] = rand() % 200 - 100;
        }
    }


    std::system("pause");

    for(int thrNum = 1; thrNum <= 16; thrNum *= 2){
        for(int chunkNum = 4; chunkNum <= 20; chunkNum += 4){

            //cout << "thrNum: "<< thrNum<< " chunk: "<< chunkNum << endl;


           // cout << "Dynamic" << endl;

            double start = omp_get_wtime();
            #pragma omp parallel num_threads(thrNum) shared(i) shared(n) private(count) private(count1)
                {
                #pragma omp for schedule(dynamic, chunkNum)
                for (i = 0; i < n; i++) {
                    count = 0;
                   // cout << "inter: " <<i << "thr: " << omp_get_thread_num()<< endl;
                    for (int j = 0; j < n; j++) {                    
                        if (A[i][j] < 10 && A[i][j] > -10) {
                            count++;
                        }
                        if (B[i][j] < 10 && B[i][j] > -10) {
                            count1++;
                        }
                    }
                    C[i] = count;
                    D[i] = count1;
                }
            }
            double end = omp_get_wtime();

            for (i = 0; i < n; i++) {
           // cout << C[i]; 
            }
            //cout << endl;
            //cout << "t = " << end - start << endl;
            cout << end - start << endl;



            //cout << "Guided" << endl;
            i=0;

            double start1 = omp_get_wtime();
            #pragma omp parallel num_threads(thrNum) shared(i) shared(n) private(count) private(count1)
                {
            #pragma omp for schedule(guided, chunkNum)
                for(i = 0;i < n; i++){
                  //  cout << "inter: " <<i << "   thr: " << omp_get_thread_num()<< endl;
                    for (int j = 0; j < n; j++) {
                        if (A[i][j] < 10 && A[i][j] > -10) {
                            count++;
                        }
                        if (B[i][j] < 10 && B[i][j] > -10) {
                            count1++;
                        }
                    }
                    C[i] = count;
                    D[i] = count1;
                }
            }        
            double end1 = omp_get_wtime();

            for (i = 0; i < n; i++) {
            //    cout << C[i]; 
            }
            //cout << endl;
            //cout << "t = " << end1 - start1 << endl;
            cout << end1 - start1 << endl;
        }
    }
    
}
