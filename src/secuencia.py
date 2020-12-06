from Bio import SeqIO
from collections.abc import Sequence
from generadores import CajitaMusicalGenerador as Generador

class Secuencia(Sequence):
    """
    """
    def __init__(self, archivo):
        
        self.sec = self.cargar_archivo(archivo)
    
    def cargar_archivo(self, archivo):
        """
        """
        try:
            tipoarchivo = archivo.suffix[1:]
            return SeqIO.read(archivo,tipoarchivo).seq
        except Exception:
            pass

    def __next__(self):
        pass
    
    def __iter__(self):
        """
        Esta función define esta clase como iterador.
        Cada vez que se necesita una nueva posición de 
        diente y nuevo aminoacido, se invoca esta función
        mediante next()
        """
        return Generador(self.sec)
    
    def __getitem__(self, key):
        return self.sec[key]
    
    def __len__(self):
        return len(self.sec)

if __name__ == '__main__':
    from pathlib import Path
    archivo = Path("./material/bacteria/Bacillus anthracis str. Ames chromosome, complete genome.gbk")
    sec = iter(Secuencia(archivo))
    print(sec)
    while True:
        try:
            print(next(sec))
        except StopIteration:
            break
    
    