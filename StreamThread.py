from threading import Thread, Event
import numpy as np
import sounddevice as sd
from Character import *

class StreamThread(Thread):
    def __init__(self, app):
        super().__init__()
        self.dispoitivo_input = 1
        self.dispoitivo_output = 3
        self.tamano_bloque = 8000
        self.frecuencia_muestreo = 44100
        self.canales = 1
        self.tipo_dato = np.int16
        self.latencia = "high"
        self.app = app
        tiempo_anterior = 0.0 
        
    def callback_stream(self, indata, outdata, frames, time, status):

        data = indata[:,0]
        transformada = np.fft.rfft(data)
        periodo_muestreo = 1/self.frecuencia_muestreo
        frecuencias = np.fft.rfftfreq(len(data), periodo_muestreo)
        frecuencia_fundamental = frecuencias[np.argmax(np.abs(transformada))]
        print("frecuencia fundamental: " + str(frecuencias[np.argmax(np.abs(transformada))]))
        
        
        tiempo_actual = glfw.get_time()
        tiempo_delta = tiempo_actual - self.app.player.tiempo_anterior

        poder_salto = 0.1
        vel_y = self.app.player.velocidad_y * tiempo_delta * poder_salto
        gravedad = -0.3
        cantidad_de_salto = 0.01

        vel_y = self.app.player.velocidad_y * tiempo_delta * self.app.player.poder_salto

        if self.app.player.JUMP is False and self.app.player.IS_JUMPING is False and frecuencia_fundamental > 100 and frecuencia_fundamental < 150:
            self.app.player.JUMP = True
            self.app.player.posicion_y_triangulo_anterior = self.app.player.posicion_y
            print('salto!')

        if self.app.player.JUMP is True:
            # Añade a la y la velocidad_y a la velocidad anteiror
            # Añade la velocidad del salto
            self.app.player.posicion_y += vel_y
            self.app.player.IS_JUMPING = True

        if self.app.player.IS_JUMPING:
            if self.app.player.posicion_y - self.app.player.posicion_y_triangulo_anterior >= cantidad_de_salto:
                self.app.player.JUMP = False
                vel_y = gravedad * tiempo_delta
                self.app.player.posicion_y += vel_y
                self.app.player.IS_FALLING = True

        if self.app.player.IS_FALLING: 
            vel_y = gravedad * tiempo_delta
            self.app.player.posicion_y += vel_y

            if self.app.player.posicion_y <= self.app.player.posicion_y_triangulo_anterior:
                self.app.player.IS_JUMPING = False
                self.app.player.JUMP = False
                self.app.player.IS_FALLING = False
                self.app.player.posicion_y = self.app.player.posicion_y_triangulo_anterior   

        return

    def run(self):
        try:
            self.event = Event()
            with sd.Stream(
                device=(self.dispoitivo_input, self.dispoitivo_output), #Se eligen dispositivos (entrada, salida)
                blocksize= self.tamano_bloque, # 0 significa que la tarjeta de sonido decide el mejor tamaño
                samplerate= self.frecuencia_muestreo, # frecuencia de muestreo
                channels= self.canales, #numero de canales1
                dtype= self.tipo_dato, #Tipo de dato (profundidad de bits)
                latency=self.latencia, # Latencia, que tanto tiempo pasa desde entrada hasta la salida
                callback= self.callback_stream
            ) as self.stream:
                self.event.wait()

        except Exception as e:
            print(str(e))