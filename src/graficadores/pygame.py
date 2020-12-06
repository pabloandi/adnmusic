from collections import deque
from threading import Thread

from .graficador import Graficador

import pygame
from pygame.sprite import Sprite, Group as SpriteGroup


class PygameGraficador(Graficador, Thread):
    def __init__(self):
        super(PygameGraficador, self).__init__()
        self.historial = deque(maxlen=70)
        self.pygame_init()
    
    def pygame_init(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((820,620), pygame.HWSURFACE)
        self.running = True
        self.clock = pygame.time.Clock()

        # colors
        self.A = pygame.Color(0,255,0)
        self.T = pygame.Color(255,0,0)
        self.G = pygame.Color(255,255,0)
        self.C = pygame.Color(0,0,255)
        self.U = pygame.Color(255,127,0)
        self.otro = pygame.Color(84,84,84)
    
    def loop(self):
        pass

    def render(self):
        self.pintar_dientes()
    
    def events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            
    
    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.events(event)
            self.render()
        pygame.quit()
    
    
    
    def pintar_linea(self, linea):
        print(linea)
        self.historial.appendleft(linea)
        

    def pintar_nota(self, nota, y):
        pos = ( int(nota[1]) * 8, y * 10 )
        pygame.draw.circle(
            self.pantalla, 
            self.seleccionarColor(nota[0]), 
            pos, 
            4 
        )

    def pintar_ambiente(self):
        """ pintar las lineas del ambiente """
        self.pantalla.fill(pygame.Color('lightgrey'))
        ancho, alto = self.pantalla.get_size()
        _ , marco_alto = ancho - 20, alto - 20

        for x in (n * 8 for n in range(1,100)):
            # pintar las lineas con un espacio de acuerdo 
            # al número de dientes

            pygame.draw.line(
                self.pantalla, 
                pygame.Color('grey'),
                (x, alto - marco_alto),
                (x, marco_alto)
            )
    
    def pintar_dientes(self):
        self.pintar_ambiente()  
        for y, linea in enumerate(list(self.historial), 1):
            # for i in range(y,y+5):
            for diente in linea:
                if diente is not None:
                    self.pintar_nota(diente, y)
                
        # pygame.time.delay(2000)
        pygame.display.update()
            
    
    def seleccionarColor(self, aminoacido):
        color = None
        if aminoacido == 'A':
            color = self.A
        elif aminoacido == 'T':
            color = self.T
        elif aminoacido == 'G':
            color = self.G
        elif aminoacido == 'C':
            color = self.C
        elif aminoacido == 'U':
            color = self.U
        else:
            color = self.otro

        return color
    
    def run(self):
        self.execute()

if __name__ == '__main__':
    PygameGraficador().start()