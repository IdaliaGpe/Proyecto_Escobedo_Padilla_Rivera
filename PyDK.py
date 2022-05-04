from fnmatch import translate
from re import S
from OpenGL.GL import *
from glew_wish import *
from math import *
from Character import *
from Barril import *
from Enemy import *
from Platano import *
from Escaleras import Escaleras
from Fondo import *
from StreamThread import *

from pygame import mixer
import pygame
import glfw

pygame.mixer.init()

# mixer.music.load("LVL_Music.wav")
# mixer.music.play(-1)

class App:
    window = None
    player = Player()
    # barril_mov = Barril()
    # enemy = Enemy()
    # platano = Platano()
    # # escaleras = Escaleras()
    # fondo = Fondo()
    tiempo_anterior = 0.0

    # escaleras = []

    # def colisionando(self):
    #     colisionando = False
    #     #Método de bounding box:
    #     #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #     #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #     #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #     #Extremo inferior del triangulo <= Extremo superior del cuadrado
    #     return colisionando   

    def actualizar(self):
        global window
        global tiempo_anterior

        tiempo_actual = glfw.get_time()
        #Cuanto tiempo paso entre la ejecucion actual
        #y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - self.tiempo_anterior

        # cantidad_movimiento = self.player.velocidad * tiempo_delta
        # estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
        # estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN) 

        if self.player.vivo:
            self.player.actualizar(window, tiempo_delta)
            # if self.player.colisionando(self.platano):
            #     self.player.vivo = False
            # if self.player.colisionando(self.barril_mov):
                # self.player.vivo = False
            # for escalera in self.escaleras:
            #     if self.player.colisionando(escalera) and estado_tecla_arriba == glfw.PRESS:
            #         self.player.posicion_y = self.player.posicion_y  + self.cantidad_movimiento
            #     if self.player.colisionando(escalera) and estado_tecla_abajo == glfw.PRESS:
            #         self.player.posicion_y = self.player.posicion_y - self.cantidad_movimiento

            # barril_mov.actualizar_barrel(tiempo_delta)
            # platano.actualizar_platano(tiempo_delta)
        
        self.tiempo_anterior = tiempo_actual

    # def escaleras_init():
    #     escaleras.append(Escaleras(0.6,-0.6))
    #     escaleras.append(Escaleras(0.6,0.0))
    #     escaleras.append(Escaleras(0.6,0.6))
    #     escaleras.append(Escaleras(-0.5,0.3))
    #     escaleras.append(Escaleras(-0.5,-0.3))



    def draw(self):  
        # fondo.draw_plataform_0_1()
        # fondo.draw_plataform()
        # fondo.draw_plataform_2()   
        # fondo.draw_plataform_3()   
        # fondo.draw_plataform_4()   
        # fondo.draw_plataform_5()   
        # fondo.draw_plataform_6()   
        # fondo.draw_plataform_7()   
        # for escalera in escaleras:
        #     escalera.draw_escaleras()
        # enemy.draw_cuadrado()
        # barril_mov.draw_barrel()
        # fondo.draw_cajas()
        # fondo.draw_explosiva()
        # fondo.draw_bote()
        # fondo.draw_letrero()
        # fondo.draw_barril()
        self.player.draw()
        # fondo.draw_barriltwo()
        # platano.draw_platano()

        # escaleras.draw_escaleras()

    def main(self):
        global app

        global window
        global tiempo_anterior
        width = 900
        height = 900
        #Inicializar GLFW
        if not glfw.init():
            return

        #declarar ventana
        window = glfw.create_window(width, height, "Mi ventana", None, None)

        #Configuraciones de OpenGL
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        #Verificamos la creacion de la ventana
        if not window:
            glfw.terminate()
            return

        #Establecer el contexto
        glfw.make_context_current(window)

        #Le dice a GLEW que si usaremos el GPU
        glewExperimental = True

        #Inicializar glew
        if glewInit() != GLEW_OK:
            print("No se pudo inicializar GLEW")
            return

        #imprimir version
        version = glGetString(GL_VERSION)
        print(version)

        #iniciar StreamThread
        self.stream_thread = StreamThread(self)   
        self.stream_thread.daemon = True
        self.stream_thread.start()

        # escaleras_init()

        #Draw loop
        while not glfw.window_should_close(window):
            #Establecer el viewport
            glViewport(0,0,800,800)
            #Establecer color de borrado
            glClearColor(0,0,0,1)
            #Borrar el contenido del viewport
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.actualizar()
            #Dibujar
            self.draw()
            #Polling de inputs
            glfw.poll_events()

            #Cambia los buffers
            glfw.swap_buffers(window)

        glfw.destroy_window(window)
        glfw.terminate()
        self.stream_thread.stream.abort()
        self.stream_thread.event.set()
        self.stream_thread.join()

if __name__ == "__main__":
    app = App()
    app.main()