import pygame
import random
from constantes import ETHER_IMAGE, NEEDLE_IMAGE, SYRINGE_IMAGE, SPRITE_SIZE, ONE_IMAGE, TWO_IMAGE, THREE_IMAGE, WALL_IMAGE, RESET_IMAGE

class Objects():
    '''
    Objects items in the game
    '''
    def __init__(self, syringe_image, ether_image, needle_image, labyrinth, window):
        self.ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        self.needle = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        self.syringe = pygame.image.load(SYRINGE_IMAGE).convert_alpha()
        self.counter_ether = 0
        self.counter_needle = 0
        self.counter_syringe = 0
        self.objects_collected = 0
        self.labyrinth = labyrinth
        self.window = window


    def generate_random_position(self):
            '''
            Random position generator
            '''
            searching = True
            self.x = 0
            self.y = 0

            while searching:
                self.position = []
                self.x = random.randrange(0, 14, 1)
                self.y = random.randrange(0, 14, 1)

                if self.labyrinth.structure[self.y][self.x] == "F":
                    self.position.extend([self.x, self.y])
                    searching = False

            return self.position


    def display_objects(self):
        '''
        Use the random position generator to assign objects positions to pictures
        '''
        self.ether_position = []
        self.needle_position = []
        self.syringe_position = []

        while (self.ether_position == self.syringe_position or self.ether_position == self.needle_position or self.syringe_position == self.needle_position):
            self.ether_position = self.generate_random_position()
            self.syringe_position = self.generate_random_position()
            self.needle_position = self.generate_random_position()

            self.ether_position_pixel = [i * SPRITE_SIZE for i in self.ether_position]
            self.needle_position_pixel = [i * SPRITE_SIZE for i in self.needle_position]
            self.syringe_position_pixel = [i * SPRITE_SIZE for i in self.syringe_position]

            self.window.blit(self.ether, self.ether_position_pixel)
            self.window.blit(self.syringe, self.syringe_position_pixel)
            self.window.blit(self.needle, self.needle_position_pixel)


    def collect_objects(self, player):
        '''
        Count number of objects collected
        '''
        if player.position == self.ether_position:
            self.counter_ether = 1
        elif player.position == self.syringe_position:
            self.counter_syringe = 1
        elif player.position == self.needle_position:
            self.counter_needle = 1

        self.objects_collected = self.counter_ether + self.counter_syringe + self.counter_needle

        self.display_object_collected(
            self.objects_collected, ONE_IMAGE, TWO_IMAGE, THREE_IMAGE, WALL_IMAGE, player.position)

        return self.objects_collected


    def display_object_collected(self, objects_collected, one, two, three, wall_image, player):
        '''
        Display counter of collected objects
        '''
        one = pygame.image.load(ONE_IMAGE).convert_alpha()
        two = pygame.image.load(TWO_IMAGE).convert_alpha()
        three = pygame.image.load(THREE_IMAGE).convert_alpha()
        reset = pygame.image.load(RESET_IMAGE).convert_alpha()
        position_objects_display = [i * SPRITE_SIZE for i in [0, 15]]
        # position_objects_display_2 = [i * SPRITE_SIZE for i in [1, 15]]
        window = self.window

        if objects_collected == 1: #and player.position == self.ether_position:
            window.blit(one, position_objects_display)
            #window.blit(ETHER_IMAGE, position_objects_display_2)
        elif objects_collected == 2:
            window.blit(reset, position_objects_display)
            window.blit(two, position_objects_display)
        elif objects_collected == 3:
            window.blit(reset, position_objects_display)
            window.blit(three, position_objects_display)    
    