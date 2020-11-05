import pygame
from constantes import WALL_IMAGE, FLOOR_IMAGE, END_IMAGE, SPRITE_SIZE, STRUCTURE_SIZE

class Labyrinth():

    def __init__(self):
        super().__init__()
        self.structure = []

    def labyrinth_construction(self):
        '''
        Init labyrinth
        '''
        with open('labyrinth.txt', 'r') as file:
            for line in file:
                row = []
                for letter in line:
                    if letter != "\n":
                        row.append(letter)
                self.structure.append(row)


    def display_level(self, window):
        '''
        Display level
        '''
        wall = pygame.image.load(WALL_IMAGE).convert_alpha()
        floor = pygame.image.load(FLOOR_IMAGE).convert_alpha()
        end = pygame.image.load(END_IMAGE).convert_alpha()
        x = 0
        y = 0
        for line in self.structure:
            for letter in line:
                if letter == "W":
                    window.blit(wall, [x, y])
                elif letter == "F":
                    window.blit(floor, [x, y])
                else:
                    window.blit(end, [x, y])
                x += SPRITE_SIZE
                if x >= len(line)*SPRITE_SIZE:
                    x = 0
                    y += SPRITE_SIZE


    def test_next_position(self, next_position):
        '''
        Test if player position is available
        '''
        if (next_position[0] < STRUCTURE_SIZE[0] and next_position[1] < STRUCTURE_SIZE[1]):
            if next_position[0] >= 0 and next_position[1] >= 0:
                if self.structure[next_position[1]][next_position[0]] != "W":
                    return True


    def end_game(self, player):
        '''
        Game finished if player is in the end position
        '''
        if player.position == [14, 14]:
            return False
        else:
            return True

    def response(self, player, objects):
        '''
        Check if player win or loose
        '''
        if player.position == [14, 14] and objects.objects_collected == 3:
            return True
        elif player.position == [14, 14] and objects.objects_collected != 3:
            return False