from collections import deque
from mingus.midi import fluidsynth
from mingus.containers import Note
from .reproductor import Reproductor
from pathlib import Path
from time import sleep

class CajitaMusicalMingusReproductor(Reproductor):
    """
    """
    def __init__(self):
        self.historial = deque(maxlen=20)
        self.sintetizador = fluidsynth
        path_soundfont_file = Path(__file__).parent.joinpath('soundfont/generaluser.sf2').resolve()
        self.sintetizador.init(str(path_soundfont_file),'alsa','sample.wav')
        self.sintetizador.set_instrument(1,9)
        
    
    def tocar_linea(self, linea):
        # notas = NoteContainer()
        for i,posicion in enumerate(linea):
            if posicion is not None:
                self.tocar_nota(Note(posicion[1],i))
        # sleep(0.5)

    def tocar_nota(self, nota):
        self.sintetizador.play_Note(nota)
        