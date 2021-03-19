from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sqrt

colors = {
    (0, 0, 0): [(1, 1), (1, 50), (50, 1), (50, 50)],
    (1, 0, 0): [(1, 52), (1, 102), (50, 52), (50, 102)],
    (0, 1, 0): [(1, 104), (1, 154), (50, 104), (50, 154)],
    (0, 0, 1): [(1, 156), (1, 206), (50, 156), (50, 206)],
    (.5, .5, .5): [(1, 208), (1, 258), (50, 208), (50, 258)],
    (0.1, 0.5, 0.7): [(1, 260), (1, 310), (50, 260), (50, 310)],
    (0.3, 0, 0.3): [(1, 312), (1, 362), (50, 312), (50, 362)],
}

width, height = 800, 500
check, draw_points = False, False
window, value = None, 0
shapes, temp, points = [], [], []
hovered, color_chosen, shape_chosen, vertex_chosen = None, None, None, None
draw_mode = True


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def mouse(button, state, mouse_x, mouse_y):
    global check, temp, points, draw_points, shape_chosen, color_chosen, draw_mode
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 1 <= mouse_x <= 50:
            if 1 <= height - mouse_y <= 50:
                color_chosen = (0, 0, 0)
            elif 52 <= height - mouse_y <= 102:
                color_chosen = (1, 0, 0)
            elif 104 <= height - mouse_y <= 154:
                color_chosen = (0, 1, 0)
            elif 156 <= height - mouse_y <= 206:
                color_chosen = (0, 0, 1)
            elif 208 <= height - mouse_y <= 258:
                color_chosen = (.5, .5, .5)
            elif 260 <= height - mouse_y <= 310:
                color_chosen = (0.1, 0.5, 0.7)
            elif 312 <= height - mouse_y <= 362:
                color_chosen = (0.3, 0, 0.3)
            else:
                color_chosen = None

            if color_chosen:
                if shape_chosen:
                    for i in shapes:
                        if i[0] == shape_chosen:
                            i[1] = color_chosen
                            break
                else:
                    for i in shapes:
                        i[1] = color_chosen
        else:
            if color_chosen:
                if shape_chosen:
                    for i in shapes:
                        if i[0] == shape_chosen:
                            i[1] = color_chosen
                            break
                else:
                    for i in shapes:
                        i[1] = color_chosen

            if hovered:
                shape_chosen = hovered
                for i in shapes:
                    i[2] = 5
                    if i[0] == shape_chosen:
                        i[2] = 10
                check = True
                glutPostRedisplay()
                return
            else:
                for i in shapes:
                    i[2] = 5
                shape_chosen = None

            if draw_mode:
                x = mouse_x
                y = height - mouse_y
                temp.append([x, y])
                points.append((x, y))
                draw_points = True

            check = True
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        pass
    glutPostRedisplay()


def keyboard(key, x, y):
    global shape_chosen, check, temp, points, draw_points
    if key == b'\x1a':
        try:
            shapes.pop()
            global check
            check = True
        except IndexError:
            print('no items to delete')
        glutPostRedisplay()
    elif key in (b'q', b'\xe9'):
        global draw_mode

        draw_mode = not draw_mode
        print('mode switched to ', draw_mode)
    elif key == b'\x7f' and shape_chosen:
        for i in shapes:
            if i[0] == shape_chosen:
                shapes.remove(i)
                break
        shape_chosen = None
        glutPostRedisplay()
    elif key == b'\r':
        shapes.append([temp, color_chosen if color_chosen else (0, 0, 0), 5])
        temp, points = [], []
        check = True
        draw_points = False
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


def menu_actions(num):
    global shape_chosen
    if num == 1:
        for i in shapes:
            if i[0] == shape_chosen:
                shapes.remove(i)
                break
        shape_chosen = None
    elif num == 2:
        try:
            shapes.pop()
            global check
            check = True
        except IndexError:
            print('no items to delete')
    elif num == 6:
        shapes.clear()
        points.clear()
    elif num == 3:
        if shape_chosen:
            for i in shapes:
                if i[0] == shape_chosen:
                    i[1] = (1, 0, 0)
                    break
        else:
            for i in shapes:
                i[1] = (1, 0, 0)
    elif num == 4:
        if shape_chosen:
            for i in shapes:
                if i[0] == shape_chosen:
                    i[1] = (0, 1, 0)
                    break
        else:
            for i in shapes:
                i[1] = (0, 1, 0)
    elif num == 5:
        if shape_chosen:
            for i in shapes:
                if i[0] == shape_chosen:
                    i[1] = (0, 0, 1)
                    break
        else:
            for i in shapes:
                i[1] = (0, 0, 1)
    global value
    value = None
    glutPostRedisplay()


def create_menu():
    submenu_id = glutCreateMenu(menu)
    glutAddMenuEntry("Red", 3)
    glutAddMenuEntry("Green", 4)
    glutAddMenuEntry("Blue", 5)
    glutCreateMenu(menu)
    glutAddMenuEntry("Delete", 1)
    glutAddMenuEntry("Delete last", 2)
    glutAddMenuEntry("Clear", 6)
    glutAddSubMenu("Paint", submenu_id)
    glutAddMenuEntry("Quit", 0)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


def draw_point():
    glPointSize(2)
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    for i in points:
        glVertex2f(*i)
    glEnd()


def draw_shapes():
    global check
    check = False
    for shape in shapes:
        glLineWidth(shape[2])
        glColor3f(*shape[1])
        glBegin(GL_LINE_LOOP)
        for coords in shape[0]:
            glVertex2f(*coords)
        glEnd()


def display():
    if value != 0:
        menu_actions(value)

    glViewport(0, 0, width, height)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, width, 0.0, height)

    for i, j in colors.items():
        color_menu(i, j)

    if draw_points:
        draw_point()

    draw_shapes()

    glFlush()


def mouse_move(x, y):
    y = height - y
    global hovered, vertex_chosen
    for pts in shapes:
        for pt in pts[0]:
            if sqrt((x - pt[0]) ** 2 + (y - pt[1]) ** 2) < 10:
                hovered = pts[0]
                vertex_chosen = pt
                return
    hovered = None
    vertex_chosen = None


def resize(key, x, y, step=3):
    if shape_chosen:
        for i in range(len(shapes)):
            if shapes[i][0] == shape_chosen:
                for j in range(len(shapes[i][0])):
                    if shapes[i][0][j] == vertex_chosen:
                        if key == GLUT_KEY_UP:
                            shapes[i][0][j][1] += step
                        elif key == GLUT_KEY_DOWN:
                            shapes[i][0][j][1] += -step
                        elif key == GLUT_KEY_LEFT:
                            shapes[i][0][j][0] += -step
                        elif key == GLUT_KEY_RIGHT:
                            shapes[i][0][j][0] += step
                        glutPostRedisplay()


def color_menu(color, coords):
    glBegin(GL_QUAD_STRIP)
    glColor(*color)
    for i in coords:
        glVertex2f(*i)
    glEnd()
    if color == color_chosen:
        glBegin(GL_LINE_LOOP)
        glColor(0, 0, 0)
        for i in coords:
            glVertex2f(*i)
        glEnd()


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
    window = glutCreateWindow("Plot Line Loops")

    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    init()
    create_menu()
    glutReshapeFunc(reshape_window)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_move)
    glutSpecialFunc(resize)
    glutMainLoop()


if __name__ == '__main__':
    main()
