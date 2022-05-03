from OpenGL.GL import *
from glew_wish import *
from Modelo import *
import glfw
import math

class Player(Modelo):

    tiempo_anterior = 0.0 
    velocidad = 0.5
    velocidad_x = 0.5
    velocidad_y = 0.5
    IS_JUMPING = False
    IS_FALLING = False
    JUMP = False
    # posicion_triangulo_x = -0.6
    # posicion_triangulo_y = -0.65
    # posicion_triangulo_z = 0
    posicion_y_triangulo_anterior = 0.0
    vivo = True

    def __init__(self):
        super().__init__(-0.6,-0.65,0.0,1.0,0.0)
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def draw(self):
        if self.vivo:
            glPushMatrix()
            glTranslatef(self.posicion_x, self.posicion_y,0.0)
        #CUERPO

        glPushMatrix()
        glTranslatef(-0.045,-0.03,0)
        glScalef(0.2,0.5,0)
        
        glBegin(GL_QUADS)
        glColor3f(252/255, 230/255, 164/255)
        glVertex3f(0.01,0.02,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.02,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.03,-0.03,0)
        glScalef(0.2,0.5,0)
        
        glBegin(GL_QUADS)
        glColor3f(252/255, 230/255, 164/255)
        glVertex3f(0.01,0.02,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.02,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(-0.045,-0.03,0)
        glScalef(0.2,1,0)
        
        glBegin(GL_QUADS)
        glColor3f(0, 81/255, 212/255)
        glVertex3f(0.01,0.02,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.02,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.03,-0.03,0)
        glScalef(0.2,1,0)
        
        glBegin(GL_QUADS)
        glColor3f(0, 81/255, 212/255)
        glVertex3f(0.01,0.02,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.02,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.024,-0.026,0)
            
        glBegin(GL_QUADS)
        glColor3f(1,0,0)

        glVertex3f(0,-0.01,0)
        glVertex3f(0,0.085,0)
        glVertex3f(-0.08,0.085,0)
        glVertex3f(-0.08,-0.01,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0,0.02,0)
        glScalef(0.3,0.2,0)

        glBegin(GL_QUADS)
        glColor3f(0, 36/255, 181/255)

        glVertex3f(0,-0.01,0)
        glVertex3f(0,0.085,0)
        glVertex3f(-0.08,0.085,0)
        glVertex3f(-0.08,-0.01,0)
        glEnd()

        glPopMatrix()

        #CABEZA
        glPushMatrix()

        glPushMatrix()
        glTranslatef(0.01,0.09,0)
        glScalef(0.5,0.35,0)
        
        glBegin(GL_QUADS)
        glColor3f(1,0,0)
        glVertex3f(0,-0.01,0)
        glVertex3f(0,0.085,0)
        glVertex3f(-0.1,0.085,0)
        glVertex3f(-0.1,-0.01,0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.01,0.06,0)
        glScalef(0.52,0.6,0)
        
        glBegin(GL_QUADS)
        glColor3f(252/255, 230/255, 164/255)
        glVertex3f(0,-0.01,0)
        glVertex3f(0,0.085,0)
        glVertex3f(-0.1,0.085,0)
        glVertex3f(-0.1,-0.01,0)
        glEnd()
        glPopMatrix()

        #PATAS
        glPushMatrix()
        glTranslatef(-0.03,-0.125,0)
        glScalef(0.2,1,0)
        
        glBegin(GL_QUADS)
        glColor3f(0, 81/255, 212/255)
        glVertex3f(0.01,0.05,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.05,0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.02,-0.125,0)
        glScalef(0.2,1,0)
        
        glBegin(GL_QUADS)
        glColor3f(0, 81/255, 212/255)
        glVertex3f(0.01,0.05,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.05,0)
        glEnd()

        glPushMatrix()
        glTranslatef(0,0.02,0)
        glScalef(1,0.4,0)
        
        glBegin(GL_QUADS)
        glColor3f(252/255, 230/255, 164/255)
        glVertex3f(0.01,0.05,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.05,0)
        glEnd()

        glPushMatrix()
        glTranslatef(-0.25,0,0)
        glScalef(1,1,0)
        
        glBegin(GL_QUADS)
        glColor3f(252/255, 230/255, 164/255)
        glVertex3f(0.01,0.05,0)
        glVertex3f(0.01,0.09,0)
        glVertex3f(-0.1,0.09,0)
        glVertex3f(-0.1,0.05,0)
        glEnd()
        

        glPopMatrix()
        

        glPopMatrix()

        glPopMatrix()

        glPopMatrix()
        
        glPopMatrix()

    def actualizar(self, window, tiempo_delta):
        if self.vivo: 
            global tiempo_anterior
            global estado_tecla_arriba, estado_tecla_abajo
            # global posicion_triangulo_x, posicion_triangulo_y, posicion_triangulo_z, posicion_y_triangulo_anterior

            # tiempo_actual = glfw.get_time()
            # #Cuanto tiempo paso entre la ejecucion actual
            # #y la inmediata anterior de esta funcion
            # tiempo_delta = tiempo_actual - tiempo_anterior

            #Leer los estados de las teclas que queremos
            estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
            estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
            estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
            estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

            # estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
            # estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
            # estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
            # estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

            #Revisamos estados y realizamos acciones
            cantidad_movimiento = self.velocidad * tiempo_delta

            if estado_tecla_derecha == glfw.PRESS:
                self.posicion_x = self.posicion_x + cantidad_movimiento
            if estado_tecla_izquierda == glfw.PRESS:
                self.posicion_x = self.posicion_x - cantidad_movimiento

            poder_salto = 1.5
            vel_y = self.velocidad_y * tiempo_delta * poder_salto
            gravedad = -0.3
            cantidad_de_salto = 0.1
            estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
            
            if self.JUMP is False and self.IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
                self.JUMP = True
                self.posicion_y_triangulo_anterior = self.posicion_y

            if self.JUMP is True:
                # Añade a la y la velocidad_y a la velocidad anteiror
                # Añade la velocidad del salto
                self.posicion_y += vel_y
                self.IS_JUMPING = True

            if self.IS_JUMPING:
                if self.posicion_y - self.posicion_y_triangulo_anterior >= cantidad_de_salto:
                    self.JUMP = False
                    vel_y = gravedad * tiempo_delta
                    self.posicion_y += vel_y
                    self.IS_FALLING = True

            if self.IS_FALLING: 
                vel_y = gravedad * tiempo_delta
                self.posicion_y += vel_y

                if self.posicion_y <= self.posicion_y_triangulo_anterior:
                    self.IS_JUMPING = False
                    self.JUMP = False
                    self.IS_FALLING = False
                    self.posicion_y = self.posicion_y_triangulo_anterior   
