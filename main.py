import pygame
from labyrinth import Labyrinth
from game import Game
from constantes import MENU_IMAGE, WIN_IMAGE, LOOSE_IMAGE

def main():
    pygame.init()

    # Game window displayed
    pygame.display.set_caption("Aidez MacGyver à s'échapper")
    window = pygame.display.set_mode((450, 480))

    # Charging game
    game = Game(window)
    game.menu(MENU_IMAGE, window)

    running = True

    # Loop
    while running:

        game.initialization(window)
        init = game.play()

        if init:
            game.player_win(WIN_IMAGE)
        else:
            game.player_loose(LOOSE_IMAGE)
        running = game.run

if __name__ == "__main__":
    main()