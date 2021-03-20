#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <omp.h>
#include "mpi.h"

using namespace std;

double f(double x, double z) {
	return (1 + sin(sqrt(x+1)))/(cos(12*z - 4));
}

int main(int argc, char* argv[]) {

	int rank, num, chunkLen;
	double  start, finish;
	double res = 0;

	double N = 10;
	double z = N * N;

	//change
	//double chunkNums = N / 2; 
	double chunkNums = N * 1 * pow(10,4);


	double step = N / chunkNums;


	start = omp_get_wtime();

	MPI_Status Status;
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &num);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	

	for (double x = 1 - step + step*(rank + 1); x < N+1; x+= step*num) {
		res += f(x, z);
	}

	if (rank != 0) {
		MPI_Send(&res, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
	}

	MPI_Barrier(MPI_COMM_WORLD);

	finish = omp_get_wtime();




	if (rank == 0) {
		double sum = res;
		for (int i = 1; i < num; i++) {
			MPI_Recv(&res, 1, MPI_DOUBLE, MPI_ANY_SOURCE,
				MPI_ANY_TAG, MPI_COMM_WORLD, &Status);
			sum += res;
		}
		sum /= chunkNums;
		cout << "chunkNums = " << chunkNums << " time = " << finish - start << endl;
		cout << "mean" << " = " << sum << endl;
	}


	MPI_Finalize();
	
	
}