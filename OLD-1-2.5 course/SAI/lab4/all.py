import sys
import cv2 as cv
import math
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp


img = cv.imread("image2.jpg",0)

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

def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
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




IMGrows=len(img)
IMGcols=len(img[0])



trueImg = [[0 for i in range(512)] for j in range(256)]

for row in range(IMGrows):
    for col in range(IMGcols):
        trueImg[row][col] = img[row][col]





newImg = trueImg.copy()
newImg1 = [[0 for i in range(512)] for j in range(256)]
newImg2 = [[0 for i in range(512)] for j in range(256)]

rows=len(newImg)
cols=len(newImg[0])

for col in range(cols):
    arr=[0 for i in range(rows)]
    for row in range(rows):
        arr[row]=newImg[row][col]
    arr = np.fft.fft(arr)
    for row in range(rows):
        newImg1[row][col] = arr[row]


for row in range(rows):
    newImg2[row] = np.fft.fft(newImg1[row])








originalIm1 = np.array(newImg2)
shiftedIm1=np.fft.fftshift(originalIm1)
LowPassCenter = shiftedIm1 * gaussianLP(50,originalIm1.shape)
LowPass = np.fft.ifftshift(LowPassCenter)


endIm1 = LowPass.copy()
endIm2 = [[0 for i in range(512)] for j in range(256)]
endIm3 = [[0 for i in range(512)] for j in range(256)]
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







endIm3=np.array(endIm3)[:IMGrows,:IMGcols]

plt.subplot(131), plt.imshow(img), plt.title("img")
plt.subplot(132), plt.imshow(np.abs(endIm3), "gray"), plt.title("after fft + gaussianLP")


res = np.abs(endIm3)


scale = 1
delta = 0
ddepth = cv.CV_16S

gray = res


grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)


abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)


grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

rows = len(grad)
cols = len(grad[0])
angle = [[0 for i in range(cols)] for j in range(rows)]
for row in range(rows):
    for col in range(cols):
        an=math.atan(np.divide(grad_x[row][col],grad_y[row][col]))
        if an>= -math.pi/4 and an<= math.pi/4:
            an=0
        elif (an>= 3*math.pi/4 and an<= math.pi) or  (an>= -math.pi and an<= -3*math.pi/4):
            an=2
        elif an> math.pi/4 and an< 3*math.pi/4:
            an=1
        elif an> -3*math.pi/4 and an < -math.pi/4:
            an=3

        angle[row][col] = an


dots = [[0 for i in range(cols)] for j in range(rows)]
for row in range(rows):
    for col in range(cols):
        if grad[row][col]<50:
            continue
        check=False
        if angle[row][col]==0 and row+1<rows:
            check = grad[row][col]> grad[row+1][col]
        elif angle[row][col]==1 and col-1>0:
            check = grad[row][col]> grad[row][col-1]
        elif angle[row][col]==2 and row-1>0:
            check = grad[row][col]> grad[row-1][col]
        elif angle[row][col]==3 and col+1<cols:
            check = grad[row][col]> grad[row][col+1]
        if check:
            dots[row][col]=1


plt.subplot(133), plt.imshow(dots, "gray"), plt.title("edges")
plt.show()

