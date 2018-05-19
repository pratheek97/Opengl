from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
from random import *
from math import *

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
ccount=0
select = 0
pselect=0
count = 0
pcount=0
M_PI = pi
M_PI_2 = pi / 2.0
MAX = 7

moving = GL_FALSE

VOID, CLEAR, ADD_PLANE, REMOVE_PLANE, SHAPES, MOTION_ON, MOTION_OFF, QUIT = list(range(8))
VOID , CUBE, PLANES = list(range(3))
VOID , RED, GREEN, BLUE = list(range(4))
BACKGROUND,NOBACKGROUND=list(range(2))

class cube(object):
    def __init__(self, speed, red, green, blue, theta, x, y, z, angle):
        self.speed = speed
        self.red = red
        self.green = green
        self.blue = blue
        self.theta = theta
        self.angle = angle
        self.x = x
        self.y = y
        self.z = z


class plane(object):
    def __init__(self, speed, red, green, blue, theta, x, y, z, angle):
        self.speed = speed
        self.red = red
        self.green = green
        self.blue = blue
        self.theta = theta
        self.angle = angle
        self.x = x
        self.y = y
        self.z = z


rgblist = [(1.0, 0.0, 0.0),  # red
           (1.0, 1.0, 1.0),  # white
           (0.0, 1.0, 0.0),  # green
           (1.0, 0.0, 1.0),  # magenta
           (1.0, 1.0, 0.0),  # yellow
           (0.0, 1.0, 1.0)  # cyan
           ]

cubes = []
for n in range(MAX):
    c = cube(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    cubes.append(c)

planes = []
for n in range(MAX):
    p = plane(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    planes.append(p)


def cplane():
    global select,pselect,ccount
    for n in range(MAX):
        if planes[n].speed != 0.0 and select==2:
            glPushMatrix()
            glTranslatef(planes[n].x, planes[n].y, planes[n].z)
            glRotatef(290.0, 1.0, 0.0, 0.0)
            glRotatef(planes[n].angle, 0.0, 0.0, 1.0)
            glScalef(1.0 / 3.0, 1.0 / 4.0, 1.0 / 4.0)
            glTranslatef(0.0, -4.0, -1.5)
            if pselect==0:
                glBegin(GL_TRIANGLE_STRIP)
                # left wing
                glVertex3f(-7.0, 0.0, 2.0)
                glVertex3f(-1.0, 0.0, 3.0)
                red = planes[n].red
                green = planes[n].green
                blue = planes[n].blue
                glColor3f(red, green, blue)
                glVertex3f(-1.0, 7.0, 3.0)
                # left side
                glColor3f(0.6 * red, 0.6 * green, 0.6 * blue)
                glVertex3f(0.0, 0.0, 0.0)
                glVertex3f(0.0, 8.0, 0.0)
                # right side
                glVertex3f(1.0, 0.0, 3.0)
                glVertex3f(1.0, 7.0, 3.0)
                # final tip of right wing */
                glColor3f(red, green, blue)
                glVertex3f(7.0, 0.0, 2.0)
                glEnd()

            elif pselect == 1:
                glBegin(GL_LINE_LOOP)
                # left wing
                glVertex3f(-7.0, 0.0, 2.0)
                glVertex3f(-1.0, 0.0, 3.0)
                red = planes[n].red
                green = planes[n].green
                blue = planes[n].blue
                glColor3f(red, green, blue)
                glVertex3f(-1.0, 7.0, 3.0)
                # left side
                glColor3f(0.6 * red, 0.6 * green, 0.6 * blue)
                glVertex3f(0.0, 0.0, 0.0)
                glVertex3f(0.0, 8.0, 0.0)
                # right side
                glVertex3f(1.0, 0.0, 3.0)
                glVertex3f(1.0, 7.0, 3.0)
                # final tip of right wing */
                glColor3f(red, green, blue)
                glVertex3f(7.0, 0.0, 2.0)
                glEnd()
            glPopMatrix()


def ccube():
    global X_AXIS, Y_AXIS, Z_AXIS,ccount,pselect,gl

    for n in range(MAX):

        if cubes[n].speed != 0:

            glPushMatrix()
            glTranslate(0.0, (n * 2.5) + (-11.0), -15.0)
            glRotatef(X_AXIS, 1.0, 0.0, 0.0)
            glRotatef(Y_AXIS, 0.0, 1.0, 0.0)
            glRotatef(Z_AXIS, 0.0, 0.0, 1.0)
            glScalef(1.0, 1.0, 1.0)
            if pselect==0:
                glBegin(GL_QUADS)
                red = cubes[n].red
                green = cubes[n].green
                blue = cubes[n].blue

                glColor3f(red, green, blue)
                glVertex3f(1.0, 1.0, -1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(1.0, 1.0, 1.0)

                glColor3f(red, 0, blue)
                glVertex3f(1.0, -1.0, 1.0)
                glVertex3f(-1.0, -1.0, 1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(1.0, -1.0, -1.0)

                glColor3f(red, green, 0)
                glVertex3f(1.0, 1.0, 1.0)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(-1.0, -1.0, 1.0)
                glVertex3f(1.0, -1.0, 1.0)

                glColor3f(0, green, blue)
                glVertex3f(1.0, -1.0, -1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(1.0, 1.0, -1.0)

                glColor3f(red, green, blue)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(-1.0, -1.0, 1.0)

                glColor3f(0, 0, blue)
                glVertex3f(1.0, 1.0, -1.0)
                glVertex3f(1.0, 1.0, 1.0)
                glVertex3f(1.0, -1.0, 1.0)
                glVertex3f(1.0, -1.0, -1.0)

                glEnd()
            elif pselect==1:
                glBegin(GL_LINE_LOOP)
                red = cubes[n].red
                green = cubes[n].green
                blue = cubes[n].blue

                glColor3f(red, green, blue)
                glVertex3f(1.0, 1.0, -1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(1.0, 1.0, 1.0)

                glColor3f(red, 0, blue)
                glVertex3f(1.0, -1.0, 1.0)
                glVertex3f(-1.0, -1.0, 1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(1.0, -1.0, -1.0)

                glColor3f(red, green, 0)
                glVertex3f(1.0, 1.0, 1.0)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(-1.0, -1.0, 1.0)
                glVertex3f(1.0, -1.0, 1.0)

                glColor3f(0, green, blue)
                glVertex3f(1.0, -1.0, -1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(1.0, 1.0, -1.0)

                glColor3f(red, green, blue)
                glVertex3f(-1.0, 1.0, 1.0)
                glVertex3f(-1.0, 1.0, -1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glVertex3f(-1.0, -1.0, 1.0)

                glColor3f(0, 0, blue)
                glVertex3f(1.0, 1.0, -1.0)
                glVertex3f(1.0, 1.0, 1.0)
                glVertex3f(1.0, -1.0, 1.0)
                glVertex3f(1.0, -1.0, -1.0)

                glEnd()
            X_AXIS = X_AXIS - 0.05
            Z_AXIS = Z_AXIS - 0.05
            glPopMatrix()




def display():
    global cselect,select,ccount
    glClear(GL_DEPTH_BUFFER_BIT)
    glDisable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-20.0, 20.0, -19.0)
    glVertex3f(20.0, 20.0, -19.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(20.0, -20.0, -19.0)
    glVertex3f(-20.0, -20.0, -19.0)
    glEnd()
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    if select == 1:
        ccube()

    elif select == 2:
        cplane()
    glFlush()
    glutSwapBuffers()


def tick_per_cube(i):
    cubes[i].z = -15.0
    cubes[i].x = 0.0
    cubes[i].y = (i * 2.5) + (-10.0)
    return


def tick_per_plane(i):
    planes[i].theta += planes[i].speed
    theta = planes[i].theta
    planes[i].z = -10 + 4 * cos(theta)
    planes[i].x = 5 * sin(2 * theta)
    planes[i].y = sin(theta / 3.4) * 3
    planes[i].angle = ((atan(2.0) + M_PI_2) * sin(theta) - M_PI_2) * 180 / M_PI
    if (planes[i].speed < 0.0):
        planes[i].angle += 45.0
    return


def add_cube():
    global select, count
    for i in range(MAX):
        if (cubes[i].speed == 0.0 and select == 1):
            cubes[i].red, cubes[i].green, cubes[i].blue = choice(rgblist)
            cubes[i].speed = -0.001
            if (getrandbits(32) & 0x1):
                cubes[i].speed *= -1
            cubes[i].theta = float(randint(0, 256)) * 0.1111
            tick_per_cube(i)
            if (not moving):
                glutPostRedisplay()
            return
    return


def add_plane():
    global select
    for i in range(MAX):
        if planes[i].speed == 0.0 and select == 2:
            planes[i].red, planes[i].green, planes[i].blue = choice(rgblist)
            planes[i].speed = (float(randint(0, 0))) - 0.001
            if (getrandbits(32) & 0x1):
                planes[i].speed *= -1
            planes[i].theta = float(randint(0, 256))
            tick_per_plane(i)
            if (not moving):
                glutPostRedisplay()
            return
    return


def remove_cube():
    for i in range(MAX - 1, -1, -1):
        if cubes[i].speed != 0 and select == 1:
            cubes[i].speed = 0
            if (not moving):
                glutPostRedisplay()
            return
    return


def remove_plane():
    global select
    for i in range(MAX - 1, -1, -1):
        if (planes[i].speed != 0 and select == 2):
            planes[i].speed = 0
            if (not moving):
                glutPostRedisplay()
            return
    return


def tick():
    for i in range(MAX):
        if (planes[i].speed != 0.0):
            tick_per_plane(i)
    return


def animate():
    tick()
    glutPostRedisplay()
    return


def visible(state):
    if (state == GLUT_VISIBLE):
        if (moving):
            glutIdleFunc(animate)
    else:
        if (moving):
            glutIdleFunc(None)
    return


def motion_on():
    moving = GL_TRUE
    glutPostRedisplay()
    glutChangeToMenuEntry(4, "Motion off", MOTION_OFF)
    glutIdleFunc(animate)
    return


def motion_off():
    moving = GL_FALSE
    glutChangeToMenuEntry(4, "Motion", MOTION_ON)
    glutIdleFunc(None)
    return


def add():
    global select,ccount
    if ccount<0:
        ccount=0
    ccount+=1
    if ccount > MAX:
        ccount=MAX
        print('stack overflow')
    #print(ccount)
    if select == 1:
        add_cube()

    elif select == 2:
        add_plane()
    return

def remove():
    global select,ccount
    ccount-=1
    if ccount<=0:
        print('stack underflow')

    if select == 1:
        remove_cube()
    elif select == 2:
        remove_plane()


def clear():
    global select,ccount
    if select == 1:
        for n in range(MAX):
            remove_cube()
    elif select == 2:
        for n in range(MAX):
            remove_plane()

    select = 0
    ccount=0



def shape(item):
    global select
    shapedict[item]()
    select = item
    return select

def back(item):
    global pselect
    planedict[item]()
    pselect = item
   #print(pselect)
    return pselect

def pback():
    global pselect,gl
    if pselect==0:
        gl=GL_QUADS
    elif pselect==1:
        gl=GL_LINE_LOOP
    return

def doquit():
    sys.exit(0)


def shapes():
    global select,ccount

    select1=select
    if select==select1:
        clear()
        ccount=0
    if select == 1:
        add_cube()
    elif select == 2:
        add_plane()
    return



menudict = {CLEAR: clear,
            ADD_PLANE: add,
            REMOVE_PLANE: remove,
            MOTION_ON: motion_on,
            MOTION_OFF: motion_off,
            SHAPES: shape,
            QUIT: doquit}

shapedict = {CUBE: shapes,
             PLANES: shapes}

planedict={BACKGROUND:pback,
           NOBACKGROUND:pback}


def menu(item):
    menudict[item]()
    return 0


def createmenu():
    submenuid = glutCreateMenu(shape)
    glutAddMenuEntry("Cube", CUBE)
    glutAddMenuEntry("Planes", PLANES)

    submenuid1=glutCreateMenu(back)
    glutAddMenuEntry("No-Faces",NOBACKGROUND)
    glutAddMenuEntry("Faces",BACKGROUND)

    menu_id = glutCreateMenu(menu)
    glutAddMenuEntry("Clear", CLEAR)
    glutAddMenuEntry("Push", ADD_PLANE)
    glutAddMenuEntry("Pop", REMOVE_PLANE)
    glutAddMenuEntry("Motion", MOTION_ON)
    glutAddSubMenu("Shapes", submenuid)
    glutAddSubMenu("Faces",submenuid1)
    glutAddMenuEntry("Quit", QUIT)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


if __name__ == "__main__":
    print('--------------Stack Project--------------')
    print('Right Click Button for Menu Button option in Mouse')
    print('1.Select the Shape')
    print('2.You can Push the Object')
    print('3.You can Pop the Object')
    print('4.You can Select with Faces and Without Faces')
    print('5.Object can be kept in Motion')
    print('------------------------------------------')
    glutInit(sys.argv)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(110, 80)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutCreateWindow(b'Stack')
    glutDisplayFunc(display)
    createmenu()
    glutVisibilityFunc(visible)
    glClearDepth(2.0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 30)
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()
