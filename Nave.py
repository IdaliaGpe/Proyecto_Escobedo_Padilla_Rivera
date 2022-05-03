from OpenGL.GL import *
from glew_wish import *
import glfw
import math
from Bala import *
from Modelo import *

class Nave(Modelo):

    fase = 90.0
    velocidad_rotacion = 90.0
    balas = [Bala(), Bala(), Bala(), Bala(), Bala(), Bala(), Bala(), Bala()]
    estado_anterior_espacio = glfw.RELEASE
    herido = False

    def __init__(self):
        super().__init__(0.0,0.0,0.0,0.5,0.0)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def dibujar(self):

        for bala in self.balas:
            bala.dibujar()

        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glRotatef(self.direccion, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)

        if not self.herido:
            glColor3f(0.0,0.0,1.0)
        else:
            glColor3f(1.0,0.0,0.0)

        #Manda vertices a dibujar
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.0,0.05,0)
        glVertex3f(0.05,-0.05,0)

        glEnd()
        glPopMatrix()

        self.dibujar_bounding_box()

        

        
        
    
    def actualizar(self, window, tiempo_delta):
        #Leer los estados de las teclas que queremos
        estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
        estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estado_tecla_espacio = glfw.get_key(window, glfw.KEY_SPACE)

        if (estado_tecla_espacio == glfw.PRESS and 
            self.estado_anterior_espacio == glfw.RELEASE):
            for bala in self.balas:
                if not bala.disparando:
                    bala.disparando = True
                    bala.posicion_x = self.posicion_x
                    bala.posicion_y = self.posicion_y
                    bala.direccion = self.direccion + self.fase
                    break

        #Revisamos estados y realizamos acciones
        cantidad_movimiento = self.velocidad * tiempo_delta
        if estado_tecla_arriba == glfw.PRESS:
            self.posicion_x = self.posicion_x + (
                math.cos((self.direccion + self.fase) * math.pi / 180.0) * cantidad_movimiento
            )
            self.posicion_y = self.posicion_y + (
                math.sin((self.direccion + self.fase) * math.pi / 180.0) * cantidad_movimiento
            )
        
        cantidad_rotacion = self.velocidad_rotacion * tiempo_delta
        if estado_tecla_izquierda == glfw.PRESS:
            self.direccion = self.direccion + cantidad_rotacion
            if self.direccion > 360.0:
                self.direccion = self.direccion - 360.0 
        if estado_tecla_derecha == glfw.PRESS:
            self.direccion = self.direccion - cantidad_rotacion
            if self.direccion < 0.0:
                self.direccion = self.direccion + 360.0
        
        if self.posicion_x > 1.05:
            self.posicion_x = -1.0
        if self.posicion_x < -1.05:
            self.posicion_x = 1.0
        if self.posicion_y > 1.05:
            self.posicion_y = -1.0
        if self.posicion_y < -1.05:
            self.posicion_y = 1.0
        
        self.estado_anterior_espacio = estado_tecla_espacio

        for bala in self.balas:
            bala.actualizar(tiempo_delta)