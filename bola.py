from math import cos, sin

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Bola:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.raio = 8
        self.vel = 10
       

    def desenhar(self):
        glColor3f(1, 1, 1)
        glBegin(GL_POLYGON)
        for i in range(360):
            ang = i * 3.14 / 180
            glVertex2f(self.x + self.raio * cos(ang), self.y + self.raio * sin(ang))
        glEnd()

    def movimentar(self, key):
        if key == 'w':
            self.y += self.vel
        elif key == 's':
            self.y -= self.vel
        elif key == 'a':
            self.x -= self.vel
        elif key == 'd':
            self.x += self.vel

    
