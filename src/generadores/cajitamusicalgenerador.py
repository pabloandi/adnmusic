from collections.abc import Generator

class CajitaMusicalGenerador(Generator):
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.numero_dientes = 100
        self.posicion_diente = self.numero_dientes // 2
        self.posicion_secuencia = 0

    def __next__(self):

        try:
            aminoacido = self.secuencia[self.posicion_secuencia]

            if aminoacido == 'A':
                self.posicion_diente-=1
            elif aminoacido == 'T':
                self.posicion_diente+=1
            elif aminoacido == 'C':
                self.posicion_diente-=1
                self.posicion_secuencia+=1
            elif aminoacido == 'G':
                self.posicion_diente+=1
                self.posicion_secuencia+=1
            else:
                pass
            
            if self.posicion_diente < 1:
                self.posicion_diente = 1
            if self.posicion_diente > self.numero_dientes:
                self.posicion_diente = self.numero_dientes

            res = (self.secuencia[self.posicion_secuencia], self.posicion_diente)
            self.posicion_secuencia+=1
            
            return res
        except IndexError:
            raise StopIteration
    
    def send(self):
        pass

    def throw(self):
        pass
