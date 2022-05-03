from OpenGL.GL import *
from glew_wish import *
from Modelo import *
import glfw
import math

class Enemy():

    posicion_cuadrado = [-0.4,0.9, 0.0]

    def draw_cuadrado(self):
        glPushMatrix()
        glTranslatef(self.posicion_cuadrado[0], self.posicion_cuadrado[1], 0.0)
        glBegin(GL_QUADS)

        glColor3f(0.9, 0.2, 0.21)

        glVertex3f(-0.1,0.1,0.0)
        glVertex3f(0.1,0.1,0.0)
        glVertex3f(0.1,-0.1,0.0)
        glVertex3f(-0.1,-0.1,0.0)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor(1,1,1)

        glVertex3f(-0.1,0.1,0.0)
        glVertex3f(0.1,0.1,0.0)
        glVertex3f(0.1,-0.1,0.0)
        glVertex3f(-0.1,-0.1,0.0)

        glEnd()
        glPopMatrix()
        