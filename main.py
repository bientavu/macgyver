import pygame
from labyrinth import Labyrinth
from game import Game

pygame.init()
# Make game run 60fps to have smooth movement - 1
clock=pygame.time.Clock()

# Game window displayed
pygame.display.set_caption("Aidez MacGyver à s'échapper")
window = pygame.display.set_mode((450, 480))

# Charging game
game = Game(window)

running = True

# Loop
while running:
    # Make game run 60fps to have smooth movement - 2
    clock.tick(60)

    game.initialization(window)
    game.play()
    # Apply player image
    #window.blit(game.player.image, game.player.rect)

    # Moving the player
    # if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 420:
    #     game.player.move_right()
    # elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
    #     game.player.move_left()
    # elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
    #     game.player.move_up()
    # elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 420:
    #     game.player.move_down()
    
    # Refresh display
    #pygame.display.flip()
        
    # Events management
    for event in pygame.event.get():
            # If player close the window
        if event.type == pygame.QUIT:
            running = False
            # Moving the player by recording keyboard
        # elif event.type == pygame.KEYDOWN:
        #     game.pressed[event.key] = True
        # elif event.type == pygame.KEYUP:
        #     game.pressed[event.key] = False

