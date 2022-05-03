from OpenGL.GL import *
from glew_wish import *
import glfw

class Modelo:
    @property
    def posicion_x(self):
        return self._posicion_x
    @posicion_x.setter
    def posicion_x(self, posicion_x):
        self._posicion_x = posicion_x

    @property
    def posicion_y(self):
        return self._posicion_y
    @posicion_y.setter
    def posicion_y(self, posicion_y):
        self._posicion_y = posicion_y

    @property
    def posicion_z(self):
        return self._posicion_z
    @posicion_z.setter
    def posicion_z(self, posicion_z):
        self._posicion_z = posicion_z

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def extremo_izquierdo(self):
        return self._extremo_izquierdo
    @extremo_izquierdo.setter
    def extremo_izquierdo(self, extremo_izquierdo):
        self._extremo_izquierdo = extremo_izquierdo

    @property
    def extremo_derecho(self):
        return self._extremo_derecho
    @extremo_derecho.setter
    def extremo_derecho(self, extremo_derecho):
        self._extremo_derecho = extremo_derecho

    @property
    def extremo_superior(self):
        return self._extremo_superior
    @extremo_superior.setter
    def extremo_superior(self, extremo_superior):
        self._extremo_superior = extremo_superior

    @property
    def extremo_inferior(self):
        return self._extremo_inferior
    @extremo_inferior.setter
    def extremo_inferior(self, extremo_inferior):
        self._extremo_inferior = extremo_inferior

    def __init__(self, posicion_x = 0.0, posicion_y = 0.0, posicion_z = 0.0,
        velocidad = 0.0, direccion = 0.0):
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._posicion_z = posicion_z
        self._velocidad = velocidad
        self._direccion = direccion

    def colisionando(self, modelo):
        assert isinstance(modelo,Modelo)
        colisionando = False
        #Método de bounding box:
        #Extrema derecha del primero >= Extrema izquierda segundo
        #Extrema izquierda del primero <= Extrema derecha segundo
        #Extremo superior del primero >= Extremo inferior del segundo
        #Extremo inferior del primero <= Extremo superior del segundo
        #Self es el 1er elemento y modelo el 2do
        if (self.posicion_x + self.extremo_derecho >= modelo.posicion_x - modelo.extremo_izquierdo 
            and self.posicion_x - self.extremo_izquierdo <= modelo.posicion_x + modelo.extremo_derecho 
            and self.posicion_y + self.extremo_superior >= modelo.posicion_y - modelo.extremo_inferior 
            and self.posicion_y - self.extremo_inferior <= modelo.posicion_y + modelo.extremo_superior):
            
            colisionando = True 
        return colisionando
    
    def dibujar_bounding_box(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-self.extremo_izquierdo, -self.extremo_inferior, 0.0)
        glVertex3f(-self.extremo_izquierdo,self.extremo_superior,0.0)
        glVertex3f(self.extremo_derecho, self.extremo_superior,0.0)
        glVertex3f(self._extremo_derecho,-self.extremo_inferior,0.0)
        glEnd()
        glPopMatrix()