import pygame
from labyrinth import Labyrinth
from game import Game

pygame.init()
clock=pygame.time.Clock()
#Génération fenetre du jeu
pygame.display.set_caption("Aidez MacGyver à s'échapper")
window = pygame.display.set_mode((450, 450))

game = Game()

running = True

#Boucle
while running:
    clock.tick(60)

    game.init(window)

    #appliquer l'image de mon joueur
    window.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP):
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN):
        game.player.move_down()
    
    #mettre à jour l'écran
    pygame.display.flip()
        
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()
            # elif event.key == pygame.K_UP:
            #     game.player.move_up()
            # elif event.key == pygame.K_DOWN:
            #     game.player.move_down()


