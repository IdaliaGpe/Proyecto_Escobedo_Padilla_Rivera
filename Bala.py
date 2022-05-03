from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Bala(Modelo):

    disparando = False

    def __init__(self):
        super().__init__(velocidad=0.75)
        self.extremo_izquierdo = 0.01
        self.extremo_derecho = 0.01
        self.extremo_inferior = 0.01
        self.extremo_superior = 0.01

    def dibujar(self):
        if self.disparando:
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.3, 0.3, 0.3)
            glVertex3f(-0.01,0.01,0.0)
            glVertex3f(0.01,0.01,0.0)
            glVertex3f(0.01,-0.01,0.0)
            glVertex3f(-0.01,-0.01,0.0)
            glEnd()
            glPopMatrix()
            self.dibujar_bounding_box()

    def actualizar(self, tiempo_delta):
        if self.disparando:
            cantidad_movimiento = self.velocidad * tiempo_delta
            self.posicion_x = self.posicion_x + (
                math.cos(self.direccion * math.pi / 180.0) * cantidad_movimiento
            )
            self.posicion_y = self.posicion_y + (
                math.sin(self.direccion * math.pi / 180.0) * cantidad_movimiento
            )
            #checar si está chocando contra enemigos
            #(Eso hay que hacerlo, no está hecho)

            #Checar si se salió de los límites:
            if (self.posicion_x > 1 or self.posicion_x < -1 or 
                self.posicion_y > 1 or self.posicion_y < -1):
                self.disparando = False