import pygame
largeur_ecran= 800
hauteur_ecran= 600


largeur_raquette=80
hauteur_raquette=10

class Raquette (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((largeur_raquette,hauteur_raquette))
        self.surf.fill((0,255,0))
        self.rect=self.surf.get_rect()
        self.rect.x=largeur_ecran /2 -largeur_ecran/2
        self.rect.y=hauteur_ecran/2- 2*  hauteur_ecran





pygame.init()
pygame.display.set_caption("Casse brique")

screen=pygame.display.set_mode([largeur_ecran,hauteur_ecran])



ma_raquette=Raquette()





running=True
while running:
    for event in pygame.event.get():#pour gerer les events en pygame
        if event.type==pygame.QUIT:
            running=False

    screen.fill('yellow') # pour remplir le fond de la fenetre en noir
    pygame.display.flip()#pour actualiser l'ecran


pygame.quit()


