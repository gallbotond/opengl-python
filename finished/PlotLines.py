import math
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *

pygame.init()

screen_width = 1000
screen_height = 800
ortho_left = 0
ortho_right = 4
ortho_bottom = -1
ortho_top = 1


screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom) # set the orthographic projection



def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()


done = False
mouse_down = False
init_ortho()
glPointSize(5)
lines = []
while not done:
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
            x = map_value(0, screen_width, p[0], ortho_left, ortho_right)
            y = map_value(0, screen_height, p[1], ortho_top, ortho_bottom)
            points.append((x, y))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
