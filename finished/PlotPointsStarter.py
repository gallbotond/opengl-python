import pygame
import math

import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *

pygame.init()

x_dimension = 1000
y_dimension = 800
screen_width = x_dimension / 2
screen_height = y_dimension / 2

screen = pygame.display.set_mode((x_dimension, y_dimension), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')

x_range = [0, 4]
y_range = [-1, 1]

def init_ortho():
    glMatrixMode(GL_PROJECTION) # set the matrix mode to projection
    glLoadIdentity() # load the identity matrix
    gluOrtho2D(0, 1000, 800, 0) # set the orthographic projection
    # gluOrtho2D(x_range[0], x_range[1], y_range[0], y_range[1]) # set the orthographic projection


def plot_graph():
    glBegin(GL_POINTS) # start plotting points
    px: GL_DOUBLE # declare a variable to store the x coordinate
    py: GL_DOUBLE # declare a variable to store the y coordinate
    for px in np.arange(-x_range[0], x_range[1], 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()

def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

done = False
points = []
init_ortho()
glPointSize(5)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            x = map_value(p[0], 0, x_dimension, -x_range[1], x_range[1])
            y = map_value(p[1], 0, y_dimension, y_range[1], y_range[0])
            points.append(pygame.mouse.get_pos())

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # plot_graph()
    plot_point()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
