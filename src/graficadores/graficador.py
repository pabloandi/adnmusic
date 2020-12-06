from abc import ABC,abstractmethod

class Graficador():
    
    @abstractmethod
    def pintar_linea(self, linea):
        pass

    @abstractmethod
    def pintar_nota(self, nota):
        pass

    @abstractmethod
    def pintar_ambiente(self):
        pass