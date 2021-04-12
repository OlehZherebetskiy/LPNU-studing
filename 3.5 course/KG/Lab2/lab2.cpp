#include <GL/glut.h>
#include <vector>
#include <iostream>
#include <math.h>
#include <stb_image.h>

using namespace std;



//Screen
GLubyte* screen;

//window
static int windowSizeX = 1200;
static int windowSizeY = 640;



//color
int red = 0;
int green = 0;
int blue = 1;

//turnOnGrid size
int m = 20;


//on/off params
int mix_color = 0; // 0- not mix, 1- xor, 2- not xor
bool sizeChanging = false;
bool angleChanging = false;
bool turnOnGrid = false;
bool lineMode = false;
bool saveMode = false;
bool moveChanging = false;
bool rastMode = false;


//main vector of figures
vector<vector<float>> figures;


//active figure
int activeFigure = 0;
bool choise_rent = false;




//help variables
struct Position
{
    Position() : x(0), y(0) {}
    float x, y;
};
Position start, finish;



// .. raster

void rastering(float r, float g, float b, int p, int k) {
    glDisable(GL_COLOR_LOGIC_OP);
    glColor3f(r / 255, g / 255, b / 255);
    glRecti(p, k, p + m, k + m);

    int sum = 255;
    int g2 = 0;
    int b2 = 150;

    int tmp = 0;
    int tmpj = 0;
    glEnable(GL_COLOR_LOGIC_OP);
    glutPostRedisplay();
}





void createFigure(float x_0, float x_1, float y_0, float y_1, int red, int green, int blue, int ang, int lineMode) {

    const double PI = 3.14159265358979323846;
    double r = sqrt(pow(max(y_0, y_1) - min(y_0, y_1), 2) + pow(max(x_0, x_1) - min(x_0, x_1), 2));
    int sides = 5;

    glColor3f(red, green, blue);
    if (lineMode == 1) 
        glBegin(GL_LINE_LOOP);
    else
        glBegin(GL_POLYGON);


    for (int i = 0; i < sides; i++) {
        double angle = (i * 2 * PI / sides) + ang;
        glVertex2d(x_0 + r * cos(angle), y_0 + r * sin(angle));
    }
    double angle = 0 * 2 * PI / sides + ang;
    glVertex2d(x_0 + r * cos(angle), y_0 + r * sin(angle));


    glEnd();
}

void drawSquare()
{
    glDisable(GL_COLOR_LOGIC_OP);
    glColor3f(1, 1, 1);

    for (size_t i = 0; i < windowSizeY; i += m)
    {
        glBegin(GL_POLYGON);

        glVertex2i(0, 0 + i);
        glVertex2i(windowSizeX, 0 + i);
        glVertex2i(windowSizeX, 1 + i);
        glVertex2i(0, 1 + i);

        glEnd();
    }

    for (size_t i = 0; i < windowSizeX; i += m)
    {
        glBegin(GL_POLYGON);

        glVertex2i(0 + i, 0);
        glVertex2i(1 + i, 0);
        glVertex2i(1 + i, windowSizeY);
        glVertex2i(0 + i, windowSizeY);

        glEnd();
    }

    glFlush();
}



//........................display


void display()
{

    vector<float> v1;
    if (mix_color == 0)
        glDisable(GL_COLOR_LOGIC_OP);
    if (mix_color != 0) {
        glEnable(GL_COLOR_LOGIC_OP);
        if (mix_color == 1)
            glLogicOp(GL_XOR);
        else if (mix_color == 2)
            glLogicOp(GL_EQUIV);
    }



    glClear(GL_COLOR_BUFFER_BIT);
    glClearColor(0, 0, 0, 0);
    GLuint tex;
    glGenTextures(1, &tex);
    glBindTexture(GL_TEXTURE_2D, tex);


    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    double w = glutGet(GLUT_WINDOW_WIDTH);
    double h = glutGet(GLUT_WINDOW_HEIGHT);
    glOrtho(0, w, h, 0, -1, 1);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glPushMatrix();


    //....active painting

    v1.push_back(start.x);
    v1.push_back(finish.x);
    v1.push_back(start.y);
    v1.push_back(finish.y);
    v1.push_back(red);
    v1.push_back(green);
    v1.push_back(blue);
    v1.push_back(0);
    v1.push_back(0);




    // ... paint all figures

    if (!moveChanging && !angleChanging && !sizeChanging)
        createFigure(v1[0], v1[1], v1[2], v1[3], v1[4], v1[5], v1[6], v1[7], v1[8]);
    if (figures.size() != 0)
    {
        for (int i = 0; i < figures.size(); i++) {
            createFigure(figures[i][0], figures[i][1], figures[i][2], figures[i][3], figures[i][4], figures[i][5], figures[i][6], figures[i][7], figures[i][8]);
            //cout << figures.size();
        }
    }


    //... end active painting

    if (saveMode) {
        figures.push_back(v1);
        cout << saveMode;
        saveMode = false;
    }




    //....  calculate rastr


    glPopMatrix();
    glReadPixels(0, 0, windowSizeX, windowSizeY, GL_RGB, GL_UNSIGNED_BYTE, screen);
    int tmp_x = windowSizeX;
    int tmp_y = windowSizeY;
    if (rastMode) {
        for (int i = 0; i < windowSizeX / m; i++) {
            for (int j = 0; j < windowSizeY / m; j++)
            {
                rastering(screen[((tmp_x)*tmp_y * 3 - (tmp_x - 10) * 3 + i * 3 * m) - 3 - windowSizeX * 3 * m * j],
                    screen[((tmp_x)*tmp_y * 3 - (tmp_x - 10) * 3 + i * 3 * m) - 2 - windowSizeX * 3 * m * j],
                    screen[((tmp_x)*tmp_y * 3 - (tmp_x - 10) * 3 + i * 3 * m) - 1 - windowSizeX * 3 * m * j],
                    i * m, j * m);
            }
        }
    }





    //...  show Square
    if (turnOnGrid && rastMode) {
        drawSquare();
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    }
    glutSwapBuffers();



}







void setActiveFigureRadius(int x, int y)
{
    finish.x = x;
    finish.y = y;
    glutPostRedisplay();
}

float getRadiusToFigure(float x_0, float x_1, float y_0, float y_1, int ang) {
    return sqrt(pow(max(y_0, y_1) - min(y_0, y_1), 2) + pow(max(x_0, x_1) - min(x_0, x_1), 2));
}






//.......changing

void changeAngle(int up) {

    if (choise_rent) {
        figures[activeFigure][7] += up;
        figures[activeFigure][7] += up;
    }
}

void changeSize(int el_x, int el_y, int up) {

    if (choise_rent) {
        figures[activeFigure][1] += el_x * up;
        figures[activeFigure][3] += el_y * up;
    }
}

void changeMove(int x, int y, int x_up, int y_up) {

    if (choise_rent) {
        figures[activeFigure][x] += x_up;
        figures[activeFigure][y] += x_up;
    }
}

void changeColor(int red, int green, int blue) {
    if (choise_rent)
        figures[activeFigure][4] = red;
        figures[activeFigure][5] = green;
        figures[activeFigure][6] = blue;
}









































//
//......................actions
//
//
// mouse actions

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        start.x = finish.x = x;
        start.y = finish.y = y;
        moveChanging = false;
        display();
    }
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP)
    {
        finish.x = x;
        finish.y = y;
        saveMode = true;
        display();
    }
    glutPostRedisplay();
}


//menu actions

void menu(int id) {
    int n = 0;

    switch (id)
    {
    case 1:
        changeColor(1, 1, 0);
        display();
        break;
    case 2:
        changeColor(1, 0, 0);
        display();
        break;
    case 3:
        changeColor(0, 1, 0);
        display();
        break;
    case 4:
        changeColor(0, 0, 1);
        display();
        break;
    case 14:
        changeColor(1, 0, 1);
        display();
        break;
    case 15:
        changeColor(0, 1, 1);
        display();
        break;


    case 6:
        moveChanging = false;
        break;
    case 5:
        moveChanging = true;
        break;
    case 7:
        sizeChanging = true;
        break;
    case 8:
        angleChanging = true;
        break;


    case 9:
        mix_color = 0;
        display();
        break;
    case 10:
        mix_color = 1;
        display();
        break;
    case 11:
        mix_color = 2;
        display();
        break;


    case 12:
        figures.clear();
        display();
        break;
    case 13:
        if (choise_rent)
        {
            figures.erase(figures.begin() + activeFigure);
            display();
        }
        break;
    }

}



//key actions

void keyboard(unsigned char Key, int x, int y)
{
    switch (Key)
    {
    case 'r':
        rastMode = !rastMode;
        glutPostRedisplay();
        break;
    case 'g':
        if(rastMode)
            turnOnGrid = !turnOnGrid;
        glutPostRedisplay();
        break;
    case 'w':
        if (m < 60)
            m = m + 1;
        display();
        break;
    case 's':
        if (m > 5)
            m = m - 1;
        display();
        break;
    case 'l':
        if (figures[activeFigure][8] == 0)
            figures[activeFigure][8] = 1;
        else
            figures[activeFigure][8] = 0;
        display();
        glutPostRedisplay();
        break;
    }
}

void processSpecialKeys(int key, int x, int y) {
    if (key == GLUT_KEY_F7) {
        for (int i = 0; i < figures.size(); i++) {
            float r = getRadiusToFigure(figures[i][0], figures[i][1], figures[i][2], figures[i][3], figures[i][7]);
            if ((figures[i][0] - x) * (figures[i][0] - x) + (figures[i][2] - y) * (figures[i][2] - y) <= (r * r))
            {
                printf("IN - %d", i);
                activeFigure = i;
                choise_rent = true;
            }
        }
    }
    if (key == 27) {
        activeFigure = false;
        choise_rent = false;
    }

    if (moveChanging) {
        if (key == GLUT_KEY_UP) {
            changeMove(2, 3, -10, -10);
            display();
        }
        if (key == GLUT_KEY_DOWN) {
            changeMove(2, 3, 10, 10);
            display();
        }
        if (key == GLUT_KEY_LEFT) {
            changeMove(0, 1, -10, -10);
            display();
        }
        if (key == GLUT_KEY_RIGHT) {
            changeMove(0, 1, 10, 10);
            display();
        }
    }
    if (sizeChanging) {
        int el_x = figures[activeFigure][0] > figures[activeFigure][1] ? -1 : 1;
        int el_y = figures[activeFigure][2] > figures[activeFigure][3] ? -1 : 1;
        if (key == GLUT_KEY_PAGE_UP) {
            changeSize(el_x, el_y, 5);
            display();
        }
        if (key == GLUT_KEY_PAGE_DOWN) {
            changeSize(el_x, el_y, -5);
            display();
        }
    }

    if (angleChanging) {
        if (key == GLUT_KEY_HOME) {
            changeAngle(5);
            display();
        }
        if (key == GLUT_KEY_END) {
            changeAngle(-5);
            display();
        }
    }

}






//help functions
void reshape(int width, int height)
{
    screen = new GLubyte[width * height * 3];
    windowSizeX = width;
    windowSizeY = height;
    glViewport(0, 0, (GLsizei)width, (GLsizei)height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, (GLdouble)width, (GLdouble)height, 0.0);
}




//main

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowSize(windowSizeX, windowSizeY);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("Lab2 Zherebetskiy Oleh");
    glutMouseFunc(mouse);
    glutReshapeFunc(reshape);
    glutSpecialFunc(processSpecialKeys);
    glutKeyboardFunc(keyboard);
    glutMotionFunc(setActiveFigureRadius);

    glutDisplayFunc(display);



    //add menu

    int color = glutCreateMenu(menu);
    glutAddMenuEntry("Red", 2);
    glutAddMenuEntry("Green", 3);
    glutAddMenuEntry("Blue", 4);
    glutAddMenuEntry("Yellow", 1);
    glutAddMenuEntry("Pink", 14);
    glutAddMenuEntry("Azure", 15);

    int mix = glutCreateMenu(menu);
    glutAddMenuEntry("Not Mix", 9);
    glutAddMenuEntry("Mix (XOR)", 10);
    glutAddMenuEntry("Mix (Not XOR)", 11);

    int change = glutCreateMenu(menu);
    glutAddMenuEntry("Move", 5);
    glutAddMenuEntry("Size", 7);
    glutAddMenuEntry("Angle", 8);

    int delet = glutCreateMenu(menu);
    glutAddMenuEntry("Delete all", 12);
    glutAddMenuEntry("Delete element", 13);

    int menu_id = glutCreateMenu(menu);
    glutAddSubMenu("Color", color);
    glutAddSubMenu("Mix color", mix);
    glutAddSubMenu("Change", change);
    glutAddSubMenu("Delete", delet);

    glutAttachMenu(GLUT_RIGHT_BUTTON);



    //loop

    glEnable(GL_BLEND);
    glutMainLoop();

    return 0;
}
