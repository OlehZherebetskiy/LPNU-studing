from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt, sin, cos
from PIL import Image
import numpy

width, height = 1200, 700
check, draw_points = False, False
window, value = None, 0
shapes = []
hovered, color_chosen, shape_chosen = None, None, None
draw_mode = True
active_shape = None
color_mix_mode = None
cell_size = 20
texture = None



def color_paint(color):
    BLACK = (0, 0, 0) if color_mix_mode != 'nand' else (1, 1, 1)
    WHITE = (1, 1, 1) if color_mix_mode != 'nand' else (0, 0, 0)
    YELLOW = (1, 1, 0) if color_mix_mode != 'nand' else (0, 0, 1)
    RED = (1, 0, 0) if color_mix_mode != 'nand' else (0, 1, 1)
    GREEN = (0, 1, 0) if color_mix_mode != 'nand' else (1, 0, 1)
    BLUE = (0, 0, 1) if color_mix_mode != 'nand' else (1, 1, 0)
    VIOLET = (1, 0, 1) if color_mix_mode != 'nand' else (0, 1, 0)
    GRAY = (.5, .5, .5)
    return eval(color)


class Octagon:
    def init(self, center, radius, color='BLACK', border_color='BLACK', border_size=5, corner=0.5, ):
        self.n = 8
        self.center = center
        self.radius = radius
        self.color = color
        self.border_color = border_color
        self.border_size = border_size
        self.corner = corner
        self.coords = regular_polygon(self.n, center, radius, corner)
        self.border_coords = regular_polygon(self.n, center, radius + 1, corner)
       

    def draw(self):
        
            glLineWidth(1)
            glColor3f(*color_paint(self.color))
            glBegin(GL_POLYGON)
            for i in self.coords:
                glVertex2f(*i)
            glEnd()

            if self == shape_chosen:
                glLineWidth(self.border_size * 3)
            else:
                glLineWidth(self.border_size)
            glColor3f(*color_paint(self.border_color))
            glBegin(GL_LINE_LOOP)
            for i in self.border_coords:
                glVertex2f(*i)
            glEnd()
        

    def set_border_color(self, new_color):
        self.border_color = new_color

    def set_color(self, color):
        self.color = color

    def set_radius(self, rad):
        self.radius = rad
        self.reshape()

    def set_center(self, step, axis):
        if axis == 'x':
            self.center[0] += step
        elif axis == 'y':
            self.center[1] += step
        self.reshape()

    def set_corner(self, new_corner):
        self.corner += new_corner
        self.reshape()

    def reshape(self):
        self.coords = regular_polygon(self.n, self.center, self.radius, self.corner)
        self.border_coords = regular_polygon(self.n, self.center, self.radius + 1, self.corner)




def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def regular_polygon(n, center, radius, corner):
    x0, y0 = center
    step = 360 / n
    res = []
    for i in range(n):
        x = x0 + radius * cos(((corner + i * step) % 360) * 0.0174533)
        y = y0 + radius * sin(((corner + i * step) % 360) * 0.0174533)
        res.append((x, y))
    return res


def length(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def menu_actions(num):
    global shape_chosen, color_mix_mode, texture
    if num:
        if num == 1:
            for i in shapes:
                if i == shape_chosen:
                    shapes.remove(i)
                    break
            shape_chosen = None
        elif num == 2:
            try:
                shapes.pop()
                global check
                # check = True
            except IndexError:
                print('no items to delete')
        elif num == 3:
            shapes.clear()
        elif 4 <= num <= 9:
            colors = {4: "RED", 5: 'GREEN', 6: 'BLUE', 7: 'YELLOW', 8: 'VIOLET', 9: 'GRAY'}
            if shape_chosen:
                for i in shapes:
                    if i == shape_chosen:
                        i.set_color(colors[num])
                        i.texture = False
                        break
            else:
                for i in shapes:
                    i.set_color(color_paint[num])
                    i.texture = False
        elif num == 10:
            glLogicOp(GL_AND)
            glEnable(GL_COLOR_LOGIC_OP)
            color_mix_mode = 'and'
        elif num == 11:
            glLogicOp(GL_NAND)
            glEnable(GL_COLOR_LOGIC_OP)
            color_mix_mode = 'nand'
        elif num == 12:
            glDisable(GL_COLOR_LOGIC_OP)
            color_mix_mode = None
        elif 13 <= num <= 18:
            colors = {13: "RED", 14: 'GREEN', 15: 'BLUE', 16: 'YELLOW', 17: 'VIOLET', 18: 'GRAY'}
            if shape_chosen:
                for i in shapes:
                    if i == shape_chosen:
                        i.set_border_color(colors[num])
                        break
            else:
                for i in shapes:
                    i.set_border_color(colors[num])
    
    global value
    value = None
    glutPostRedisplay()


def menu(num):
    global value
    if num == 0:
        glutDestroyWindow(window)
        exit(0)
    else:
        value = num
        glutPostRedisplay()
    return 0


def create_menu():
    submenu1_id = glutCreateMenu(menu)
    glutAddMenuEntry("Red", 4)
    glutAddMenuEntry("Green", 5)
    glutAddMenuEntry("Blue", 6)
    glutAddMenuEntry("Yellow", 7)
    glutAddMenuEntry("Violet", 8)
    glutAddMenuEntry("Gray", 9)
    submenu2_id = glutCreateMenu(menu)
    glutAddMenuEntry("AND", 10)
    glutAddMenuEntry("NOT AND", 11)
    glutAddMenuEntry("Disable", 12)
    submenu3_id = glutCreateMenu(menu)
    glutAddMenuEntry("Red", 13)
    glutAddMenuEntry("Green", 14)
    glutAddMenuEntry("Blue", 15)
    glutAddMenuEntry("Yellow", 16)
    glutAddMenuEntry("Violet", 17)
    glutAddMenuEntry("Gray", 18)
    glutCreateMenu(menu)
    glutAddMenuEntry("Delete", 1)
    glutAddMenuEntry("Delete last", 2)
    glutAddMenuEntry("Clear", 3)
    glutAddSubMenu("Paint Shape", submenu1_id)
    glutAddSubMenu("Mix colors", submenu2_id)
    glutAddSubMenu("Paint Border", submenu3_id)
    glutAddMenuEntry("Quit", 0)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


def mouse_move(x, y):
    if active_shape:
        x = x
        y = height - y
        l = length((x, y), active_shape.center)
        active_shape.set_radius(l)
        glutPostRedisplay()
    elif shape_chosen:
        index = shapes.index(shape_chosen)
        x = x
        y = height - y
        l = length((x, y), shapes[index].center)
        shapes[index].set_radius(l)
        glutPostRedisplay()


def passive_mouse_move(x, y):
    y = height - y
    global hovered
    for i in shapes:
        for j in i.coords:
            if sqrt((x - j[0]) ** 2 + (y - j[1]) ** 2) < 10:
                hovered = i
                return
    hovered = None


def mouse(button, state, x, y):
    global check, shape_chosen, color_chosen, draw_mode, active_shape, cell_size
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x = x
        y = height - y
        if hovered:
            shape_chosen = hovered
        else:
            if shape_type == 8:
                if not shape_chosen and draw_mode:
                    active_shape = Octagon([x, y], 0)
            
            shape_chosen = None
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if active_shape and draw_mode:
            shapes.append(active_shape)
            active_shape = None
    elif button == 3:
        cell_size += 1
    elif button == 4:
        cell_size -= 1 if cell_size > 0 else 0
    glutPostRedisplay()


def keyboard(key, x, y):
    print(key)
    global shape_chosen, check, draw_points, shape_type
    if key == b'\x1a':
        try:
            shapes.pop()
            global check
            # check = True
        except IndexError:
            print('no items to delete')
    elif key in (b'q', b'\xe9'):
        global draw_mode
        draw_mode = not draw_mode
        print('mode switched to ', draw_mode)
    elif key in (b'-', b'+'):
        if shape_chosen:
            corner_val = key.decode() + str(5)
            index = shapes.index(shape_chosen)
            shapes[index].set_corner(eval(corner_val))
   
    glutPostRedisplay()


def keyboard_arrows(key, x, y, step=5):
    if shape_chosen:
        index = shapes.index(shape_chosen)
        if key == GLUT_KEY_UP:
            shapes[index].set_center(step, 'y')
        elif key == GLUT_KEY_DOWN:
            shapes[index].set_center(-step, 'y')
        elif key == GLUT_KEY_LEFT:
            shapes[index].set_center(-step, 'x')
        elif key == GLUT_KEY_RIGHT:
            shapes[index].set_center(step, 'x')
        glutPostRedisplay()


def grid():
    if cell_size > 0:
        glLineWidth(1)
        glColor3f(*color_paint('BLACK'))
        glBegin(GL_LINES)
        for i in range(1, width, cell_size):
            glVertex2f(i, 0)
            glVertex2f(i, height)
        for i in range(1, height, cell_size):
            glVertex2f(0, i)
            glVertex2f(width, i)
        glEnd()


def display():
    if value != 0:
        menu_actions(value)

    glViewport(0, 0, width, height)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)

    grid()

    for i in shapes:
        i.draw()

    if active_shape:
        active_shape.draw()

    glFlush()


def reshape_window(width_new, height_new):
    global height, width
    height, width = height_new, width_new
    glutPostRedisplay()


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(220, 50)
    window = glutCreateWindow("Paint for poor people")

    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    init()
    create_menu()
    glutReshapeFunc(reshape_window)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutMotionFunc(mouse_move)
    glutPassiveMotionFunc(passive_mouse_move)
    glutSpecialFunc(keyboard_arrows)
    glutMainLoop()


if __name__ == '__main__':
    main()