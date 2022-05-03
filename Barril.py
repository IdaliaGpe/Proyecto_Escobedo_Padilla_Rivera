from msilib.schema import Class
from OpenGL.GL import *
from glew_wish import *
from math import *
from Modelo import *
import glfw

class Barril(Modelo):
    direccion_barrelx = 1
    direccion_barrely = 0
    velocidad_barrel = 0.9
    # posicion_barrel = [-0.4,0.85, 0.0]

    def __init__(self):
        super().__init__(-0.4,0.85,0.0,0.5,0.0)
        self.extremo_izquierdo = 0.02
        self.extremo_derecho = 0.02
        self.extremo_inferior = 0.02
        self.extremo_superior = 0.02

    def draw_barrel(self):
        sides = 32    
        radius = 0.04  
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(150/255,62/255,0)    
        for i in range(100):    
            cosine= radius * cos(i*2*pi/sides)     
            sine  = radius * sin(i*2*pi/sides)   
            glVertex2f(cosine,sine)
        glEnd()
        glPopMatrix()   

        self.dibujar_bounding_box()
        
    def actualizar_barrel(self, tiempo_delta):
        cantidad_movimiento = self.velocidad_barrel * tiempo_delta

        if self.direccion_barrelx == 0:
            self.posicion_x = self.posicion_x - cantidad_movimiento
        elif self.direccion_barrelx == 1:    
            self.posicion_x = self.posicion_x + cantidad_movimiento

        if self.posicion_x <= -0.45 and self.direccion_barrelx == 0:
            self.direccion_barrelx = 1
            if self.direccion_barrely == 0:
                self.posicion_y = self.posicion_y - (cantidad_movimiento + 0.3)
            
        if self.posicion_x >= 0.75 and self.direccion_barrelx == 1:
            self.direccion_barrelx = 0
            if self.direccion_barrely == 0:
                self.posicion_y = self.posicion_y - (cantidad_movimiento + 0.3)
        
        if self.posicion_y <= -0.9:
            self.posicion_x = -0.4
            self.posicion_y = 0.85
            self.velocidad_barrel = self.velocidad_barrel + 0.2