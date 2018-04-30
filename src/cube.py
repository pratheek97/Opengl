from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

VOID, CLEAR,ADD_PLANE, REMOVE_PLANE,COLOR, MOTION_ON, MOTION_OFF, QUIT = list(range(8))
VOID, RED, GREEN,BLUE =list(range(4))

PROMPT = ("Press keys '1' - '0' to start callbacks",
          "Press ESCAPE to exit.")

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set background color to black and opaque
    glClearDepth(1.0)  # Set background depth to farthest
    glEnable(GL_DEPTH_TEST)

def square():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    w = float(glutGet(GLUT_WINDOW_WIDTH))
    h = float(glutGet(GLUT_WINDOW_HEIGHT))
    y = 25.0
    for s in PROMPT:
        glRasterPos(40.0, y)
        y += 30.0
        for c in s:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0,0.0,-20.0)#View changes of the cube can be done here
    #glRotate(-90.0,0.0,1.0,0.0)
    glBegin(GL_QUADS)
    #TOP
    glColor3f(0.0,1.0,0.0)# Green
    glVertex3f(1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,-1.0)
    glVertex3f(-1.0,1.0,1.0)
    glVertex3f(1.0,1.0,1.0)

    #BOTTOM
    glColor3f(1.0, 0.0, 0.0)  # RED
    glVertex3f(1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(1.0,-1.0,-1.0)

    #FRONT
    glColor3f(0.0, 0.0, 1.0)  # BLUE
    glVertex3f(1.0, 1.0,1.0)
    glVertex3f(-1.0, 1.0,1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(1.0,-1.0,1.0)

    #BACK
    glColor3f(1.0,0.5, 0.0)  # ORANGE
    glVertex3f(1.0,-1.0, -1.0)
    glVertex3f(-1.0,-1.0, -1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(1.0, 1.0,-1.0)

    #LEFT
    glColor3f(1.0, 1.0, 0.0)  #YELLOW
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    #RIGHT
    glColor3f(1.0, 1.0, 1.0)  # Green
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0,-1.0, 1.0)
    glVertex3f(1.0,-1.0,-1.0)

    glEnd()
    glutSwapBuffers()

def add_plane():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-4.0, 0.0, -20.0)  # View changes of the cube can be done here
    # glRotate(-90.0,0.0,1.0,0.0)
    glBegin(GL_QUADS)
    # TOP
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # BOTTOM
    glColor3f(1.0, 0.0, 0.0)  # RED
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # FRONT
    glColor3f(0.0, 0.0, 1.0)  # BLUE
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # BACK
    glColor3f(1.0, 0.5, 0.0)  # ORANGE
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    # LEFT
    glColor3f(1.0, 1.0, 0.0)  # YELLOW
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # RIGHT
    glColor3f(1.0, 1.0, 1.0)  # Green
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()


    return

def createmenu():
    submenuid = glutCreateMenu(color)
    glutAddMenuEntry("Red", RED)
    glutAddMenuEntry("Blue", BLUE)
    glutAddMenuEntry("Green", GREEN)

    menu_id = glutCreateMenu(menu)
    glutAddMenuEntry("Clear",CLEAR)
    glutAddMenuEntry("Add Cube", ADD_PLANE)
    glutAddMenuEntry("Remove plane", REMOVE_PLANE)
    glutAddSubMenu("Background", submenuid)
    glutAddMenuEntry("Motion", MOTION_ON)
    glutAddMenuEntry("Quit", QUIT)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


def remove_plane():
    return 0

def domotion_on():
    return 0

def domotion_off():
    return 0

def doquit():
    sys.exit(0)
    return

def color(item):
    colordict[item]()
    return 0

def clear():
    return

def red():
    glClearColor(1,0,0,1)
    glutPostRedisplay()
    return

def blue():
    glClearColor(0,0,1,1)
    glutPostRedisplay()
    return

def green():
    glClearColor(0,1,0,1)
    glutPostRedisplay()
    return

colordict={RED:red,
           GREEN:green,
           BLUE:blue}

menudict = {CLEAR:clear,
            ADD_PLANE: add_plane,
            REMOVE_PLANE: remove_plane,
            COLOR:color,
            MOTION_ON: domotion_on,
            MOTION_OFF: domotion_off,
            QUIT: doquit}


def reshape(w,h):
    if(h==0):
        h=1
    aspect=w/h
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,aspect,0.1,100.0)

def menu(item):
    menudict[item]()
    return 0

if __name__=="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowPosition(50,100)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b'Square')
    glutDisplayFunc(square)
    glutReshapeFunc(reshape)
    createmenu()
    init()
    glutMainLoop()
