#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from cmath import cos, pi, sin
import dis
from OpenGL.GL import *
from Asteroide import Asteroide
from Nave_Enemiga import *
from glew_wish import *
import glfw
import math
from Nave import *
import random
from StreamThread import *

class App:

    window = None
    tiempo_anterior = 0.0

    nave = Nave()
    asteroides = []

    nave_enemiga = Nave_Enemiga()
    

    def actualizar(self):

        tiempo_actual = glfw.get_time()
        #Cuanto tiempo paso entre la ejecucion actual
        #y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - self.tiempo_anterior
        
        self.nave.actualizar(self.window, tiempo_delta)
        for asteroide in self.asteroides:
            if asteroide.vivo:
                asteroide.actualizar(tiempo_delta)
                #if asteroide.colisionando(self.nave):
                #    self.nave.herido = True
                if asteroide.colisionando(self.nave_enemiga):
                    self.nave_enemiga.herida = True
                for bala in self.nave.balas:
                    if bala.disparando:
                        if asteroide.colisionando(bala):
                            bala.disparando = False
                            asteroide.vivo = False
        self.tiempo_anterior = tiempo_actual



    def draw(self):
        self.nave.dibujar()
        for asteroide in self.asteroides:
            asteroide.dibujar()
        #nave_enemiga.dibujar()

    def inicializar_asteroides(self):
        for i in range(10):
            posicion_x = (random.random() * 2) - 1 
            posicion_y = (random.random() * 2) - 1 
            if abs(posicion_x) < 0.2:
                if posicion_x < 0:
                    posicion_x = -0.2
                else:
                    posicion_x = 0.2
            if abs(posicion_y) < 0.2:
                if posicion_y < 0:
                    posicion_y = -0.2
                else:
                    posicion_y = 0.2
            direccion = random.random() * 360
            velocidad = (random.random() * 0.5) +0.2 
            self.asteroides.append(Asteroide(posicion_x,posicion_y,
                direccion, velocidad))
            
            mi_asteroide = Asteroide(-0.4, 0.7, 45.0, 1.0)

    def main(self):
        global app

        width = 700
        height = 700
        #Inicializar GLFW
        if not glfw.init():
            return

        #declarar ventana
        self.window = glfw.create_window(width, height, "Mi ventana", None, None)

        #Configuraciones de OpenGL
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        #Verificamos la creacion de la ventana
        if not self.window:
            glfw.terminate()
            return

        #Establecer el contexto
        glfw.make_context_current(self.window)

        #Le dice a GLEW que si usaremos el GPU
        glewExperimental = True

        #Inicializar glew
        if glewInit() != GLEW_OK:
            print("No se pudo inicializar GLEW")
            return

        #imprimir version
        version = glGetString(GL_VERSION)
        print(version)

        self.inicializar_asteroides()

        #iniciar StreamThread
        self.stream_thread = StreamThread(self)
        self.stream_thread.daemon = True
        self.stream_thread.start()

        #Draw loop
        while not glfw.window_should_close(self.window):
            #Establecer el viewport
            #glViewport(0,0,width,height)
            #Establecer color de borrado
            glClearColor(0.7,0.7,0.7,1)
            #Borrar el contenido del viewport
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


            self.actualizar()
            #Dibujar
            self.draw()


            #Polling de inputs
            glfw.poll_events()

            #Cambia los buffers
            glfw.swap_buffers(self.window)

        glfw.destroy_window(self.window)
        glfw.terminate()
        self.stream_thread.stream.abort()
        self.stream_thread.event.set()
        self.stream_thread.join()

if __name__ == "__main__":
    app = App()
    app.main()
