from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Modelo import *

class Asteroide(Modelo):

    vivo = True

    def __init__(self, x, y, direccion, velocidad):
        super().__init__(x,y,0.0,velocidad,direccion)
        self.extremo_izquierdo = 0.07
        self.extremo_derecho = 0.07
        self.extremo_inferior = 0.07
        self.extremo_superior = 0.07

    def actualizar(self, tiempo_delta):
        if self.vivo:
            cantidad_movimiento = self.velocidad * tiempo_delta
            self.posicion_x = self.posicion_x + (
                math.cos(self.direccion * math.pi / 180.0) *
                cantidad_movimiento)
            self.posicion_y = self.posicion_y + (
                math.sin(self.direccion * math.pi / 180.0) *
                cantidad_movimiento
            )

            if self.posicion_x > 1.05:
                self.posicion_x = -1.0
            if self.posicion_x < -1.05:
                self.posicion_x = 1.0
            
            if self.posicion_y > 1.05:
                self.posicion_y = -1.0
            if self.posicion_y < -1.05:
                self.posicion_y = 1.0

    def dibujar(self):
        if self.vivo:
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
            glBegin(GL_POLYGON)
            glColor3f(0.4, 0.9, 0.21)
            for i in range(0, 360, 10):
                componente_x = 0.07 * math.cos(i * math.pi / 180.0)
                componente_y = 0.07 * math.sin(i * math.pi / 180.0)
                glVertex3f(componente_x, componente_y, 0.0)
            glEnd()
            glPopMatrix()

            self.dibujar_bounding_box()