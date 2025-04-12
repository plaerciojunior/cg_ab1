from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from bola import Bola
from campo import desenha_linhas

bola = Bola()


def desenha_campo():
    # Linhas do campo
    glColor3f(1, 1, 1)
    desenha_linhas(100, 100, 700, 100)  # linha inferior
    desenha_linhas(100, 500, 700, 500)  # linha superior
    desenha_linhas(100, 100, 100, 500)  # lateral esquerda
    desenha_linhas(700, 100, 700, 500)  # lateral direita
    desenha_linhas(400, 100, 400, 500)  # linha do meio

def desenha_area_campo():
    glColor3f(0.0, 0.6, 0.0)  # verde
    glBegin(GL_POLYGON)
    glVertex2i(100, 100)
    glVertex2i(700, 100)
    glVertex2i(700, 500)
    glVertex2i(100, 500)
    glEnd()

def desenha_areas_gol():
    # Gol da esquerda (encostado na lateral esquerda)
    desenha_linhas(100, 250, 100, 350)  # linha lateral do campo
    desenha_linhas(100, 250, 150, 250)  # topo da área
    desenha_linhas(150, 250, 150, 350)  # linha paralela
    desenha_linhas(150, 350, 100, 350)  # base da área

    # Gol da direita (encostado na lateral direita)
    desenha_linhas(700, 250, 700, 350)  # linha lateral do campo
    desenha_linhas(700, 250, 650, 250)  # topo da área
    desenha_linhas(650, 250, 650, 350)  # linha paralela
    desenha_linhas(650, 350, 700, 350)  # base da área


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    desenha_area_campo()  # primeiro o retângulo verde
    desenha_campo()       # depois as linhas brancas por cima
    desenha_areas_gol()
    bola.desenhar()
    
    glFlush()

def teclado(key, x, y):
    key = key.decode("utf-8")  # converte o byte para string
    bola.movimentar(key)  # movimenta a bola conforme a tecla pressionada
    glutPostRedisplay()  # força a atualização da tela


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)  # tamanho compatível com as coordenadas
    glutInitWindowPosition(500, 200)
    glutCreateWindow(b"Flamengo x Vasco")
    glutKeyboardFunc(teclado)

    glClearColor(0, 0, 0, 1)  # campo Preto

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
