import pygame
from labyrinth import Labyrinth
from playgame import Playgame

pygame.init()

#Génération fenetre du jeu
pygame.display.set_caption("Aidez MacGyver à s'échapper")
window = pygame.display.set_mode((450, 450))


#charger jeu
labyrinth = Labyrinth()
labyrinth.display_level(window)

running = True

#Boucle
while running:

    #appliquer l'image de mon joueur
    #window.blit(playgame.player.image, playgame.player.rect)
    #mettre à jour l'écran
    pygame.display.flip()
        
        # si le joueur ferme cette fenetre
    for event in pygame.event.get():
            # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False


