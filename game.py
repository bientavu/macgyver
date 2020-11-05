import pygame
import math
from player import Player
from labyrinth import Labyrinth
from objects import Objects
from constantes import MAC_GYVER_IMAGE, FLOOR_IMAGE, SPRITE_SIZE, SYRINGE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE, MENU_IMAGE, WIN_IMAGE, LOOSE_IMAGE, PLAY_BUTTON

class Game:
    def __init__(self, window):
        self.is_playing = False
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

        self.run = True
        self.response = None

    def menu(self, menu_image, window):
        '''
        Display menu
        '''
        self.menu = pygame.image.load(menu_image).convert_alpha()
        self.window.blit(self.menu, (0, 0))

        play_button = pygame.image.load('assets/playbutton.png')
        play_button = pygame.transform.scale(play_button, (200, 70))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = math.ceil(window.get_width() / 3.333)
        play_button_rect.y = math.ceil(window.get_height() / 1.4)
        window.blit(play_button, play_button_rect)

        continu = True
        while continu:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continu = False
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        continu = False
                        return True

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
                    continu = self.labyrinth.end_game(self.mac_gyver)
                    self.response = self.labyrinth.response(self.mac_gyver, self.objects)

            pygame.display.flip()
        return self.response


    def player_win(self, win_image):
        '''Display Win Screen at the end of the game'''
        self.win_image = pygame.image.load(win_image).convert_alpha()
        self.window.blit(self.win_image, ((0, 0)))

        continu = True
        while continu:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continu = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continu = False
                        return True

    def player_loose(self, loose_image):
        '''Display Loose Screen at the end of the game'''
        self.loose_image = pygame.image.load(loose_image).convert_alpha()
        self.window.blit(self.loose_image, ((0, 0)))

        continu = True
        while continu:
            pygame.display.update()
            for event in pygame.event.get():
                # Waiting for events
                if event.type == pygame.QUIT:
                    continu = False
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        continu = False
                        return True