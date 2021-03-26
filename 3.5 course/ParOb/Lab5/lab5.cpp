#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <iostream>
#define SIZE 1000
#define BLOCK 1500


__global__ void addVector(float* result, int n)
{
	int i = threadIdx.x;
	for(int x = i; x<n; x+= BLOCK)
		result[x] = (1 + sin(sqrt(x+1)))/(cos(12*n*n - 4));
}


__host__ int main()
{
	float* vec1 = new float[SIZE];

	float time;
	cudaEvent_t start, stop;

	float* devVec1;

	cudaMalloc((void**)&devVec1, sizeof(float) * SIZE);
	cudaMemcpy(devVec1, vec1, sizeof(float) * SIZE, cudaMemcpyHostToDevice);


	dim3 gridSize = dim3(1, 1, 1);
	dim3 blockSize = dim3(256, 1, 1);

	cudaEventCreate(&start);
	cudaEventCreate(&stop);
	cudaEventRecord(start, 0);

	addVector << <gridSize, blockSize >> > (devVec1, SIZE);

	cudaEventRecord(stop, 0);
	cudaEventSynchronize(stop);
	cudaEventElapsedTime(&time, start, stop);

	cudaEvent_t syncEvent;

	cudaEventCreate(&syncEvent);
	cudaEventRecord(syncEvent, 0);
	cudaEventSynchronize(syncEvent);

	cudaMemcpy(vec1, devVec1, sizeof(float) * SIZE, cudaMemcpyDeviceToHost);

	cudaEventDestroy(syncEvent);
	cudaFree(devVec1);
	printf("Time to generate:  %3.1f ms \n", time);
	delete[] vec1; vec1 = 0;

}
