from threading import Thread, Event
import numpy as np
import sounddevice as sd

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
    def callback_stream(self, indata, outdata, frames, time, status):

        data = indata[:,0]
        transformada = np.fft.rfft(data)
        periodo_muestreo = 1/self.frecuencia_muestreo
        frecuencias = np.fft.rfftfreq(len(data), periodo_muestreo)
        frecuencia_fundamental = frecuencias[np.argmax(np.abs(transformada))]
        print("frecuencia fundamental: " + str(frecuencias[np.argmax(np.abs(transformada))]))

        if frecuencia_fundamental > 400 and frecuencia_fundamental < 605:
            self.app.nave.herido = True
        else: 
            self.app.nave.herido = False

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