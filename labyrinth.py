import pygame
from constantes import WALL_PATH, FLOOR_PATH, END_PATH, SPRITE_SIZE


class Labyrinth():

    def __init__(self):
        self.structure = []

    def labyrinth_construction(self):
        """
        Init labyrinth
        """
        with open('labyrinth.txt', 'r') as file:
            for line in file:
                row = []
                for letter in line:
                    if letter != "\n":
                        row.append(letter)
                self.structure.append(row)

    def display_level(self, window):
        """
        Display level
        """
        wall = pygame.image.load(WALL_PATH).convert_alpha()
        floor = pygame.image.load(FLOOR_PATH).convert_alpha()
        #end = pygame.image.load(END_PATH).convert_alpha()
        x = 0
        y = 0
        for line in self.structure:
            for letter in line:
                if letter == "W":
                    window.blit(wall, [x, y])
                elif letter == "F":
                    window.blit(floor, [x, y])
                #else:
                    #window.blit(end, [x, y])
                x += SPRITE_SIZE
                if x >= len(line)*SPRITE_SIZE:
                    x = 0
                    y += SPRITE_SIZE




# laby = Labyrinth()
# laby.labyrinth_construction()

# for element in laby.structure:
#     print(element)