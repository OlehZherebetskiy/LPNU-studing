from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

width, height = 1200, 600
window = None
points, polygons = [], []
actualColor = (0,0,0)
to_draw_color_peaker, to_change_color_all, to_wait_change_color_all, to_move_verticle, to_select_verticle = False, False, False, False, False
selectedVerticle, selectedPolygon = None, []
newX , newY = None, None


def prepare_display():
    glViewport(0, 0, width, height)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)

def draw_left_sidebur():
    glBegin(GL_QUAD_STRIP)
    glColor(*actualColor)
    glVertex2f(0, height - 0)
    glVertex2f(50, height - 0)
    glVertex2f(0, height - 50)
    glVertex2f(50, height - 50)
    glEnd()
    glBegin(GL_QUAD_STRIP)
    glColor(1,1,0)
    glVertex2f(15, height - 50 - 15)
    glVertex2f(35, height - 50 - 15)
    glVertex2f(15, height - 50 - 35)
    glVertex2f(35, height - 50 - 35)
    glEnd()
    glBegin(GL_QUAD_STRIP)
    glColor(1,0,1)
    glVertex2f(15, height - 100 - 15)
    glVertex2f(35, height - 100 - 15)
    glVertex2f(15, height - 100 - 35)
    glVertex2f(35, height - 100 - 35)
    glEnd()

def draw_color_peaker(x,y):
    glBegin(GL_QUAD_STRIP)
    glColor(0,0,0)
    glVertex2f(x + 0, y + 0 )
    glVertex2f(x + 50, y + 0)
    glVertex2f(x + 0, y + 50)
    glVertex2f(x + 50, y + 50)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor(1,0,0)
    glVertex2f(x + 0, y + 0)
    glVertex2f(x - 50, y + 0)
    glVertex2f(x - 0, y - 50)
    glVertex2f(x - 50, y -50)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor(0,1,0)
    glVertex2f(x +0, y - 0)
    glVertex2f(x +50, y - 0)
    glVertex2f(x +0, y - 50)
    glVertex2f(x +50, y - 50)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor(0,0,1)
    glVertex2f(x - 0, y - 0)
    glVertex2f(x - 50, y - 0)
    glVertex2f(x - 0, y + 50)
    glVertex2f(x - 50, y + 50)
    glEnd()




def draw():
    global polygons, points, to_draw_color_peaker, to_change_color_all, to_move_verticle, to_select_verticle, selectedVerticle, newX, newY, selectedPolygon

    draw_left_sidebur()
    
    if to_draw_color_peaker:
        draw_color_peaker(*to_draw_color_peaker)



    if (len(points) > 0) :
        glPointSize(5)
        glColor3f(0, 0, 0)
        glBegin(GL_POINTS)

        for point in points:
            glVertex2f(*point)
        glEnd()

    if (to_move_verticle):
        for polygon in polygons:
            polPoints, polColor = polygon["points"], polygon["color"]
            
            if (len(selectedPolygon) and polygon not in selectedPolygon):
                continue
            
            for i in range(len(polPoints)):
                glPointSize(5)
                glColor3f(0, 0, 0)
                if(selectedVerticle == polPoints[i] and newX and newY):
                    polPoints[i] = (newX, newY)
                    selectedVerticle = (newX, newY)
                    glPointSize(10)
                    glColor3f(1, 0, 0)
                elif selectedVerticle == polPoints[i]:
                    glPointSize(10)
                    glColor3f(1, 0, 0)
                elif (to_select_verticle):
                    x, y = to_select_verticle
                    pX, pY = polPoints[i]
                    if (abs(x-pX) < 5 and abs(y-pY) < 5):
                        newX, newY = None, None
                        selectedVerticle = polPoints[i]
                        to_select_verticle = None
                        glPointSize(10)
                        glColor3f(1, 0, 0)

                glBegin(GL_POINTS)
                glVertex2f(*polPoints[i]) 
                glEnd()

    if (len(polygons) > 0) :
        for polygon in polygons:
            polPoints, polColor = polygon["points"], polygon["color"]
            glLineWidth(2)
            if to_change_color_all and ((len(selectedPolygon) and  polygon in selectedPolygon) or not len(selectedPolygon)):
                polygon["color"] = to_change_color_all
                glColor3f(*to_change_color_all)
            else:
                glColor3f(*polColor)
            glBegin(GL_POLYGON)
            for point in polPoints:
                glVertex2f(*point)
            glEnd()
        to_change_color_all = None

    
            
        






def display_func():
    prepare_display()
    draw()
    glFlush()


def mouse_func(btn, state, x, y):
    global to_draw_color_peaker, actualColor, to_change_color_all, to_wait_change_color_all, height, to_move_verticle, to_select_verticle, selectedPolygon

    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        

        if to_wait_change_color_all and to_draw_color_peaker:
            centerX, centerY = to_draw_color_peaker
            if x > centerX + 0 and x < centerX + 50 and height - y > centerY + 0 and height - y < centerY + 50:
                to_change_color_all = (0,0,0)
            elif x < centerX - 0 and x > centerX - 50 and height - y < centerY - 0 and height - y > centerY - 50:
                to_change_color_all = (1,0,0)
            elif x > centerX + 0 and x < centerX + 50 and height - y < centerY - 0 and height - y > centerY - 50:
                to_change_color_all = (0,1,0)
            elif x < centerX - 0 and x > centerX - 50 and height - y > centerY + 0 and height - y < centerY + 50:
                to_change_color_all = (0,0,1)
            
            if to_change_color_all:
                to_wait_change_color_all = False

            to_draw_color_peaker = None
        elif to_move_verticle:
            to_select_verticle = (x, height - y)
        
        if x > 0 and x < 50 and y > 50 + 0 and y < 50 + 50:
            to_draw_color_peaker = (150, height - 150)
            to_wait_change_color_all = True
        elif x > 0 and x < 50 and y > 100 + 0 and y < 100 + 50:
            to_move_verticle = True
        else:
            for i in  range(len(polygons)):
                if (len(polygons)  and Polygon(polygons[i]["points"]).contains(Point(x,height - y))):
                    selectedPolygon.append(polygons[i])
                    to_move_verticle = True
            if not len(selectedPolygon):
                points.append((x, height - y))
                

            


    elif btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        pass

    elif btn == GLUT_MIDDLE_BUTTON  and state == GLUT_DOWN:
        to_draw_color_peaker = (x, height - y)



    elif btn == GLUT_MIDDLE_BUTTON  and state == GLUT_UP:
        centerX, centerY = to_draw_color_peaker
        if x > centerX + 0 and x < centerX + 50 and height - y > centerY + 0 and height - y < centerY + 50:
            actualColor = (0,0,0)
        elif x < centerX - 0 and x > centerX - 50 and height - y < centerY - 0 and height - y > centerY - 50:
            actualColor = (1,0,0)
        elif x > centerX + 0 and x < centerX + 50 and height - y < centerY - 0 and height - y > centerY - 50:
            actualColor = (0,1,0)
        elif x < centerX - 0 and x > centerX - 50 and height - y > centerY + 0 and height - y < centerY + 50:
            actualColor = (0,0,1)

        if to_wait_change_color_all:
            to_wait_change_color_all = False
            to_change_color_all = actualColor

        to_draw_color_peaker = None

    glutPostRedisplay()

def keyboard_func(key, x, y):
    step = 3
    global polygons, points, selectedVerticle, to_move_verticle, newX, newY, selectedPolygon
    if key == b' ': #space
        polygons.append({"points": points, "color": actualColor})
        points = []
    elif key == b'\x13': #ctrl+s
        selectedVerticle = False
        selectedPolygon = []
        to_move_verticle = False
        newX = None
        newY = None
    elif key == b'\x1a': #ctrl+z
       
        if len(selectedPolygon):
            for r in selectedPolygon:
                polygons.remove(r)
            selectedPolygon = []
        elif len(points):
            points.pop()
        else:
            polygons.pop()
    elif key == b'\x7f': #del
        polygons = []
    elif key == b'\x08': #backspace
        if len(selectedPolygon):
            for r in selectedPolygon:
                polygons.remove(r)
            selectedPolygon = []
        elif len(points):
            points.pop()
        else:
            polygons.pop()
    elif key == b'\r': #enter
        pass
    
    if selectedVerticle:
        x,y = selectedVerticle
        if key == b'w':
            newX, newY = x, y + step
        elif key == b's':
            newX, newY = x, y - step
        elif key == b'a':
            newX, newY = x - step, y
        elif key == b'd':
            newX, newY = x + step, y
    glutPostRedisplay()




def init_glut():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(50, 20)

def init_functions():
    glutDisplayFunc(display_func)
    glutMouseFunc(mouse_func)
    glutKeyboardFunc(keyboard_func)
    create_menu()

def menu(num):
    global polygons, to_change_color_all, to_move_verticle, points, selectedPolygon

    if num == 0:
        glutDestroyWindow(window)
        exit(0)
    elif num == 1:
        polygons = []
    elif num == 2:
        if len(selectedPolygon):
            for r in selectedPolygon:
                polygons.remove(r)
            selectedPolygon = []
        elif len(points):
            points.pop()
        else:
            polygons.pop()
    elif num == 3:
        to_change_color_all = (1,0,0)
    elif num == 4:
        to_change_color_all = (0,1,0)
    elif num == 5:
        to_change_color_all = (0,0,1)
    elif num == 6:
        to_move_verticle = True
    elif num == 7:
        selectedVerticle = False
        selectedPolygon = []
        to_move_verticle = False
        newX = None
        newY = None
        
    glutPostRedisplay()
    return 0

def create_menu():
    submenu_id = glutCreateMenu(menu)
    glutAddMenuEntry("Red", 3)
    glutAddMenuEntry("Green", 4)
    glutAddMenuEntry("Blue", 5)
    glutCreateMenu(menu)
    glutAddMenuEntry("Delete all", 1)
    glutAddMenuEntry("Delete last", 2)
    glutAddSubMenu("Change colour", submenu_id)
    glutAddMenuEntry("Edit", 6)
    glutAddMenuEntry("Save", 7)
    glutAddMenuEntry("Exit", 0)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def create_window():
    global window
    window = glutCreateWindow("Lab1 Oleh Zherebetskiy")

def clear_color():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)


def main():
    init_glut()
    create_window()
    clear_color()
    init_functions()

    #loop

    glutMainLoop()
    
    

if __name__ == '__main__':
    main()

