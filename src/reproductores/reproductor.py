from abc import ABC,abstractmethod

class Reproductor():
    @abstractmethod
    def tocar_linea(self, linea):
        pass

    @abstractmethod
    def tocar_nota(self, nota):
        pass