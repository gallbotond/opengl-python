import math
import numpy as np

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():
    glColor3f(0, .5, 0)
    glBegin(GL_POLYGON)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    glColor3f(0, .5, 1)
    glBegin(GL_LINE_LOOP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()
    # for i in np.arange(0, len(points) - 2, 3):
    #     glBegin(GL_LINE_STRIP)
    #     glVertex2f(points[i][0], points[i][1])
    #     glVertex2f(points[i+1][0], points[i+1][1])
    #     glVertex2f(points[i+2][0], points[i+2][1])
    #     glEnd()


done = False
init_ortho()
points = []
glLineWidth(3)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, p[0], ortho_left, ortho_right),
                           map_value(0, screen_height, p[1], ortho_bottom, ortho_top)))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    pygame.display.flip()
pygame.quit()
