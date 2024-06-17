import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(100, 50)
    glVertex2f(200, 200)
    glVertex2f(400, 100)
    glVertex2f(150, 350)
    glVertex2f(50, 500)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()