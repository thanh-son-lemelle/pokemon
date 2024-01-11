import pygame
import sys
from pygame import *
from pygame.locals import *
import random
from Menu import *

class Combat():

    def __init__(self):
        pygame.init()
        self.__WIDTH = 722
        self.__HEIGHT = 541
        self.__SCREEN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__fond = ["images\\background\combat\sprite_combat_background01.png","images\\background\combat\sprite_combat_background02.png","images\\background\combat\sprite_combat_background03.png","images\\background\combat\sprite_combat_background04.png","images\\background\combat\sprite_combat_background05.png","images\\background\combat\sprite_combat_background06.png","images\\background\combat\sprite_combat_background07.png","images\\background\combat\sprite_combat_background08.png","images\\background\combat\sprite_combat_background09.png","images\\background\combat\sprite_combat_background10.png","images\\background\combat\sprite_combat_background11.png"]
        self.__choice = random.choice(self.__fond)
        self.__arene = pygame.image.load(self.__choice)
        self.__size_image = (self.__WIDTH,self.__HEIGHT)
        self.__zone = pygame.transform.scale(self.__arene, self.__size_image)
        self.__liste_musique = ["musique\combat\Pokémon Black & White - Critical Health Music (HQ).mp3","musique\combat\Pokémon Diamond, Pearl & Platinum - Champion Cynthia Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Primal Kyogre & Groudon Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Zinnia Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Kieran Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Nemona Battle Music (HQ)(1).mp3","musique\combat\Pokémon Sun & Moon - Battle Legend Red & Blue Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Rival Gladion Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Team Skull Leader Guzma Battle Music (HQ).mp3","musique\combat\Pokémon HeartGold & SoulSilver - Champion & Red Battle Music (HQ).mp3"]
        self.__choice_musique = random.choice(self.__liste_musique)
        self.max_hp = 250
        self.hp = self.max_hp
        self.ratio = self.hp / self.max_hp
        self.degats_subi_joueur = 0 #Créer une conditions si degat subis == hp max --> pokemon ko --> Victoire/defaites
        self.degats_subi_adverssaire = 100 #Créer une conditions si degat subis == hp max --> pokemon ko --> Victoire/defaites
        self.multiplicateur_joueur = int(self.max_hp) - self.degats_subi_joueur
        self.multiplicateur_adverssaire = int(self.max_hp) - self.degats_subi_adverssaire
        self.police = pygame.font.Font("font\Pokemon Classic.ttf", 10)
        self.__nom = self.police.render("Pikachu :", True, "black")
        self.__adversaire = self.police.render("Salamèche :", True, "black")






    def fight(self):
        jouer = True
        pygame.display.set_caption("Fight")
        musique = pygame.mixer.music.load(self.__choice_musique)
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)
        

        while jouer:
            self.__SCREEN.blit(self.__zone, (0, 0))
            self.__SCREEN.blit(self.__nom, (30, 10))
            self.__SCREEN.blit(self.__adversaire, (450, 10))
            self.health_bar()
            pygame.display.update() 
            self.degats_subi_adverssaire = 100
            pygame.display.update() 
            
            for events in event.get():
                

                if events.type == QUIT:

                    jouer=False

                    quit()



    def health_bar(self):
            #Joueur
            pygame.draw.rect(self.__SCREEN, "red", (30, 30, 250, 10))
            pygame.draw.rect(self.__SCREEN, "green", (30, 30,self.multiplicateur_joueur*self.ratio, 10))
            pygame.draw.rect(self.__SCREEN, "black", (30, 30,250, 10),1)

            #Pokémon
            pygame.draw.rect(self.__SCREEN, "black", (450, 30, 250, 10))
            pygame.draw.rect(self.__SCREEN, "green", (450, 30,self.multiplicateur_adverssaire*self.ratio, 10))
            pygame.draw.rect(self.__SCREEN, "black", (450, 30,250, 10),1)
                   



combat = Combat()
combat.fight()


