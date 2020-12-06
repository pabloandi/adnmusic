from collections import deque
from .graficador import Graficador

class TerminalGraficador(Graficador):
    def __init__(self):
        self.historial = deque(maxlen=20)

    def pintar_linea(self, linea):
        print(linea)
        self.historial.append(linea)

    def pintar_nota(self, nota):
        pass

    def pintar_ambiente(self):
        pass