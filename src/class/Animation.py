import pygame
import os
from Pokemon import Pokemon
import re

class Animation():
    def __init__(self, target) -> None:
        self.Id = target.get_id()
        self.frames = []
        self.delay = []
        self.current_frame = 0
        self.sc_w = 1000
        self.sc_h = 500
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.ospath = os.path.dirname(__file__)
        self.frontSplitGif = os.path.join("images", "sprite_pokemon", "front", "split_gif")
        self.backSplitGif = os.path.join("images", "sprite_pokemon", "back", "split_gif")
        self.backIdRepertory = os.path.join(self.backSplitGif, str(self.Id))
        self.frontIdRepertory = os.path.join(self.frontSplitGif, str(self.Id))
        self.screen = pygame.display.set_mode((self.sc_w, self.sc_h))


    def get_delay(self, isFront = True):
        if isFront:
            for chemin in self.getPath():
                matches = re.findall(r'delay-(\d+\.\d+)s\.gif', chemin)
                if matches:
                    for match in matches:
                        delay_value = float(match)
                        self.delay.append(delay_value)
                    
                else:
                    print("Aucune correspondance trouvée dans front.")
        else:
            for chemin in self.getPath(isFront = False):
                matches = re.findall(r'delay-(\d+\.\d+)s\.gif', chemin)
                if matches:
                    for match in matches:
                        delay_value = float(match)
                        self.delay.append(delay_value)
                    
                else:
                    print("Aucune correspondance trouvée dans back.")
        
        return self.delay

    def getPath(self, isFront = True):
        if isFront:
            fichiers = os.listdir(self.frontIdRepertory)
            chemins_fichiers = [os.path.join(self.frontIdRepertory, fichier) for fichier in fichiers]
            return chemins_fichiers
        else:
            fichiers = os.listdir(self.backIdRepertory)
            chemins_fichiers = [os.path.join(self.backIdRepertory, fichier) for fichier in fichiers]
            return chemins_fichiers


    def resizeImage(self, image, multiplier):
        originalWidth, originalHeight = image.get_size()
        newHeight = int(multiplier * originalHeight)
        newWidth = int(multiplier * originalWidth)
        image = pygame.transform.scale(image, (newWidth, newHeight))
        return image
    
    def loadFrames(self, isFront = True):
    
        if isFront:
            self.get_delay()
            for chemin in self.getPath():
                frame = pygame.image.load(chemin).convert_alpha()
                frame_resized = self.resizeImage(frame, 2)
                self.frames.append(frame_resized)
        else:
            self.get_delay(isFront = False)
            for chemin in self.getPath(isFront = False):
                frame = pygame.image.load(chemin).convert_alpha()
                frame_resized = self.resizeImage(frame, 3)
                self.frames.append(frame_resized)
    
    def displayFrontAnimation(self):
            
            rect = self.frames[self.current_frame].get_rect()
            rect.midbottom = (770,320)
            self.screen.blit(self.frames[self.current_frame], rect)
            self.current_frame += 1
            self.current_frame %= len(self.frames)
            pygame.time.delay(int(self.delay[self.current_frame]*500))
    
    def displayBackAnimation(self): 
            rect = self.frames[self.current_frame].get_rect()
            rect.midbottom = (270,500)
            self.screen.blit(self.frames[self.current_frame], rect)
            self.current_frame += 1
            self.current_frame %= len(self.frames)
            pygame.time.delay(int(self.delay[self.current_frame]*500))

    def delaythread(self, delay):
        pygame.time.delay(delay)
        self.delayFinished = True
        
"""
starter = Pokemon(3)
animation = Animation(starter)
animation.loadFrames(isFront=False)
adversaire = Pokemon(6)
animationAdversaire = Animation(adversaire)
animationAdversaire.loadFrames()




pygame.init()


screen = pygame.display.set_mode((animation.sc_w, animation.sc_h))
animation.clock = pygame.time.Clock()
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()


    bg = pygame.image.load("images\\background\\combat\\sprite_combat_background02.png")
    bg = pygame.transform.scale(bg, (animation.sc_w, animation.sc_h))
    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    animation.displayBackAnimation()

    animationAdversaire.displayFrontAnimation()


    
        

    pygame.display.flip()
    animation.clock.tick(animation.FPS)
"""