import pygame
from constantes import MAC_GYVER_PIC

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__
        self.velocity = 30
        self.image = pygame.image.load(MAC_GYVER_PIC).convert_alpha()
        self.rect = self.image.get_rect()

    