import sys
import cv2 as cv
import math
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp


img = [
    [10, 20, 200, 20],
    [100, 30, 210,120],
    [20, 130, 50, 5],
    [220, 200, 100, 150]
]

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base



def FFT_vectorized(x):
    """A vectorized, non-recursive version of the Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    # N_min here is equivalent to the stopping condition above,
    # and should be a power of 2
    N_min = min(N, 32)
    
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    # build-up each level of the recursive calculation all at once
    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()

def IFFT_vectorized(x):
    """A vectorized, non-recursive version of the Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    # N_min here is equivalent to the stopping condition above,
    # and should be a power of 2
    N_min = min(N, 32)
    
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    # build-up each level of the recursive calculation all at once
    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()


rows=len(img)
cols=len(img[0])

trueImg = [[0 for i in range(4)] for j in range(4)]



for row in range(rows):
    for col in range(cols):
        trueImg[row][col] = img[row][col]


newImg = trueImg.copy()
newImg1 = [[0 for i in range(4)] for j in range(4)]
newImg2 = [[0 for i in range(4)] for j in range(4)]
newImg10 = [[0 for i in range(4)] for j in range(4)]

rows=len(newImg)
cols=len(newImg[0])

for col in range(cols):
    arr=[0 for i in range(rows)]
    for row in range(rows):
        arr[row]=newImg[row][col]
    arr = FFT_vectorized(arr)
    for row in range(rows):
        newImg1[row][col] = arr[row]
    arr = FFT_vectorized(arr)
    for row in range(rows):
        newImg1[row][col] = arr[row]
    newImg10


for row in range(rows):
    newImg2[row] = FFT_vectorized(newImg1[row])








originalIm1 = np.array(newImg2)
shiftedIm1=np.fft.fftshift(originalIm1)
LowPassCenter = shiftedIm1 * gaussianLP(50,originalIm1.shape)
LowPass = np.fft.ifftshift(LowPassCenter)


endIm1 = LowPass.copy()

endIm2 = [[0 for i in range(4)] for j in range(4)]
endIm3 = [[0 for i in range(4)] for j in range(4)]

rows=len(endIm1)
cols=len(endIm1[0])



for row in range(rows):
    endIm2[row] = np.fft.ifft(endIm1[row])


for col in range(cols):
    arr=[0 for i in range(rows)]
    for row in range(rows):
        arr[row]=endIm2[row][col]
    arr = np.fft.ifft( arr)
    for row in range(rows):
        endIm3[row][col] = arr[row]






plt.subplot(131), plt.imshow(trueImg , "gray"), plt.title("img")
plt.subplot(132), plt.imshow(np.abs(newImg1), "gray"), plt.title("img")
plt.subplot(133), plt.imshow(np.abs(newImg10), "gray"), plt.title("img")
#plt.subplot(133), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("img")

#plt.subplot(132), plt.imshow(np.log(1+np.abs(originalIm1)), "gray"), plt.title("newImg")
#plt.subplot(133), plt.imshow(np.log(1+np.abs(originalIm2)), "gray"), plt.title("newImg")

plt.show()

