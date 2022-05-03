from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Nave_Enemiga(Modelo):

    herida = False

    def __init__(self):
        super().__init__()
        self.extremo_derecho = 0.1
        self.extremo_izquierdo = 0.1
        self.extremo_superior = 0.15
        self.extremo_inferior = 0.15

        

    def dibujar(self):
        glPushMatrix()
        glBegin(GL_QUADS)
        if not self.herida:
            glColor3f(1.0,0.8,0.0)
        else:
            glColor3f(1.0,0.0,0.0)
        glVertex3f(-0.1,0.15,0.0)
        glVertex3f(0.1,0.15,0.0)
        glVertex3f(0.1,-0.15,0.0)
        glVertex3f(-0.1,-0.15,0.0)
        glEnd()
        glPopMatrix()