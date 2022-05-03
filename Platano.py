from OpenGL.GL import *
from glew_wish import *
from math import *
from Modelo import *
import math
import glfw


class Platano(Modelo):

    angulo_platano = 0.0
    direccion_platano = 1
    velocidad_platano = 0.5
    rotacion_platano = 0
    posicion_platano = [-0.9,0.85,0.0]
    velocidad_angular = 135.0

    def __init__(self):
        super().__init__(0.0,0.0,0.0,0.5,0.0)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def draw_platano(self):
        glPushMatrix()
        
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        glRotatef(self.rotacion_platano,0.0,0.0,1.0)
        glScalef(0.8,0.8,0)

        glBegin(GL_POLYGON)
        glColor3f(0.9, 1.0, 0.0)
        glVertex3f(0.1,0.1,0.0)
        glVertex3f(0.08,0.1,0.0)
        glVertex3f(0.06,0.05,0.0)
        glVertex3f(0.06,0.0,0.0)
        glVertex3f(0.07,-0.05,0.0)
        glVertex3f(0.1,-0.1,0.0)
        glVertex3f(0.12,-0.1,0.0)

        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.3,0.3,0.3)
        glVertex3f(0.08,0.1,0.0)
        glVertex3f(0.1,0.1,0.0)
        glVertex3f(0.1,0.12,0.0)
        glVertex3f(0.08,0.12,0.0)

        glEnd()

        glPopMatrix()


    def actualizar_platano(self, tiempo_delta):

        cantidad_rotacion = self.velocidad_angular * tiempo_delta
        self.rotacion_platano = self.rotacion_platano + cantidad_rotacion
        
        if self.rotacion_platano > 360.0:
            self.rotacion_platano = self.rotacion_platano - 360.0

        cantidad_movimiento = self.velocidad_platano * tiempo_delta

        if self.direccion_platano == 1:
            self.posicion_x = self.posicion_x + cantidad_movimiento
            self.posicion_y = self.posicion_y + (
                math.sin((self.angulo_platano + -90) * pi / 180.0) * cantidad_movimiento
            )
            if self.posicion_x >= 1:
                self.direccion_platano = 0

        if self.direccion_platano == 0:
            self.posicion_x = self.posicion_x - cantidad_movimiento
            self.posicion_y = self.posicion_y - (
                math.sin((self.angulo_platano - 90) * pi / 180.0) * cantidad_movimiento
            )
            if self.posicion_x <= -1:
                self.direccion_platano = 1
        