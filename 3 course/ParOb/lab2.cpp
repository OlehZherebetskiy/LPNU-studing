#include <iostream>
#include <omp.h>
#include <math.h>
#include <vector>
#include <time.h>

int N = 8000;

using namespace std;

vector<int> not_parallel(vector<vector<double>> mtx) {
  vector<int> res;
  res.resize(N);
  double st = omp_get_wtime();
  for (int i = 0; i < N; i++)
  {
    int counter = 0;
    for (int j = 0; j < N; j++) if (mtx[i][j] < 0) counter++;
    res[i] = counter;
  }
  double en = omp_get_wtime();
  cout << "single thread:" << "[ duration: " << en - st << " seconds ]" << endl;
  return res;
}

vector<int> parallel(vector<vector<double>> mtx, int chunk) {
  vector<int> res;
  res.resize(N);
  double st = omp_get_wtime();
# pragma omp parallel for shared(mtx) schedule(static, chunk)
  for (int i = 0; i < N; i++)
  {
    int counter = 0;
    for (int j = 0; j < N; j++) if (mtx[i][j] < 0) counter++;
    res[i] = counter;
  }
  double en = omp_get_wtime();
  cout << "parallel(static schedule, chunk=" << chunk << "):" << "[ duration: " << en - st << " seconds ]" << endl;

  st = omp_get_wtime();
# pragma omp parallel for shared(mtx) schedule(dynamic, chunk)
  for (int i = 0; i < N; i++)
  {
    int counter = 0;
    for (int j = 0; j < N; j++) if (mtx[i][j] < 0) counter++;
    res[i] = counter;
  }
  en = omp_get_wtime();
  cout << "parallel(dynamic schedule, chunk=" << chunk << "):" << "[ duration: " << en - st << " seconds ]" << endl;

  return res;
}

int main()
{
  vector<vector<double>> A;
  vector<vector<double>> B;

  A.resize(N);
  B.resize(N);

  srand(time(NULL));
  int n = 0;
  std::cout << "Matrix\n0 -> auto generating\n1 -> manual input" << endl;
  cin >> n;
  switch (n) {
  case 0:
    std::cout << "generating..." << endl;
# pragma omp parallel for shared(A, B)
    for (int i = 0; i < N; i++) {
      A[i].resize(N);
      B[i].resize(N);
      for (int j = 0; j < N; j++) {
        A[i][j] = (rand() % 1000 - 1000) + (rand() % 1000);
        B[i][j] = (rand() % 1000 - 1000) + (rand() % 1000);
      }
    }
    break;
  case 1:
    std::cout << "input pairs [A element] [B element] one by one" << endl;
    for (int i = 0; i < N; i++) {
      A[i].resize(N);
      B[i].resize(N);
      for (int j = 0; j < N; j++) {
        cin >> A[i][j];
        cin >> B[i][j];
      }
    }
    break;
  }

  std::cout << "matrix A and B generated" << endl;
  std::system("pause");

  vector<int> C = not_parallel(A);
  vector<int> D = not_parallel(B);

  for (int chunk = 4; chunk <= 32; chunk += 4) {
    C = parallel(A, chunk);
    D = parallel(B, chunk);
    cout << endl;
  };

}