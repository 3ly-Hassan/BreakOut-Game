from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame as pg

pg.init()
tick = pg.mixer.Sound('tick.wav')
crash = pg.mixer.Sound('crash.wav')
music = pg.mixer.music.load('remix.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(.1)

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
deltaX = 1
deltaY = 1
time_interval = 5


class BLOC:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

ball = BLOC(100, 100, 120, 120)  # initial position of the ball
border = BLOC(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
Stick = BLOC(370, 0, 470, 10)  # initial position of the bat
side1 = BLOC(0, 0, 10, 280)
side2 = BLOC(790, 0, 800, 280)
blocList = []
sidesList=[]
x = 15
y = 350
sidex=0
sidey=280
for i in range(0, 156):
    if (i % 13 == 0):
        x = 15
        y += 30
    if(i%39==0):
        y+=50

    blocList.append(BLOC(x, y, x + 50, y + 20))
    x += 60
# for i in range(0, 6):
#     if(i%2==0):
#         sidesList.append(BLOC(sidex, sidey, sidex + 14, sidey + 140))
#         sidex = 787
#     else:
#         sidesList.append(BLOC(sidex, sidey, sidex + 14, sidey + 140))
#         sidex=0
#         sidey+=140

def defaultVlaues():
    global sidesList
    global blocList
    global x
    global y
    global move
    global pause
    global sidex
    global sidey
    blocList.clear()
    sidesList.clear()
    pause = True
    move=0
    x = 15
    y = 350
    # sidex = 0
    # sidey = 280
    for i in range(0, 156):
        if (i % 13 == 0):
            x = 15
            y += 30
        if (i % 39 == 0):
            y += 50
        blocList.append(BLOC(x, y, x + 50, y + 20))
        x += 60
    # for h in range(0, 6):
    #     if (h % 2 == 0):
    #         sidesList.append(BLOC(sidex, sidey, sidex + 14, sidey + 140))
    #         sidex = 787
    #     else:
    #         sidesList.append(BLOC(sidex, sidey, sidex + 14, sidey + 140))
    #         sidex = 0
    #         sidey += 140
# Initialization
def init():
    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)

def DrawRectangle(rect,r,g,b):
    glLoadIdentity()
    glColor(r,g,b)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()

def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def drawEndText(string, x, y):
    glLineWidth(2.5)
    glColor(1, 1, 1)  # white Color
    glLoadIdentity()  # remove the previous transformations
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def Test_Ball_Wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    # print(ball.right)

    if ball.right >= wall.right-14:
        return FROM_RIGHT
    if ball.left <= wall.left+14:
        return FROM_LEFT
    if ball.top >= wall.top-14:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

def Test_Ball_Player(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False

exit = False
made = -10
by = -40
ALI = -90
AYA = -160
KARIM = -230
EMAN = -300
BY = -420

def keyboard(key, x, y):
    global pause
    global Lives
    global exit
    global score
    if key == b"q":
        exit = True
    elif key == b" ":
        pause = not pause
    elif key == b"p":
        glClearColor(0, 0, 0, 1)
        exit = False
        score=0
        Lives = 3
        defaultVlaues()
mouse_x = 0
def MouseMotion(x, y):
    global mouse_x
    mouse_x = x
def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)

Lives = 3
pause = True
score= 0
move=0
def Display():
    global score
    global Lives
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global pause
    global blocList
    global made
    global by
    global ALI
    global AYA
    global KARIM
    global EMAN
    global BY
    global move
    global sidesList




    if (Lives > 0 and exit == False):
        glClear(GL_COLOR_BUFFER_BIT)


        if (pause and Lives>0):
            string = "p r e s s  s p a c e  t o  p l a y  ' Q '  t o  e x i t"
            drawText(string, 80, 150)
        DrawRectangle(BLOC(0,WINDOW_HEIGHT-14,WINDOW_WIDTH,WINDOW_HEIGHT),0,0,1)
        DrawRectangle(BLOC(0,WINDOW_HEIGHT-120,14,WINDOW_HEIGHT-10),0,0,1)
        DrawRectangle(BLOC(WINDOW_WIDTH-14,WINDOW_HEIGHT-120,WINDOW_WIDTH,WINDOW_HEIGHT-10),0,0,1)
        DrawRectangle(BLOC(0, WINDOW_HEIGHT - 240, 14, WINDOW_HEIGHT - 120), 1, 1, 1)
        DrawRectangle(BLOC(WINDOW_WIDTH-14,WINDOW_HEIGHT-240,WINDOW_WIDTH,WINDOW_HEIGHT-120),1,1,1)
        DrawRectangle(BLOC(0, WINDOW_HEIGHT - 360, 14, WINDOW_HEIGHT - 240), 1, 1, 0)
        DrawRectangle(BLOC(WINDOW_WIDTH - 14, WINDOW_HEIGHT - 360, WINDOW_WIDTH, WINDOW_HEIGHT - 240), 1, 1, 0)
        DrawRectangle(BLOC(0, WINDOW_HEIGHT - 490, 14, WINDOW_HEIGHT - 360), 1, 0, 0)
        DrawRectangle(BLOC(WINDOW_WIDTH - 14, WINDOW_HEIGHT - 490, WINDOW_WIDTH, WINDOW_HEIGHT - 360), 1, 0, 0)
        DrawRectangle(BLOC(0, 0, 14, 10), 0, 1, 0)
        DrawRectangle(BLOC(WINDOW_WIDTH - 14, 0 , WINDOW_WIDTH, 10), 0, 1, 0)
        for x in blocList:  # blocs
            r = 0
            b = 1
            g = 0
            if (x.bottom <= WINDOW_HEIGHT - 120 and x.bottom > WINDOW_HEIGHT - 240):
                r = 1
                b = 1
                g = 1
            elif (x.bottom <= WINDOW_HEIGHT - 240 and x.bottom > WINDOW_HEIGHT - 360):
                r = 1
                b = 0
                g = 1
            elif (x.bottom <= WINDOW_HEIGHT - 360 and x.bottom > WINDOW_HEIGHT - 490):
                r = 1
                b = 0
                g = 0

            DrawRectangle(x, r, g, b)

        if (pause == False):

            move += 10
            if (move % 300 == 0):
                for x in blocList:
                    x.bottom -= 1
                    x.top -= 1
                for x in sidesList:
                    x.bottom-=1
                    x.top-=1
            ball.left = ball.left + deltaX  # updating ball's coordinates
            ball.right = ball.right + deltaX
            ball.top = ball.top + deltaY
            ball.bottom = ball.bottom + deltaY
            if Test_Ball_Player(ball, Stick) == True:
                if (Stick.right - 50 < ball.left):
                    deltaY = 1
                    deltaX = 1
                else:
                    deltaY = 1
                    deltaX = -1

            if Test_Ball_Wall(ball, border) == FROM_RIGHT:
                deltaX = -1

            if Test_Ball_Wall(ball, border) == FROM_LEFT:
                deltaX = 1

            if Test_Ball_Wall(ball, border) == FROM_TOP:
                deltaY = -1

            if Test_Ball_Wall(ball, border) == FROM_BOTTOM:
                crash.set_volume(3)
                crash.play()
                deltaY = 1
                Lives = Lives - 1
            for x in blocList:
                if (x.left == 0):
                    score += 1
                    x.left = -10
                elif(x.right==-5):
                    score-=1
                    x.right=-4
                if(x.bottom==Stick.top):
                    x.bottom=-5
                    x.top=-5
                    x.left=-5
                    x.right=-5



            # s=1
            # for x in sidesList:
            #     if(s<=2):
            #         DrawRectangle(x,1,1,1)
            #     elif(s<=4):
            #         DrawRectangle(x,0,0,1)
            #     else:
            #         DrawRectangle(x,1,1,0)
            #     s+=1
        # glColor(1, 0, 0)  # red color

        for x in blocList:

            if (((ball.top == x.bottom or ball.bottom == x.top) and (
                    (ball.right >= x.left and ball.right <= x.right) or (
                    ball.left <= x.right and ball.left >= x.left))) or ((
                    (ball.right == x.left or ball.left == x.right) and (
                    (ball.top >= x.bottom and ball.top <= x.top) or (
                    ball.bottom >= x.bottom and ball.bottom <= x.top))))):
                tick.set_volume(10)
                tick.play()
                if (ball.top == x.bottom):
                    deltaY = -1
                elif (ball.right == x.left):
                    deltaX = -1
                elif (ball.left == x.right):
                    deltaX = 1
                else:
                    deltaY = 1
                x.left = 0
                x.bottom = 0
                x.top = 0
                x.right = 0

        glColor(0, 1, 0)

        DrawRectangle(ball,0,1,0)

        # print(Test_Ball_Wall(ball,wall))


        Stick.left = mouse_x - 50
        Stick.right = mouse_x + 50
        if Stick.left <= 14:
            Stick.left = 14
            Stick.right = 114
        if Stick.right >= WINDOW_WIDTH-14:
            Stick.right = WINDOW_WIDTH-14
            Stick.left = WINDOW_WIDTH - 114
        DrawRectangle(Stick,0,1,0)

        string = "Lives : " + str(Lives)
        drawText(string, 700, 20)
        string = "Score : " + str(score)
        drawText(string, 700, 50)
        glutSwapBuffers()
        i=0
        for x in blocList:
            if(x.left>0):
                i+=1;
        if(i==0):
            glClearColor(0, 1, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            string = "p r e s s  ' P '  t o  p l a y  a g a i n "
            drawText(string, 200, 200)
            string = "N i c e  W O R K "
            drawText(string, 320, 300)
            glutSwapBuffers()
    elif (Lives == 0 and exit == False):
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        string = "p r e s s  ' P '  t o  p l a y  a g a i n "
        drawText(string, 200, 200)
        string = "G A M E  O V E R "
        drawText(string, 320, 300)
        glutSwapBuffers()


    else:
        if (BY < 500):
            glClearColor(0, 0, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            string = "M a d e  W i t h  L o v e  "
            drawEndText(string, 250, made)
            string = "B Y "
            drawEndText(string, 380, by)
            string = "A L I  H A S S A N "
            drawEndText(string, 290, ALI)
            string = "A Y A  M O H A M E D "
            drawEndText(string, 290, AYA)
            string = "K A R I M  A H M E D "
            drawEndText(string, 290, KARIM)
            string = "E M A N  F A R I E D "
            drawEndText(string, 290, EMAN)
            string = "G O O D  B Y "
            drawEndText(string, 350, BY)
            made += 1
            by += 1
            ALI += 1
            AYA += 1
            KARIM += 1
            EMAN += 1
            BY += 1

            glutSwapBuffers()
        else:
            sys.exit(0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"BreakOut Game ")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
