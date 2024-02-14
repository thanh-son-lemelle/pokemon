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
        self.sc_h = 700
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.ospath = os.path.dirname(__file__)
        self.frontSplitGif = os.path.join("images", "sprite_pokemon", "front", "split_gif")
        self.backSplitGif = os.path.join("images", "sprite_pokemon", "back", "split_gif")
        self.backIdRepertory = os.path.join(self.backSplitGif, str(self.Id))
        self.frontIdRepertory = os.path.join(self.frontSplitGif, str(self.Id))
        self.screen = pygame.display.set_mode((self.sc_w, self.sc_h))


#===============================================================================
#                               Animation pokémon 
#                                General methode
#================================================================================
    # Méthode pour obtenir les délais des frames
    def get_delay(self, isFront = True):
        if isFront:
            for chemin in self.getPath():
                # Findall utilise un pattern pour recuperer le delay
                matches = re.findall(r'delay-(\d+\.\d+)s\.gif', chemin)
                if matches:
                    for match in matches:
                        delay_value = float(match)
                        self.delay.append(delay_value)

        else:
            for chemin in self.getPath(isFront = False):
                matches = re.findall(r'delay-(\d+\.\d+)s\.gif', chemin)
                if matches:
                    for match in matches:
                        delay_value = float(match)
                        self.delay.append(delay_value)
                    
    # Méthode pour obtenir les chemins des fichiers d'images
    def getPath(self, isFront = True):
        if isFront:
            fichiers = os.listdir(self.frontIdRepertory)
            chemins_fichiers = [os.path.join(self.frontIdRepertory, fichier) for fichier in fichiers]
            return chemins_fichiers
        else:
            fichiers = os.listdir(self.backIdRepertory)
            chemins_fichiers = [os.path.join(self.backIdRepertory, fichier) for fichier in fichiers]
            return chemins_fichiers

    # Méthode pour redimensionner une image
    def resizeImage(self, image, multiplier):
        originalWidth, originalHeight = image.get_size()
        newHeight = int(multiplier * originalHeight)
        newWidth = int(multiplier * originalWidth)
        image = pygame.transform.scale(image, (newWidth, newHeight))
        return image
    
    
#===============================================================================
#                               Animation pokémon 
#                             Display Pour Combat
#================================================================================
    # Méthode pour charger les frames pour le combat
    def loadFramesForCombat(self, isFront = True):
    
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
    # Affiche l'animation du pokémon adverse
    def displayFrontAnimation(self):
            
            rect = self.frames[self.current_frame].get_rect()
            rect.midbottom = (770,320)
            self.screen.blit(self.frames[self.current_frame], rect)
            self.current_frame += 1
            self.current_frame %= len(self.frames)
            pygame.time.delay(int(self.delay[self.current_frame]*500))
    # Affiche l'animation du pokémon du joueur
    def displayBackAnimation(self): 
            rect = self.frames[self.current_frame].get_rect()
            rect.midbottom = (270,500)
            self.screen.blit(self.frames[self.current_frame], rect)
            self.current_frame += 1
            self.current_frame %= len(self.frames)
            pygame.time.delay(int(self.delay[self.current_frame]*500))


#===============================================================================
#                               Animation pokémon 
#                             Display Pour Choix Pokémon
#================================================================================
            # Méthode pour charger les frames pour le choix du pokémon
    def loadFramesForPokeball(self):
            self.background = pygame.image.load(os.path.join("images", "background", "menu", "Area icon.png")).convert_alpha()
            self.background = pygame.transform.scale(self.background, (100, 130))
            self.background = pygame.transform.rotate(self.background, 90)

            self.get_delay()
            for chemin in self.getPath():
                frame = pygame.image.load(chemin).convert_alpha()
                frame_resized = self.resizeImage(frame, 1)
                self.frames.append(frame_resized)

    # Affiche l'animation du pokémon dans un cadre
    def displayPokemonForPokeball(self, X, Y):
        rect = self.background.get_rect()
        rect.center = (X, Y)
        self.screen.blit(self.background, rect)
        rect = self.frames[self.current_frame].get_rect()
        rect.center = (X, Y)
        self.screen.blit(self.frames[self.current_frame], rect)
        self.current_frame += 1
        self.current_frame %= len(self.frames)
        pygame.time.delay(int(self.delay[self.current_frame]*1000))
#===============================================================================
