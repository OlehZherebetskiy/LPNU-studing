import sys
import cv2 as cv
import math
import numpy as np
import matplotlib.pyplot as plt
import imutils
from math import sqrt,exp

'''
40.(складна) перша четверта лаби з власною реалізацією fft+маштабування і поворот шаблону

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


coloredImages = []
greyImages = []
edgesImages = []
Mmatrix = []
fftImages = []
fftNewImages = []
fftImageBackShifteds = []
fftFiltereds = []
fftImageShifteds = []
fftImages = []
poses=[]





'''
.............................................
    Власна реалізація перетворення Фур'є
.............................................
.
'''

def FFT(x):
    # Векторна реалізація, нерекурсивна, версія Cooley-Tukey

    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    N_min = min(N, 32)
    
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()



def IFFT(x):
    # Векторна реалізація, нерекурсивна, версія Cooley-Tukey

    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    N_min = min(N, 32)
    
    n = np.arange(N_min)
    k = n[:, None]
    M = np.exp(2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        X_even = X[:, :int(X.shape[1] / 2)]
        X_odd = X[:, int(X.shape[1] / 2):]
        factor = np.exp(1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()


'''
.............................................
    Власна реалізація перетворення Фур'є для 2D
.............................................
.
'''
def FFT2D(X):

    rows = len(X)
    cols = len(X[0])

    X0 = X.copy()
    X1 = [[0 for i in range(cols)] for j in range(rows)]
    X2 = [[0 for i in range(cols)] for j in range(rows)]

    for col in range(cols):
        arr=[0 for i in range(rows)]
        for row in range(rows):
            arr[row]=X0[row][col]
        arr = np.fft.fft(arr)
        for row in range(rows):
            X1[row][col] = arr[row]

    for row in range(rows):
        X2[row] = np.fft.fft(X1[row])

    return X2


def IFFT2D(X):

    rows = len(X)
    cols = len(X[0])

    X0 = X.copy()
    X1 = [[0 for i in range(cols)] for j in range(rows)]
    X2 = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        X1[row] = np.fft.ifft(X0[row])


    for col in range(cols):
        arr=[0 for i in range(rows)]
        for row in range(rows):
            arr[row]=X1[row][col]
        arr = np.fft.ifft( arr)
        for row in range(rows):
            X2[row][col] = arr[row]
        
    return X2


'''
.............................................
    Релізація Гаусівського фільтру
.............................................
.
'''

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


'''
.............................................
    Зсування 0 частоти до центру та назад
.............................................
.
'''
def FFTShift(X):
    return np.fft.fftshift(X)

def IFFTShift(X):
    return np.fft.ifftshift(X)

'''
.............................................
    Пошук контура на зображенні
.............................................
.
'''
def edgesFind(X):
    M = np.abs(X.copy())
    grad, grad_x, grad_y = gradFind(M)
    angle = angleGradFind(grad, grad_x, grad_y)
    edges = chooseEdges(grad, angle)
    return edges


'''.............................................
    Пошук градієнта для кожної точки
.............................................'''

def gradFind(X):
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    grad_x = cv.Sobel(X, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    grad_y = cv.Sobel(X, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    return grad, grad_x, grad_y

'''.............................................
    Пошук кута градієнта для кожної точки
.............................................'''

def angleGradFind(grad, grad_x, grad_y):
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

    return angle


'''.............................................
    Відділення точок які відповідають адекватним контурам
.............................................'''

def chooseEdges(grad, angle):
    rows = len(grad)
    cols = len(grad[0])

    edges = [[0 for i in range(cols)] for j in range(rows)]

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
                edges[row][col]=255
    return edges



'''
.............................................
    Побудова матриці Манхетенських відстаней
.............................................
.
'''

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


'''
.............................................
    Звичайний пошук розміщення шаблону на зображенні
.............................................
.
'''

def simplefindPos(MImage, edgesTemplate):
    dotsTemplate = np.argwhere(np.array(edgesTemplate) == 255)

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

    posMatrix=[[rows+cols+1 for i in range(cols)] for j in range(rows) ]
    for xy in dotsTemplate:
        posMatrix[xy[0]+minSumX][xy[1]+minSumY]=255

    return minSum, posMatrix



'''
.............................................
    Пошук розміщення шаблону на зображенні зі зміною маштабу шаблону
.............................................
.
'''

def scalefindPos(MImage, imageNum, filterType, filterParam):

    minSum = 1000000000
    minSumPos = []
    minSumScale = 0
    
    for scale_percent in range(100,80,-5):

        image = np.array(greyImages[imageNum])

        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        # resize image
        image = cv.resize(image, dim, interpolation = cv.INTER_AREA)

        fftImage = FFT2D(image)
        fftImageShifted = FFTShift(fftImage)
        fftFiltered = []
        if filterType == 0:
            fftFiltered = fftImageShifted * gaussianLP(filterParam, fftImageShifted.shape)
        else:
            fftFiltered = fftImageShifted * gaussianRP(filterParam, fftImageShifted.shape)
        fftImageBackShifted = IFFTShift(fftFiltered)
        fftNewImage = IFFT2D(fftImageBackShifted)

        imageEdges = edgesFind(fftNewImage)

        
        Sum, posMatrix = simplefindPos(MImage, imageEdges)

        if minSum > Sum:
            minSum = Sum
            minSumPos = posMatrix
            minSumScale = scale_percent
    
    return minSum, minSumPos, minSumScale



'''
.............................................
    Пошук розміщення шаблону на зображенні зі зміною маштабу шаблону та обертанням
.............................................
.
'''
def rotateScalefindPos(MImage, imageNum, filterType, filterParam):

    image = greyImages[imageNum]

    minSum = 1000000000
    minSumPos = []
    minSumScale = 0
    minSumAngle = 0
    for scale_percent in range(100,80,-5):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        # resize image
        image = cv.resize(image, dim, interpolation = cv.INTER_AREA)

        fftImage = FFT2D(image)
        fftImageShifted = FFTShift(fftImage)
        if filterType == 0:
            fftFiltered = fftImageShifted * gaussianLP(filterParam, fftImageShifted.shape)
        else:
            fftFiltered = fftImageShifted * gaussianRP(filterParam, fftImageShifted.shape)
        fftImageBackShifted = IFFTShift(fftFiltered)
        fftNewImage = IFFT2D(fftImageBackShifted)

        imageEdges = edgesFind(fftNewImage)
        
        
        for angle in np.arange(0, 360, 15):
            rotated = imutils.rotate_bound(np.uint8(np.abs(imageEdges)), angle)

            Sum, posMatrix = simplefindPos(MImage, rotated)
            if minSum > Sum:
                minSum = Sum
                minSumPos = posMatrix
                minSumScale = scale_percent
                minSumAngle = angle

    return minSum, minSumPos, minSumScale, minSumAngle

'''
.............................................
    Виведення графіка
.............................................
.
'''
def showPlot(imageTypeNum, imageNum):
    if imageTypeNum == "0":
        plt.subplot(131),plt.imshow(coloredImages[imageNum])
        plt.title('Image Colored'), plt.xticks([]), plt.yticks([])
    elif imageTypeNum == "1":
        plt.subplot(131),plt.imshow(greyImages[imageNum], "gray")
        plt.title('Input Gray'), plt.xticks([]), plt.yticks([])
    elif imageTypeNum == "2":
        plt.subplot(131), plt.imshow(edgesImages[imageNum], "gray"), plt.title("Edge image")
    elif imageTypeNum == "3":
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImages[imageNum])), "gray"), plt.title(".fftImages. image")
    elif imageTypeNum == "4":
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftNewImages[imageNum])), "gray"), plt.title(".fftNewImages. image")
    elif imageTypeNum == "5":
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageBackShifteds[imageNum])), "gray"), plt.title(".fftImageBackShifteds. image")
    elif imageTypeNum == "6":
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftFiltereds[imageNum])), "gray"), plt.title(".fftFiltereds. image")
    elif imageTypeNum == "7":
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageShifteds[imageNum])), "gray"), plt.title(".fftImageShifteds. image")
    elif imageTypeNum == "8":
        plt.subplot(131), plt.imshow(fftImages[imageNum], "gray"), plt.title("New image")
    elif imageTypeNum == "9":
        plt.subplot(132), plt.imshow(poses[imageNum], "gray"), plt.title("posM")

    plt.show()






'''
.............................................
    Завантажити зображення(зберегти)
.............................................
.
'''
def loadNewImage(name):
    return cv.imread(name), cv.imread(name,0)

'''
.............................................
.............................................
.
'''



'''
.............................................
    Меню
.............................................
.
'''

colored, grey = loadNewImage("image2.jpg")
coloredImages.append(colored)
greyImages.append(grey)

colored, grey = loadNewImage("template2.png")
coloredImages.append(colored)
greyImages.append(grey)

colored, grey = loadNewImage("image.jpg")
coloredImages.append(colored)
greyImages.append(grey)

colored, grey = loadNewImage("template.png")
coloredImages.append(colored)
greyImages.append(grey)

colored, grey = loadNewImage("template01.png")
coloredImages.append(colored)
greyImages.append(grey)


while True:
    print('Choose comand num:\n'+
            '0 - Load new Image\n'+
            '1 - Show Image\n'+
            '2 - Simple find template position\n'+
            '3 - Simple find 2.0\n'+
            '4 - Find position with scale\n'+
            '5 - Find position with scale and rotate\n'+
            '6 - Find Edge\n'+
            '7 - Calc M matrix\n'
    )
    comandNum = str(input())

    if comandNum == "0":

        print("Image file name: ")
        fileName = str(input())

        colored, grey = loadNewImage(fileName)
        coloredImages.append(colored)
        greyImages.append(grey)

    elif comandNum == "1":

        print('Choose image type num:\n'+
            '0 - Colored\n'+
            '1 - Grey\n'+
            '2 - Edge image\n'+
            '3 - fftImages\n'+
            '4 - fftNewImages\n'+
            '5 - fftImageBackShifteds\n'+
            '6 - fftFiltereds\n'+
            '7 - fftImageShifteds\n'+
            '8 - fftImages\n'+
            '9 - poses'
        )
        imageTypeNum = str(input())

        print('Choose image num:')
        imageNum = int(input())

        showPlot(imageTypeNum, imageNum)

    elif comandNum == "2":

        print('Choose image num:')
        imageNum = int(input())

        print('Choose template num:')
        templateNum = int(input())

        image = greyImages[imageNum]
        template = greyImages[templateNum]

        fftImage = FFT2D(image)
        fftImages.append(fftImage)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImage)), "gray"), plt.title(".fftImage. image")
        plt.show()

        fftImageShifted = FFTShift(fftImage)
        fftImageShifteds.append(fftImageShifted)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageShifted)), "gray"), plt.title(".fftImageShifted. image")
        plt.show()

        fftFiltered = fftImageShifted * gaussianLP(50, fftImageShifted.shape)
        fftFiltereds.append(fftFiltered)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftFiltered)), "gray"), plt.title(".fftFiltered. image")
        plt.show()

        fftImageBackShifted = IFFTShift(fftFiltered)
        fftImageBackShifteds.append[fftImageBackShifted]
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageBackShifted)), "gray"), plt.title(".fftImageBackShifted. image")
        plt.show()

        fftNewImage = IFFT2D(fftImageBackShifted)
        fftNewImages.append(fftNewImage)
        plt.subplot(131), plt.imshow(fftNewImage, "gray"), plt.title("New image")
        plt.show()

        imageEdges = edgesFind(fftNewImage)
        edgesImages.append(imageEdges)
        plt.subplot(131), plt.imshow(imageEdges, "gray"), plt.title("Edge image")
        plt.show()

        print("Start M matrix calc...")
        imageMMatrix = getM(imageEdges)
        Mmatrix.append(imageMMatrix)
        print("end.")

        fftTemplate = FFT2D(template)
        fftTemplateShifted = FFTShift(fftTemplate)
        fftTemplateFiltered = fftTemplateShifted * gaussianLP(50, fftTemplateShifted.shape)
        fftTemplateBackShifted = IFFTShift(fftTemplateFiltered)
        fftNewTemplate = IFFT2D(fftTemplateBackShifted)

        templateEdges = edgesFind(fftNewTemplate)

        sum, posM = simplefindPos(imageMMatrix, templateEdges)

        plt.subplot(131), plt.imshow(image, "gray"), plt.title("image")
        plt.subplot(132), plt.imshow(posM, "gray"), plt.title("posM")
        plt.show()

    elif comandNum == "3":
        print('Choose M matrix num:')
        matrixNum = int(input())
        imageMMatrix = Mmatrix[matrixNum]

        print('Choose template edge num:')
        templateEdgesNum = int(input())
        templateEdges = edgesImages[templateEdgesNum]

        print('Choose image num:')
        imageNum = int(input())

        sum, posM = simplefindPos(imageMMatrix, templateEdges)
        print(sum)

        plt.subplot(131), plt.imshow(greyImages[imageNum], "gray"), plt.title("image")
        plt.subplot(132), plt.imshow(posM, "gray"), plt.title("posM")
        poses.append(posM)
        plt.show()
    elif comandNum == "4":
        print('Choose M matrix num:')   
        matrixNum = int(input())
        imageMMatrix = Mmatrix[matrixNum]

        print('Choose image num:')
        imageNum = int(input())

        print('Choose template image num:')
        templateEdgesNum = int(input())

        print('Choose filter type num:\n'+
        '0 - Low\n'+
        '1 - High\n')
        filterType = int(input())

        print('Choose filter param:')
        filterParam = int(input())

        sum, posM, scale = scalefindPos(imageMMatrix, templateEdgesNum, filterType, filterParam)

        print(sum)
        print(scale)
        plt.subplot(131), plt.imshow(greyImages[imageNum], "gray"), plt.title("image")
        plt.subplot(132), plt.imshow(posM, "gray"), plt.title("posM")
        poses.append(posM)
        plt.show()
        

    elif comandNum == "5":
        print('Choose M matrix num:')   
        matrixNum = int(input())
        imageMMatrix = Mmatrix[matrixNum]

        print('Choose template image num:')
        templateEdgesNum = int(input())

        print('Choose image num:')
        imageNum = int(input())

        print('Choose filter type num:\n'+
        '0 - Low\n'+
        '1 - High\n')
        filterType = int(input())

        print('Choose filter param:')
        filterParam = int(input())

        sum, posM, scale, angle = rotateScalefindPos(imageMMatrix, templateEdgesNum, filterType, filterParam)
        print(angle)
        print(scale)
        print(sum)

        plt.subplot(131), plt.imshow(greyImages[imageNum], "gray"), plt.title("image")
        plt.subplot(132), plt.imshow(posM, "gray"), plt.title("posM")
        poses.append(posM)
        plt.show()
        
    elif comandNum == "6":
        print('Choose image num:')
        imageNum = int(input())

        print('Choose filter type num:\n'+
        '0 - Low\n'+
        '1 - High\n')
        filterType = int(input())

        print('Choose filter param:')
        filterParam = int(input())

        image = greyImages[imageNum]

        fftImage = FFT2D(image)
        fftImages.append(fftImage)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImage)), "gray"), plt.title(".fftImage. image")
        plt.show()

        fftImageShifted = FFTShift(fftImage)
        fftImageShifteds.append(fftImageShifted)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageShifted)), "gray"), plt.title(".fftImageShifted. image")
        plt.show()

        fftFiltered = []
        if filterType==0:
            fftFiltered = fftImageShifted * gaussianLP(filterParam, fftImageShifted.shape)
        else:
            fftFiltered = fftImageShifted * gaussianHP(filterParam, fftImageShifted.shape)
        fftFiltereds.append(fftFiltered)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftFiltered)), "gray"), plt.title(".fftFiltered. image")
        plt.show()

        fftImageBackShifted = IFFTShift(fftFiltered)
        fftImageBackShifteds.append(fftImageBackShifted)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftImageBackShifted)), "gray"), plt.title(".fftImageBackShifted. image")
        plt.show()

        fftNewImage = IFFT2D(fftImageBackShifted)
        fftNewImages.append(fftNewImage)
        plt.subplot(131), plt.imshow(np.log(1+np.abs(fftNewImage)), "gray"), plt.title(".fftNewImage. image")
        plt.show()

        imageEdges = edgesFind(fftNewImage)
        edgesImages.append(imageEdges)
        plt.subplot(131), plt.imshow(imageEdges, "gray"), plt.title("Edge image")
        plt.show()


    elif comandNum == "7":

        print('Choose image edge num:')
        imageNum = int(input())

        imageEdges = edgesImages[imageNum]

        print("Start M matrix calc...")
        imageMMatrix = getM(imageEdges)
        print("end.")
        print(imageMMatrix[20][:100])

        Mmatrix.append(imageMMatrix)








        








