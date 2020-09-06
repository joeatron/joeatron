#Cube 1
#00:28 01/09/2020 
#----IMPORT AREA----
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
#----setup zone----
vertices = (        #-Note (X,Y,Z)
    (0, 0.45, 0.5),         #0
    (-0.1, 0.45, 0.5),      #1
    (-0.5, 0.45, 0.2),      #2
    (-0.5, 0, 0.2),         #3
    (-0.1, 0, 0.55),        #4
    (1, 0, 0.5),            #5
    (0, 0.45, -0.5),        #6
    (-0.1, 0.45, -0.5),     #7
    (-0.5, 0.45, -0.2),     #8
    (-0.5, 0, -0.2),        #9
    (-0.1, 0, -0.55),       #10
    (1, 0, -0.5),            #11
    )

edges = (           #-Note (Conection 1,Conection 2)
    (0,1),
    (0,5),
    (0,6),
    (1,4),
    (1,2),
    (2,8),
    (2,3),
    (3,4),
    (3,9),
    (4,5),
    (5,11),
    (6,7),
    (6,11),
    (7,8),
    (7,10),
    (8,9),
    (9,10),
    (10,11),
    )
surfaces = (            #-Note (Conection 1,Conection 2)
    (1,2,8,7),      #top 1
    (0,1,7,6),      #top 2    
    (4,3,9,10),     #bottem 1
    (5,4,10,11),    #bottem 2
    (0,6,11,5),         #ram 
    (6,7,10,11),        #lside 
    (0,1,4,5),          #rside 
    (7,8,9,10),         #lback
    (1,2,3,4),          #rback
    (2,8,9,3),          #midback
    )
colours = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,1),
    (1,1,0),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,1),
    (1,1,0),

    )


#----render code----
def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        X = 0
        for vertex in surface:
            X+=1
            glColor3fv(colours[X])
            glVertex3fv(vertices[vertex])

    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
#            glColor3fv(colours[0])
            glVertex3fv(vertices[vertex])
    glEnd()

#----main----
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1 , 50.0)

    glTranslate(0,0, -5)   #-Note (x,y,z)
    glRotatef(0, 0, 0, 0)   #-Note (angle , x , y , z)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

        keys = pygame.key.get_pressed()
        #Arrow_keys
        if keys[pygame.K_a]:
            glTranslate(-0.1,0,0)
        if keys[pygame.K_d]:
            glTranslate(0.1,0,0)
        if keys[pygame.K_w]:
            glTranslate(0,0.1,0)
        if keys[pygame.K_s]:
            glTranslate(0,-0.1,0)
        #buttons
        if keys[pygame.K_q]:
            glTranslate(0,0,0.1)
        if keys[pygame.K_e]:
            glTranslate(0,0,-0.1)
        #numpad
        if keys[pygame.K_LEFT]:
            glRotatef(1, 0, 1, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(1, 0, -1, 0)
        if keys[pygame.K_UP]:    
            glRotatef(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(1, -1, 0, 0)
        if keys[pygame.K_m]:    
            glRotatef(1, 0, 0, -1)
        if keys[pygame.K_n]:
            glRotatef(1, 0, 0, 1)
           


                    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(1)
main()
