import pygame
import pylint
from constantes import MAC_GYVER_IMAGE, FLOOR_IMAGE, SPRITE_SIZE
from labyrinth import Labyrinth


class Player:
    def __init__(self, mac_gyver_image, floor_image, labyrinth, window):
        self.position = [0, 0]
        self.mac_gyver_image = pygame.image.load(MAC_GYVER_IMAGE).convert_alpha()
        self.floor_image = pygame.image.load(FLOOR_IMAGE).convert_alpha()
        self.labyrinth = labyrinth
        self.window = window

    def blit(self, past_position):
        """
        Calculate next position for blit images
        """
        x_pix = self.position[0] * SPRITE_SIZE
        y_pix = self.position[1] * SPRITE_SIZE
        past_position = [i * SPRITE_SIZE for i in past_position]

        self.window.blit(self.floor_image, past_position)
        self.window.blit(self.mac_gyver_image, [x_pix, y_pix])
        pygame.display.update()

    def move(self, direction):
        """
        Input setup for character movement
        """
        self.x = self.position[0]
        self.y = self.position[1]
        labyrinth = self.labyrinth

        if direction == "right":
            next_position = [self.x + 1, self.y]
            if labyrinth.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace by floor image
                self.position = (
                    next_position  # Determine new position to blit mac_gyver_image
                )
                self.blit(past_position)

        elif direction == "left":
            next_position = [self.x - 1, self.y]
            if labyrinth.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace by floor image
                self.position = (
                    next_position  # Determine new position to blit mac_gyver_image
                )
                self.blit(past_position)

        elif direction == "up":
            next_position = [self.x, self.y - 1]
            if labyrinth.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace by floor image
                self.position = (
                    next_position  # Determine new position to blit mac_gyver_image
                )
                self.blit(past_position)

        elif direction == "down":
            next_position = [self.x, self.y + 1]
            if labyrinth.test_next_position(next_position):
                past_position = (
                    self.position
                )  # Determine previous position to replace by floor image
                self.position = (
                    next_position  # Determine new position to blit mac_gyver_image
                )
                self.blit(past_position)
