import pygame
from player import Player
from labyrinth import Labyrinth

class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}

    def init(self, window):
        """
        Initialization labyrinth
        """
        labyrinth = Labyrinth()
        labyrinth.labyrinth_construction()
        labyrinth.display_level(window)