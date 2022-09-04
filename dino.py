# Dino Game
# Sprite Sheet: é uma imagem que contem todos os frames de uma animação.


import pygame
from pygame.locals import *
from sys import exit
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')
# carregar as pastas de sons  e imagens para dentro do diretório principal.

LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Dino Game')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha() #carregar as imagens(sprites)

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossaouro = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img, (32*3, 32*3)) # tamanho do dino
            self.imagens_dinossaouro.append(img)
            # reprodução das imagens em ciclo de repetição.

        self.index_lista = 0
        self.image = self.imagens_dinossaouro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)
        # posicionamento na tela e tamanho da sprite.
    
    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossaouro[int(self.index_lista)]
        # criar ciclo de repetição das sprites na tela.

        

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()


