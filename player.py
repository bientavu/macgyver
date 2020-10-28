import pygame
from constantes import MAC_GYVER_PIC

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__
        self.velocity = 3
        self.slower_velocity = 1 / 2
        self.image = pygame.image.load(MAC_GYVER_PIC).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.velocity = self.velocity - self.slower_velocity

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

