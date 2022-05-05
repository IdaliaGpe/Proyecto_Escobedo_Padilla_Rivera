from OpenGL.GL import *
from glew_wish import *
import glfw
from StreamThread import *

class App:

    window = None
    tiempo_anterior = 0.0

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

            #Dibujar

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