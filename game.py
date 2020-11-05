import pygame
from player import Player
from labyrinth import Labyrinth
from objects import Objects
from constantes import MAC_GYVER_IMAGE, FLOOR_IMAGE, SPRITE_SIZE, SYRINGE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE

class Game:
    def __init__(self, window):
        self.window = window
        # self.pressed = {}

    def initialization(self, window):
        '''
        Initialise new objects when call
        '''
        self.labyrinth = Labyrinth()
        self.mac_gyver = Player(MAC_GYVER_IMAGE, FLOOR_IMAGE, self.labyrinth, self.window)
        self.mac_gyver.position = [0, 0]
        self.objects = Objects(SYRINGE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE, self.labyrinth, self.window)

        # Labyrinth
        self.labyrinth.labyrinth_construction()
        self.labyrinth.display_level(window)
        
        # Player
        self.mac_gyver.blit(self.mac_gyver.position)

        #Objects
        self.objects.generate_random_position()
        self.objects.display_objects()
        self.objects.objects_collected = 0


    def play(self):
        '''Manage all input player's input'''
        continu = True
        while continu:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continu = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.mac_gyver.move("right")
                    elif event.key == pygame.K_LEFT:
                        self.mac_gyver.move("left")
                    elif event.key == pygame.K_UP:
                        self.mac_gyver.move("up")
                    elif event.key == pygame.K_DOWN:
                        self.mac_gyver.move("down")
                    self.objects.collect_objects(self.mac_gyver)

            pygame.display.flip()
