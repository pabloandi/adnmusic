from reproductores import CajitaMusicalMingusReproductor as Reproductor
from graficadores import PygameGraficador as Graficador
from secuencia import Secuencia

from pathlib import Path
from time import sleep
from itertools import zip_longest
from pubsub import pub

class Main():
    def __init__(self):
        
        self.reproductor = Reproductor()
        self.graficador = Graficador()
        self.iniciar()

    def iniciar(self):
        
        archivos_secuencias = [ archivo for archivo in Path('./secuencias').resolve().rglob('*') if archivo.is_file() ]
        secuencias = [ iter(Secuencia(archivo)) for archivo in archivos_secuencias ]
        iterador_secuencias = zip_longest(*secuencias)

        pub.subscribe(self.reproductor.tocar_linea, 'linea')
        pub.subscribe(self.graficador.pintar_linea, 'linea')

        self.graficador.start()

        while True:
            try:
                linea =  next(iterador_secuencias)
                pub.sendMessage('linea', linea=linea)
                sleep(0.5)
            except StopIteration:
                break
            except KeyboardInterrupt:
                self.graficador.join()
                break
            

if __name__ == '__main__':
    Main()