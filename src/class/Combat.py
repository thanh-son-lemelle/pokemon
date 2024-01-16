from Button import *
import pygame
import sys
from pygame import *
from pygame.locals import *
import random
from Pokemon import *

class Combat():

    def __init__(self):
        pygame.init()
        self.__WIDTH = 1000
        self.__HEIGHT = 700
        self.__SCREEN = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__fond = ["images\\background\combat\sprite_combat_background01.png","images\\background\combat\sprite_combat_background02.png","images\\background\combat\sprite_combat_background03.png","images\\background\combat\sprite_combat_background04.png","images\\background\combat\sprite_combat_background05.png","images\\background\combat\sprite_combat_background06.png","images\\background\combat\sprite_combat_background07.png","images\\background\combat\sprite_combat_background08.png","images\\background\combat\sprite_combat_background09.png","images\\background\combat\sprite_combat_background10.png","images\\background\combat\sprite_combat_background11.png"]
        self.__choice = random.choice(self.__fond)
        self.__arene = pygame.image.load(self.__choice)
        self.__size_image = (1000,500)
        self.__zone = pygame.transform.scale(self.__arene, self.__size_image)
        self.__liste_musique = ["musique\combat\Pokémon Black & White - Critical Health Music (HQ).mp3","musique\combat\Pokémon Diamond, Pearl & Platinum - Champion Cynthia Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Primal Kyogre & Groudon Battle Music (HQ).mp3","musique\combat\Pokémon Omega Ruby & Alpha Sapphire - Zinnia Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Kieran Battle Music (HQ).mp3","musique\combat\Pokémon Scarlet & Violet - Champion Nemona Battle Music (HQ)(1).mp3","musique\combat\Pokémon Sun & Moon - Battle Legend Red & Blue Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Rival Gladion Battle Music (HQ).mp3","musique\combat\Pokémon Sun & Moon - Team Skull Leader Guzma Battle Music (HQ).mp3","musique\combat\Pokémon HeartGold & SoulSilver - Champion & Red Battle Music (HQ).mp3","musique\combat\Battle! Gym Leader - Remix Cover (Pokémon Sword and Shield).mp3","musique\combat\Driftveil City Past Paradox (Remix) ► Pokémon Black & White Toothless Dancing.mp3","musique\combat\Red vs Gold (Theme).mp3","musique\combat\Volo Theme (Piano Etude) Pokémon.mp3"]
        self.__choice_musique = random.choice(self.__liste_musique)

        self.max_hp = 250
        self.max_hp_adv = 250

        self.multiplicateur_degat_adv = 1
        self.multiplicateur_degat = 1

        self.hp = self.max_hp 
        self.hp_adv = self.max_hp_adv 

        self.ratio = self.hp / self.max_hp
        self.ratio_adv = self.hp_adv / self.max_hp_adv

        self.police = pygame.font.Font("font\Pokemon Classic.ttf", 10)
        self.__nom = self.police.render(starter.get_nom() + " :", True, "black")#remplacer nom par le get_nom pokemon 
        self.__adversaire = self.police.render(adv.get_nom() + " :", True, "black")
        






    def fight(self):
        size_capa = (1000,200)
        press = False
        capa = pygame.image.load("images\\background\combat\panel.png")
        capa = pygame.transform.scale(capa, size_capa)
        
        jouer = True
        pygame.display.set_caption("Fight")
        musique = pygame.mixer.music.load(self.__choice_musique)
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)

        
        self.__SCREEN.blit(capa, (0, 500))
        self.__SCREEN.blit(self.__zone, (0, 0))
        self.__SCREEN.blit(starter.get_imageBack(),(150,290))
        self.__SCREEN.blit(self.__nom, (30, 10))
        self.__SCREEN.blit(self.__adversaire, (700, 10))
        self.__SCREEN.blit(adv.get_imageFace(),(650,120))
        self.health_bar()

        while jouer:

            
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ATT1 = Button(image=pygame.image.load("images\\button\images\\sprite_test3.png"), pos=(250, 550), 
                                text_input=starter.get_4abilities()[0], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT2 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(250, 650), 
                                text_input=starter.get_4abilities()[1], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT3 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(750, 550), 
                                text_input=starter.get_4abilities()[2], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT4 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(750, 650), 
                                text_input=starter.get_4abilities()[3], font=self.police, base_color="#000000", hovering_color="White")


            for button in [ATT1,ATT2,ATT3,ATT4]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.__SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if ATT1.checkForInput(MENU_MOUSE_POS) and not press:
                    self.hp_adv -= 30
                    print(self.hp_adv)
                    press = True
                    self.ratio = self.hp / self.max_hp
                    self.ratio_adv = self.hp_adv / self.max_hp_adv
                    if self.hp_adv < 0:
                        self.hp_adv = 0
                        print(self.hp_adv)
                    self.health_bar()
                    


            elif event.type == pygame.MOUSEBUTTONUP:
                if  ATT1.checkForInput(MENU_MOUSE_POS):
                    press = False




                    




                ##if ATT2.checkForInput(MENU_MOUSE_POS):

                
                    

                #if ATT3.checkForInput(MENU_MOUSE_POS):


                #if ATT4.checkForInput(MENU_MOUSE_POS):

                    


                pygame.display.flip()

            pygame.display.flip() 





    def health_bar(self):
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.__SCREEN, (255,255,255), (30, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (30, 30,250*self.ratio, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (30, 30,250, 10),1)

        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(self.__SCREEN, (255,255,255), (700, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (700, 30,250*self.ratio_adv, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (700, 30,250, 10),1)



    def update_hp_adversse(self):
        self.degats_subi_adverssaire = self.degats_effectuer 


    def update_degats(self):
        self.degats_effectuer = 100 





        '''import random #gere le taux de reussite des attaques (à adapter)

        probabilite_reussite = 0.75
        nombre_aleatoire = random.uniform(0, 1)

        if nombre_aleatoire <= probabilite_reussite:
            print("L'action a réussi!")
        else:
            print("L'action a échoué.")'''
                   


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


        if type_attaque_pokemon == "Feu" and type_pokemon_adv == "Plante":
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Feu" and type_pokemon_adv == "Glace":
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Feu" and type_pokemon_adv == "Insecte":
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------


        #-----------------------------Eau-------------------------------------

        elif type_attaque_pokemon == "Eau" and type_pokemon_adv == "Feu":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Eau" and type_pokemon_adv == "Roche":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Eau" and type_pokemon_adv == "Sol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------
            


        #-----------------------------Plante----------------------------------


        elif type_attaque_pokemon == "Plante" and type_pokemon_adv == "Eau":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Plante" and type_pokemon_adv == "Roche":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Plante" and type_pokemon_adv == "Sol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------
            

        #-----------------------------Combat----------------------------------


        elif type_attaque_pokemon == "Combat" and type_pokemon_adv == "Glace":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Combat" and type_pokemon_adv == "Roche":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Combat" and type_pokemon_adv == "Normal":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------
            


        #-----------------------------Dragon----------------------------------


        elif type_attaque_pokemon == "Dragon" and type_pokemon_adv == "Dragon":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        #---------------------------------------------------------------------
            


        #-----------------------------Electrick----------------------------------


        elif type_attaque_pokemon == "Electrik" and type_pokemon_adv == "Eau":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Electrik" and type_pokemon_adv == "Vol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------
            

        #-----------------------------Glace----------------------------------


        elif type_attaque_pokemon == "Glace" and type_pokemon_adv == "Dragon":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Glace" and type_pokemon_adv == "Plante":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Glace" and type_pokemon_adv == "Sol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Glace" and type_pokemon_adv == "Vol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------
            



        #-----------------------------Insecte----------------------------------


        elif type_attaque_pokemon == "Insecte" and type_pokemon_adv == "Poison":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Insecte" and type_pokemon_adv == "Plante":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Insecte" and type_pokemon_adv == "Psy":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------
            



        #-----------------------------Poisson----------------------------------


        elif type_attaque_pokemon == "Poison" and type_pokemon_adv == "Insecte":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Poison" and type_pokemon_adv == "Plante":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        #---------------------------------------------------------------------
            


        #-----------------------------Psy----------------------------------


        elif type_attaque_pokemon == "Psy" and type_pokemon_adv == "Poison":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Psy" and type_pokemon_adv == "Combat":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------
    



        #-----------------------------Roche----------------------------------


        elif type_attaque_pokemon == "Roche" and type_pokemon_adv == "Feu":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Roche" and type_pokemon_adv == "Glace":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        elif type_attaque_pokemon == "Roche" and type_pokemon_adv == "Insecte":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Roche" and type_pokemon_adv == "Vol":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------
    
        #-----------------------------Sol----------------------------------


        elif type_attaque_pokemon == "Sol" and type_pokemon_adv == "Feu":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Sol" and type_pokemon_adv == "Electrik":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 


        elif type_attaque_pokemon == "Sol" and type_pokemon_adv == "Poison":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        elif type_attaque_pokemon == "Sol" and type_pokemon_adv == "Roche":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------

        #-----------------------------Spectre----------------------------------


        elif type_attaque_pokemon == "Spectre" and type_pokemon_adv == "Spectre":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 
        
        #---------------------------------------------------------------------
        
        #-----------------------------Vol----------------------------------


        elif type_attaque_pokemon == "Vol" and type_pokemon_adv == "Insecte":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        
        elif type_attaque_pokemon == "Vol" and type_pokemon_adv == "Plante":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        elif type_attaque_pokemon == "Vol" and type_pokemon_adv == "Combat":
        
            self.multiplicateur_degat = 2
            degat_recu = degat_attaque * self.multiplicateur_degat - defense_pokemon_adv
            self.hp_adv -= degat_recu
            self.multiplicateur_degat = 1 

        #---------------------------------------------------------------------
        
        
        #---------------------------------------------------------------------
        #-----------------------------Défensif--------------------------------
        #---------------------------------------------------------------------
        
        
        #---------------------------------------------------------------------
        #-----------------------------Inefficace------------------------------
        #---------------------------------------------------------------------'''
            


        


random_id = random.randint(1,20)
adv = Pokemon (random_id)
starter = Pokemon(4)
starter.set_level(30)


combat = Combat()
combat.fight()


