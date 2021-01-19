'''
40. перша четверта лаби з власною реалізацією fft+маштабування і поворот шаблону
'''
'''
Написати програму яка шукає шаблон на зображені наступним чином
Підготовка
1 - перетворює зображення на ЧБ.
2 - знаходить контури на зображенні (canny)
3 - будує матрицю M, елементами якої є манхетенська відстань до найближчого контуру
Шаблон
Шаблоном є бінарне зображення пікселі якого 1 або 0
Пошук
Результатом пошуку є така позиція шаблону на матриці, що сума всіх елементів M які відповідають 1 в шаблоні, була мінімальною.
'''
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


def getEdges(file):
    originalImage = cv2.imread(file,0)


    f = np.fft.fft2(originalImage)
    fshift = np.fft.fftshift(f)

    rows, cols = originalImage.shape
    crow,ccol = int(rows/2) , int(cols/2)
    fshift[crow-50:crow+50, ccol-50:ccol+50] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    img=slice1Copy = np.uint8(img_back)
    edges = cv2.Canny(img,100,110)
    print("ROW: "+ str(rows))
    print("COL: " + str(cols))

    plt.subplot(131),plt.imshow(originalImage)
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(edges,cmap = 'Greys')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()


    edges = np.array(edges)
    return edges, originalImage

def getM(edges):
    rows = len(edges)
    cols = len(edges[0])
    
    M = [[rows+cols+1 for i in range(cols)] for i in range(rows) ]

    dots = np.argwhere(edges == 255)

    print("Num dots: "+ str(len(dots)))

    for el in dots:
        for irow in range(rows):
            for icol in range(cols): 
                if M[irow][icol]> abs((irow-el[0]))+abs((icol-el[1])):
                    M[irow][icol]= abs((irow-el[0]))+abs((icol-el[1]))

    #print(M)
    return M


def findPos(MImage, edgesTemplate):
    dotsTemplate = np.argwhere(edgesTemplate == 255)

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
    print("Min Sum: " + str(minSum))
    print("Row: " + str(minSumX))
    print("Col: " + str(minSumY))

    posMatrix=[[rows+cols+1 for i in range(cols)] for i in range(rows) ]
    for xy in dotsTemplate:
        posMatrix[xy[0]+minSumX][xy[1]+minSumY]=255

    return posMatrix



edgesImage, image = getEdges("image.jpg")
MImage = getM(edgesImage)
edgesTemplate, template = getEdges("template.png")

posMatrix = findPos(MImage, edgesTemplate)



plt.subplot(131),plt.imshow(edgesImage, cmap = 'Greys')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(posMatrix, cmap = 'Greys')
plt.title('posMatrix'), plt.xticks([]), plt.yticks([])

plt.show()
