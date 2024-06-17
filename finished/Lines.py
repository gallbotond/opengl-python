import pygame
import math

import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *

pygame.init()

screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')

x_range = [0, 4]
y_range = [-1, 1]

def init_ortho():
    glMatrixMode(GL_PROJECTION) # set the matrix mode to projection
    glLoadIdentity() # load the identity matrix
    gluOrtho2D(0, ortho_width, 0, ortho_height) # set the orthographic projection

def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def plot_line():
    for line in lines:
        glBegin(GL_LINE_STRIP)
        for p in line:
            glVertex2f(p[0], p[1])
        glEnd()

done = False
mouse_down = False
points = []
lines = [points]

init_ortho()
glPointSize(5)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
            points = []
            lines.append(points)
            # print(len(lines), lines[-1])
        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            x = map_value(0, screen_width, p[0], 0, ortho_width)
            y = map_value(0, screen_height, p[1], ortho_height, 0)
            points.append((x, y))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # plot_point()
    plot_line()
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
