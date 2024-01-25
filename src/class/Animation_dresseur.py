import pygame
import os
from Dresseurs import Dresseurs
import random

class Animation_dresseur():

    def __init__(self) -> None:

        self.chemin_fichiers = []
        self.image = None
        self.frames = []   
        self.current_frame = 0
        self.sc_w = 1000
        self.sc_h = 500
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.ospath = os.path.dirname(__file__)
        self.spriteEnnemies = os.path.join("images", "sprite_characters", "ennemies")
        self.spriteJoueur = os.path.join("images", "sprite_characters", "player","male")
        self.screen = pygame.display.set_mode((self.sc_w, self.sc_h))
        self.postionDepartAdversaire = -200
        self.postionDepartJoueur = 1200
        self.nextStep = False
    
    def get_path(self, isFront = True):
        if isFront:
            fichiers = os.listdir(self.spriteEnnemies)
            self.chemins_fichiers = [os.path.join(self.spriteEnnemies, fichier) for fichier in fichiers]
            return self.chemins_fichiers
        else:
            fichiers = os.listdir(self.spriteJoueur)
            self.chemins_fichiers = [os.path.join(self.spriteJoueur, fichier) for fichier in fichiers]
            return self.chemins_fichiers
        
    def load(self, isFront = True):
        if isFront:
            chemin = random.choice(self.get_path())
            if chemin.endswith(".png"):
                self.image = pygame.image.load(chemin).convert()
                self.image.set_colorkey(self.image.get_at((0,0)))
                self.image = pygame.transform.scale(self.image, (200, 200))
            else:
                print("Aucune correspondance trouvée dans front.")
            
        else:
            self.get_path(isFront = False)
            for chemin in self.chemins_fichiers:
                if chemin.endswith(".png"):
                    self.image = pygame.image.load(chemin).convert()
                    self.image.set_colorkey(self.image.get_at((0,0)))
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.frames.append(self.image)         
            self.image = self.frames[0]   

    def displayFrontSprite(self):

        if self.postionDepartAdversaire < 770:
            self.postionDepartAdversaire +=7
        

        rect = self.image.get_rect()
        rect.midbottom = (self.postionDepartAdversaire, 320) 
        self.screen.blit(self.image, rect)
        


    def displayBackSprite(self):

        if self.postionDepartJoueur > 270:
            self.postionDepartJoueur -=7
        

        rect = self.image.get_rect()
        rect.midbottom = (self.postionDepartJoueur, 500) 
        self.screen.blit(self.image, rect)

    def test(self):
        self.image = self.frames[2]
        rect = self.image.get_rect()
        rect.midbottom = (270, 500)
        self.screen.blit(self.image, rect)
        

    def displayLancerPokeball(self):


        if self.current_frame < len(self.frames):
            rect = self.image.get_rect()
            rect.midbottom = (270, 500)
            self.screen.blit(self.frames[self.current_frame], rect)
            self.current_frame += 1
            pygame.time.delay(int(0.3*500))
        elif self.current_frame == len(self.frames) and self.postionDepartJoueur == 1200:
            self.postionDepartJoueur = 270

            
        elif self.current_frame == len(self.frames) and -200 < self.postionDepartJoueur <= 270:
            self.postionDepartJoueur -=7
            rect = self.image.get_rect()
            rect.midbottom = (self.postionDepartJoueur, 500)
            self.screen.blit(self.image, rect)
        else:
            self.nextStep = True
        return




    


"""
adversaire = Dresseurs()
joueur = Dresseurs()    
animationadversaire = Animation_dresseur()
animationjoueur = Animation_dresseur()
animationjoueur.load(isFront = False)

animationadversaire.load()
pygame.init()


screen = pygame.display.set_mode((animationjoueur.sc_w, animationjoueur.sc_h))
animationjoueur.clock = pygame.time.Clock()
running = True

while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()


    bg = pygame.image.load("images\\background\\combat\\sprite_combat_background02.png")
    bg = pygame.transform.scale(bg, (animationjoueur.sc_w, animationjoueur.sc_h))
    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    if animationjoueur.nextStep == False:
        animationadversaire.displayFrontSprite()
        
        animationjoueur.displayBackSprite()
        if animationadversaire.nextStep == True:
        animationjoueur.displayLancerPokeball()




    
    pygame.display.flip()
    animationjoueur.clock.tick(animationjoueur.FPS)
    """