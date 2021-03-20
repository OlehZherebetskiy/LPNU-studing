import sys
import cv2 as cv
import math
import numpy as np
import matplotlib.pyplot as plt



scale = 1
delta = 0
ddepth = cv.CV_16S



# Load the image
src = cv.imread("image2.jpg")





src = cv.GaussianBlur(src, (3, 3), 0)


gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)


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

plt.subplot(131), plt.imshow(grad), plt.title("grad")
plt.subplot(132), plt.imshow(dots, "gray"), plt.title("dots")
plt.show()

