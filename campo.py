from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def desenha_linhas(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)  # aumenta a espessura dos pontos
    glBegin(GL_POINTS)
    while True:
        glVertex2i(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    glEnd()

    

