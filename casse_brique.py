import pygame
largeur_ecran= 800
hauteur_ecran= 600


largeur_raquette=80
hauteur_raquette=10

class Raquette(pygame.sprite.Sprite):
    def__init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur


pygame.init()
pygame.display.set_caption("Casse brique")

screen=pygame.d0isplay.set_mode([largeur_ecran,hauteur_ecran])

running=True
while running:
    for event in pygame.event.get():#pour gerer les events en pygame
        if event.type==pygame.QUIT:
            running=False

    screen.fill('yellow') # pour remplir le fond de la fenetre en noir
    pygame.display.flip()#pour actualiser l'ecran


pygame.quit()


