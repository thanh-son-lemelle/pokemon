import pygame
import sys
from pygame import *
from pygame.locals import *
import random

class Combat():

    def __init__(self):
        pygame.init()
        self.__WIDTH = 1000
        self.__HEIGHT = 700
        self.__SCREEN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__fond = ["images\\background\combat\sprite_combat_background01.png","images\\background\combat\sprite_combat_background02.png","images\\background\combat\sprite_combat_background03.png","images\\background\combat\sprite_combat_background04.png","images\\background\combat\sprite_combat_background05.png","images\\background\combat\sprite_combat_background06.png","images\\background\combat\sprite_combat_background07.png","images\\background\combat\sprite_combat_background08.png","images\\background\combat\sprite_combat_background09.png","images\\background\combat\sprite_combat_background10.png","images\\background\combat\sprite_combat_background11.png"]
        self.__choice = random.choice(self.__fond)
        self.__arene = pygame.image.load(self.__choice)
        self.__size_image = (self.__WIDTH,self.__HEIGHT)
        self.__zone = pygame.transform.scale(self.__arene, self.__size_image)
        self.__liste_musique = ["musique\combat\Pokémon Black & White - Critical Health Music (HQ).mp3","musique\combat\Pokémon Diamond, Pearl & Platinum - Champion Cynthia Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Primal Kyogre & Groudon Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Zinnia Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Kieran Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Nemona Battle Music (HQ)(1).mp3","musique\combat\Pokémon Sun & Moon - Battle Legend Red & Blue Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Rival Gladion Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Team Skull Leader Guzma Battle Music (HQ).mp3","musique\combat\Pokémon HeartGold & SoulSilver - Champion & Red Battle Music (HQ).mp3"]
        self.__choice_musique = random.choice(self.__liste_musique)
        self.max_hp = 250
        self.multiplicateur_degat = 1
        self.degats_effectuer = 0 * self.multiplicateur_degat
        self.hp = self.max_hp - self.degats_effectuer
        self.ratio = self.hp / self.max_hp
        self.degats_subi_joueur = 0 #Créer une conditions si degat subis == hp max --> pokemon ko --> Victoire/defaites
        self.degats_subi_adverssaire = 0 #Créer une conditions si degat subis == hp max --> pokemon ko --> Victoire/defaites
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
        print("Degat subi adv : ",self.degats_subi_adverssaire," , Degats effectuer : ",self.degats_effectuer)
        self.update_degats()
        
        while jouer:
            self.__SCREEN.blit(self.__zone, (0, 0))
            self.__SCREEN.blit(self.__nom, (30, 10))
            self.__SCREEN.blit(self.__adversaire, (700, 10))

            self.update_degats()
            self.update_hp_adversse()

            self.health_bar()
            print("Degat subi adv : ",self.degats_subi_adverssaire," , Degats effectuer : ",self.degats_effectuer)
            print("Multiplicateur adverssaire : ",self.multiplicateur_adverssaire," , HP : ",self.hp)
            pygame.display.update() 
            
            
            for events in event.get():
                

                if events.type == QUIT:

                    jouer=False

                    quit()



    def health_bar(self):
            #Joueur
            pygame.draw.rect(self.__SCREEN, "white", (30, 30, 250, 10))
            pygame.draw.rect(self.__SCREEN, "green", (30, 30,self.multiplicateur_joueur*self.ratio, 10))
            pygame.draw.rect(self.__SCREEN, "black", (30, 30,250, 10),1)

            #Pokémon
            pygame.draw.rect(self.__SCREEN, "white", (700, 30, 250, 10))
            pygame.draw.rect(self.__SCREEN, "green", (700, 30,self.multiplicateur_adverssaire*self.ratio, 10))
            pygame.draw.rect(self.__SCREEN, "black", (700, 30,250, 10),1)



    def update_hp_adversse(self):
        self.degats_subi_adverssaire = self.degats_effectuer 


    def update_degats(self):
        self.degats_effectuer = 100 
                   


    '''def lvl_up(self):
        if "level du pokemon" < 5:
            xp_gagner += 1000
            if xp_gagner >= 100:
                lvl +=1

        elif 10 >"level du pokemon" < 16:
            xp_gagner += 300
            if xp_gagner >= 100:
                lvl +=1


        elif 16 >"level du pokemon" < 30:
            xp_gagner += 150
            if xp_gagner >= 100:
                lvl +=1


        elif 30 >"level du pokemon" < 50:
            xp_gagner += 100
            if xp_gagner >= 100:
                lvl +=1
        
        elif 50 >"level du pokemon":
            xp_gagner += 30
            if xp_gagner >= 100:
                lvl +=1'''
    


    '''def multiplicateur_type(self):


        #---------------------------------------------------------------------
        #-----------------------------Offensif--------------------------------
        #---------------------------------------------------------------------


        #-----------------------------Feu-------------------------------------


        if type_pokemon_joueur == "Feu" and type_pokemon_adv == "Plante":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Feu" and type_pokemon_adv == "Glace":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Feu" and type_pokemon_adv == "Insecte":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------


        #-----------------------------Eau-------------------------------------

        elif type_pokemon_joueur == "Eau" and type_pokemon_adv == "Feu":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Eau" and type_pokemon_adv == "Roche":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Eau" and type_pokemon_adv == "Sol":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------
            


        #-----------------------------Plante----------------------------------


        elif type_pokemon_joueur == "Plante" and type_pokemon_adv == "Eau":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Plante" and type_pokemon_adv == "Roche":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Plante" and type_pokemon_adv == "Sol":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------
            

        #-----------------------------Combat----------------------------------


        elif type_pokemon_joueur == "Combat" and type_pokemon_adv == "Glace":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Combat" and type_pokemon_adv == "Roche":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Combat" and type_pokemon_adv == "Normal":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------
            


        #-----------------------------Dragon----------------------------------


        elif type_pokemon_joueur == "Dragon" and type_pokemon_adv == "Dragon":
            self.multiplicateur_degat = 2 
        
        #---------------------------------------------------------------------
            


        #-----------------------------Electrick----------------------------------


        elif type_pokemon_joueur == "Electrik" and type_pokemon_adv == "Eau":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Electrik" and type_pokemon_adv == "Vol":
            self.multiplicateur_degat = 2 

        #---------------------------------------------------------------------
            

        #-----------------------------Glace----------------------------------


        elif type_pokemon_joueur == "Glace" and type_pokemon_adv == "Dragon":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Glace" and type_pokemon_adv == "Plante":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Glace" and type_pokemon_adv == "Sol":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Glace" and type_pokemon_adv == "Vol":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------
            



        #-----------------------------Insecte----------------------------------


        elif type_pokemon_joueur == "Insecte" and type_pokemon_adv == "Poison":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Insecte" and type_pokemon_adv == "Plante":
            self.multiplicateur_degat = 2 

        elif type_pokemon_joueur == "Insecte" and type_pokemon_adv == "Psy":
            self.multiplicateur_degat = 2 

        #---------------------------------------------------------------------
            



        #-----------------------------Poisson----------------------------------


        elif type_pokemon_joueur == "Poison" and type_pokemon_adv == "Insecte":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Poison" and type_pokemon_adv == "Plante":
            self.multiplicateur_degat = 2 


        #---------------------------------------------------------------------
            


        #-----------------------------Psy----------------------------------


        elif type_pokemon_joueur == "Psy" and type_pokemon_adv == "Poison":
            self.multiplicateur_degat = 2 
        
        elif type_pokemon_joueur == "Psy" and type_pokemon_adv == "Combat":
            self.multiplicateur_degat = 2 

        #---------------------------------------------------------------------'''
            


        




combat = Combat()
combat.fight()


