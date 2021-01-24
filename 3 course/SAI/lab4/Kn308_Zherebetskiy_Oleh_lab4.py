import sys
import cv2 as cv
import math
import numpy as np
import matplotlib.pyplot as plt
import imutils
from math import sqrt,exp


plt.axis("off")

#Пошук

def simplefindPos(MImage, edgesTemplate):
    dotsTemplate = np.argwhere(np.array(edgesTemplate) == 255)
    if (len(MImage)<len(edgesTemplate)) or (len(MImage[0])<len(edgesTemplate[0])):
        return 999999999,[]

    edgesRows = len(edgesTemplate)
    edgesCols = len(edgesTemplate[0])

    rows = len(MImage)
    cols = len(MImage[0])

    minSum = 1000000000
    minSumX = 0
    minSumY = 0

    for row in range(rows):
        for col in range(cols):
            if edgesRows+row>=rows or edgesCols+col>=cols:
                continue
            sum=0
            for xy in dotsTemplate:
                sum+=MImage[xy[0]+row][xy[1]+col]
                if minSum< sum:
                    break
            if minSum> sum:
                minSum = sum
                minSumX = row
                minSumY = col

    posMatrix=[[0 for i in range(cols)] for j in range(rows) ]
    for xy in dotsTemplate:
        posMatrix[xy[0]+minSumX][xy[1]+minSumY]=255

    return {"minSum":minSum, "x":minSumX,"y":minSumY}, posMatrix


#будує матрицю M, елементами якої є манхетенська відстань до найближчого контуру
def getM(edges):
    rows = len(edges)
    cols = len(edges[0])
    
    M = [[rows+cols+1 for i in range(cols)] for i in range(rows) ]

    dots = np.argwhere(np.array(edges) ==255)

    for el in dots:
        for irow in range(rows):
            for icol in range(cols): 
                if M[irow][icol]> abs((irow-el[0]))+abs((icol-el[1])):
                    M[irow][icol]= abs((irow-el[0]))+abs((icol-el[1]))

    return M


#завантажує зображення
def loadImage(name):
    return cv.imread(name)


def loadTemplate(name):
    template = cv.imread(name)
    templateBW = imageBlackandWhite(template)
    return getEdges(templateBW,100,200)


#знаходить контури на зображенні (canny)
def getEdges(img, minP, maxP):
    return cv.Canny(img,minP,maxP)

#перетворює зображення на ЧБ
def imageBlackandWhite(image):

    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY)
    
    return grayImage

def connect(image1, template1Pos, template1Sum, template1):
    rows = len(image1)
    cols = len(image1[0])

    image1template1 = [[0 for i in range(cols)] for i in range(rows) ]

    for row in range(rows):
        for col in range(cols):
            if template1Pos[row][col]==255:
                image1template1[row][col]=[255,0,0]
            else:
                image1template1[row][col]=image1[row][col]
    for x in range(len(template1)):
        image1template1[template1Sum['x']+x][template1Sum['y']]=[0,0,255]
        image1template1[template1Sum['x']+x][template1Sum['y']+len(template1[0])-1]=[0,0,255]
    for y in range(len(template1[0])):
        image1template1[template1Sum['x']][template1Sum['y']+y]=[0,0,255]
        image1template1[template1Sum['x']+len(template1)-1][template1Sum['y']+y]=[0,0,255]
        
    return image1template1


image1 = loadImage("image1.png")

image1BW = imageBlackandWhite(image1)

image1Edges = getEdges(image1BW,100,200)

image2 = loadImage("image2.png")

image2BW = imageBlackandWhite(image2)

image2Edges = getEdges(image2BW,100,200)

print(image1)

plt.imshow(image1)
plt.title('Image 1')

plt.imshow(image1BW, "gray")
plt.title('Image BW 1')

plt.imshow(image1Edges, "gray")
plt.title('Image Edges 1')

image1M = getM(image1Edges)

with open('image1M.npy', 'wb') as f:
    np.save(f, np.array(image1M))
    
    
with open('image1M.npy', 'rb') as f:
    image1M = np.load(f).tolist()
    
    
plt.imshow(image1M)
plt.title('image1M')

print(image1M)

plt.imshow(template1Pos, "gray")
plt.title('Template pos 1')

image1template1 = connect(image1, template1Pos, template1Sum, template1)

plt.imshow(image1template1)
plt.title('image1template1')

cv.imwrite('image1template1.png', np.array(image1template1))
cv.imwrite('templateedge1.png', np.array(template1))