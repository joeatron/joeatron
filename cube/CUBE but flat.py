#Cube 1
#00:28 01/09/2020 
#----IMPORT AREA----
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),        #-Note (x,y,z)
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    )

edges = (
    (0,1),
    (0,3),
    (2,1),
    (2,3),
    )

#----render code----
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
#----main----
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1 , 50.0)

    glTranslate(0,0, -10)   #-Note (x,y,z)
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
           


                    
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(1)
main()
