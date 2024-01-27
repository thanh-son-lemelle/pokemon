from Button import *
import pygame
import sys
from pygame import *
from pygame.locals import *
import random
from Pokemon import *
import json
from Animation import Animation
from Dresseurs import Dresseurs
from Animation_dresseur import Animation_dresseur
import threading



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


        self.liste_poke = []
        self.liste_poke_adv = []
        self.starter = None
        self.adv = None
        self.health_change_speed = 5
        musique = pygame.mixer.music.load(self.__choice_musique)
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)
        self.police = pygame.font.Font("font\Pokemon Classic.ttf", 15)
        self.police_moyen = pygame.font.Font("font\Pokemon Classic.ttf", 20)
        self.police_grande = pygame.font.Font("font\Pokemon Classic.ttf", 40)
        self.text_bulle = pygame.font.Font("font\Pokemon Classic.ttf", 30)
        self.get_nom = None
        self.running = True
        self.nom_dresseur = None

            
    def initialis_combat(self):
        if self.starter is not None:
            self.starter = self.starter
            self.adv = self.adv
            self.animation = Animation(self.starter)
            self.animation.loadFramesForCombat(isFront=False)
            self.animationAdversaire = Animation(self.adv)
            self.animationAdversaire.loadFramesForCombat()
            self.max_hp = self.starter.get_statHp()
            self.max_hp_adv = self.adv.get_statHp()

            self.multiplicateur_degat_adv = 1
            self.multiplicateur_degat = 1
            self.__attaque = ""
                        

            self.hp = self.max_hp 
            self.hp_adv = self.max_hp_adv 

            
            self.ratio = self.hp / self.max_hp
            self.ratio_adv = self.hp_adv / self.max_hp_adv

            
            self.__nom = self.police.render(self.starter.get_nom() + " :", True, "black")
            
            self.__adversaire = self.police.render(self.adv.get_nom() + " :", True, "black")
            self.win = self.police_grande.render("Victoire",True,"white")
            self.loose = self.police_grande.render("Défaite",True,"white")

            self.rater = self.police_moyen.render("L'action a échoué",True,"red")
            self.lvl_start = self.police.render(str(self.starter.get_level()) , True, "black")
            self.lvl_adv = self.police.render(str(self.adv.get_level()), True, "black")
            self.aff_lvl = self.police.render("Lv : ", True, "black")
            
    
        

    def get_liste_dresseurs(self,l,l1):
        for i in l:
              self.liste_poke.append(i)
        for i in l1:
             self.liste_poke_adv.append(i)


    def get_nom_adv(self,adv):
        self.get_nom = adv
        self.nom_dresseur = self.text_bulle.render("Le Dresseur "+self.get_nom+" vous défie.",True,"black")
        

        self.starter = self.liste_poke[0]
        print("Starter : ",self.liste_poke)
        print("Starter : ",self.liste_poke[0].get_nom())

        self.adv = self.liste_poke_adv[0]
        print("Adv : ",self.adv.get_nom())
        


    def fight(self):
      
        self.animation = Animation(self.starter)
        self.animation.loadFramesForCombat(isFront=False)
        self.animationAdversaire = Animation(self.adv)
        self.animationAdversaire.loadFramesForCombat()
        self.__nom = self.police.render(self.starter.get_nom() + " :", True, "black")
        self.__adversaire = self.police.render(self.adv.get_nom() + " :", True, "black")
        self.lvl_start = self.police.render(str(self.starter.get_level()) , True, "black")
        size_capa = (500,200)
        press = False
        capa = pygame.image.load("images\\background\combat\panel.png")
        capa = pygame.transform.scale(capa, size_capa)
        
        
        pygame.display.set_caption("Fight")
        
        

        self.animation.displayBackAnimation()

        self.animationAdversaire.displayFrontAnimation()
                
                
        self.health_bar_player()
        self.health_bar_adv()
        self.animation.clock = pygame.time.Clock()
        rezize_capa_button = (200,50)
        capa_button = pygame.image.load("images\\button\images\\sprite_test3.png")
        capa_button = pygame.transform.scale(capa_button,rezize_capa_button)
        self.vu()
        self.zone_text = pygame.transform.scale(self.zone_text,(500,200))
        while self.running:
            self.__SCREEN.blit(capa, (0, 500))
            self.__SCREEN.blit(self.zone_text,(500,500))
            self.__SCREEN.blit(self.__zone, (0, 0))
            self.__SCREEN.blit(self.__nom, (30, 5))
            self.__SCREEN.blit(self.__adversaire, (700, 5))
            self.__SCREEN.blit(self.aff_lvl,(30,40))
            self.__SCREEN.blit(self.aff_lvl,(700,40))
            self.__SCREEN.blit(self.lvl_start,(90,40))
            self.__SCREEN.blit(self.lvl_adv,(760,40))
            self.animation.displayBackAnimation()

            self.animationAdversaire.displayFrontAnimation()
            self.health_bar_player()
            self.health_bar_adv()
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ATT1 = Button(image= capa_button, pos=(125, 550), 
                                text_input=self.starter.get_4abilities()[0], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT2 = Button(image= capa_button, pos=(125, 650), 
                                text_input=self.starter.get_4abilities()[1], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT3 = Button(image= capa_button, pos=(375, 550), 
                                text_input=self.starter.get_4abilities()[2], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT4 = Button(image= capa_button, pos=(375, 650), 
                                text_input=self.starter.get_4abilities()[3], font=self.police, base_color="#000000", hovering_color="White")


            for button in [ATT1,ATT2,ATT3,ATT4]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.__SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

            

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ATT1.checkForInput(MENU_MOUSE_POS) and not press:
                        press = True
                        self.__attaque = self.starter.get_4abilities()[0]
                        self.multiplicateur_type()


                    if ATT2.checkForInput(MENU_MOUSE_POS) and not press:
                            press = True
                            self.__attaque = self.starter.get_4abilities()[1]
                            if self.__attaque == "-":
                                self.fight()

                            self.multiplicateur_type()



                    if ATT3.checkForInput(MENU_MOUSE_POS) and not press:
                            press = True
                            self.__attaque = self.starter.get_4abilities()[2]
                            if self.__attaque == "-":
                                self.fight()
                            self.multiplicateur_type()



                    if ATT4.checkForInput(MENU_MOUSE_POS) and not press:
                            press = True
                            self.__attaque = self.starter.get_4abilities()[3]
                            if self.__attaque == "-":
                                self.fight()
                            self.multiplicateur_type()
                        

                
                elif event.type == pygame.MOUSEBUTTONUP:
                    if  ATT1.checkForInput(MENU_MOUSE_POS):
                        press = False


                    if  ATT2.checkForInput(MENU_MOUSE_POS):
                        press = False


                    if  ATT3.checkForInput(MENU_MOUSE_POS):
                        press = False

                    if  ATT4.checkForInput(MENU_MOUSE_POS):
                        press = False

                    pygame.display.flip()

            pygame.display.flip() 
            self.animation.clock.tick(self.animation.FPS)
                

            





    def health_bar_player(self):
        
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.__SCREEN, (255,255,255), (30, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (30, 30,250*self.ratio, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (30, 30,250, 10),1)

        



    def health_bar_adv(self):
        
        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(self.__SCREEN, (255,255,255), (700, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (700, 30,250*self.ratio_adv, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (700, 30,250, 10),1)





        
                   


    def lvl_up(self):
        if self.starter.get_level() <= 5:
            self.starter.set_xp(1000)
            print(self.starter.get_level())

        elif 10 >= self.starter.get_level() <= 16:
            self.starter.set_xp(300)
            print(self.starter.get_level())
            


        elif 16 >=self.starter.get_level() <= 30:
            self.starter.set_xp(150)
            print(self.starter.get_level())


        elif 30 >=self.starter.get_level() <= 50:
            self.starter.set_xp(100)
            print(self.starter.get_level())
        
        elif 50 >=self.starter.get_level():
            self.starter.set_xp(30)
            print(self.starter.get_level())



    def Victoire(self):
        pygame.mixer.music.stop()
        pygame.display.update()
        pygame.display.set_caption("Win Menu")
        size_capa = (1000, 700)
        Back = pygame.image.load("images\\background\menu\Win.jpg")
        Back = pygame.transform.scale(Back, size_capa)
        self.__SCREEN.blit(Back, (0, 0))
        self.__SCREEN.blit(self.win, (50, 10))
        pygame.display.update()

        while self.running:
            MENU_MOUSE_POS = pygame.mouse.get_pos()


            REPLAY_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(100, 130), 
                                text_input="REPLAY", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")
            
            MENU_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(100, 230), 
                                text_input="MENU", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(50, 330), 
                                text_input="QUIT", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")


            for button in [REPLAY_BUTTON, MENU_BUTTON,QUIT_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.__SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()




                if event.type == pygame.MOUSEBUTTONDOWN:

                    if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        print("Test liste : ",self.liste_poke)
                        # self.choix_pokemon()
                       


                    if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                         self.running = False
                        
                            



                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()

                        sys.exit()
                            


            pygame.display.update()



    def Defaite(self):
        pygame.mixer.music.stop()
        self.max_hp_adv = self.adv.get_statHp()
        self.hp_adv = self.max_hp_adv
        pygame.display.update()
        pygame.display.set_caption("Loose Menu")
        size_capa = (1000, 700)
        Back = pygame.image.load("images\\background\menu\Loose.jpg")
        Back = pygame.transform.scale(Back, size_capa)
        self.__SCREEN.blit(Back, (0, 0))
        self.__SCREEN.blit(self.loose, (150, 100))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


        
        

    def multiplicateur_type(self):
        delay_time = 1000
        self.start_time = pygame.time.get_ticks()
        i = 0 # set d'un numéro à utiliser plus tard dans la fonction

        degats = 0  # set des dégâts subit à 0

        less_press = 0 # set de la baisse de precision à 0 
        
        degats_stat = 0 # set des dégat des staut à 0 (poison,brulure,etc...)

        capa_adv = self.adv.get_4abilities()[random.randint(0,3)]
        while capa_adv == "-": # Si l'adverssaire choissis une compétance non definie
            capa_adv = self.adv.get_4abilities()[random.randint(0,3)]
             
        size_capa = (1000,200)
        capa = pygame.image.load("images\\background\combat\panel.png")
        capa = pygame.transform.scale(capa, size_capa)


        probabilite_reussite = self.starter.get_abilityAccuracyByName(self.__attaque) 
        nombre_aleatoire = random.uniform(0, 100)

        if probabilite_reussite >= nombre_aleatoire: #Si taux de reussite est supérieure au nombre aléatoire l'attque est reussi 

            # Verif du type d'attaques du joueur = Physique , Special ou Statut

            if self.starter.get_abilityCategoryByName(self.__attaque) == "Physique":
                #Calcul des dégats que va subir l'adverssaire 
                degats = int((((((self.starter.get_level() * 0.4 + 2) * self.starter.get_statAttack() * self.starter.get_abilityPowerByName(self.__attaque)) / self.adv.get_statDefense()) / 50) + 2))

            elif self.starter.get_abilityCategoryByName(self.__attaque) == "Special":
                #Calcul des dégats que va subir l'adverssaire 
                degats = int((((((self.starter.get_level() * 0.4 + 2) *self.starter.get_statSpecialAttack() * self.starter.get_abilityPowerByName(self.__attaque)) / self.adv.get_statSpecialDefense()) / 50) + 2))

                
            elif self.starter.get_abilityCategoryByName(self.__attaque) == "Statut":
                if self.starter.get_abilityStatutChangeByName(self.__attaque) == "Empoisonnement":
                    #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                    degats_stat += 10 

                elif self.starter.get_abilityStatutChangeByName(self.__attaque) == "Brûlure":
                    #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                    degats_stat = 10

                elif self.starter.get_abilityStatutChangeByName(self.__attaque) == "Baisse de Précision":
                    #set de la reduction de precision du pokemon adverse 
                    less_press = 10

            
             # Verif du type d'attaques de l'adverssaire = Physique , Special ou Statut
            
            if self.adv.get_abilityCategoryByName(capa_adv) == "Physique":
                #Calcul des dégats que va subir le joueur 
                degats = int((((((self.adv.get_level() * 0.4 + 2) * self.adv.get_statAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statDefense()) / 50) + 2)+ degats_stat)

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Special":
                #Calcul des dégats que va subir le joueur 
                degats = int((((((self.adv.get_level() * 0.4 + 2) *self.adv.get_statSpecialAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statSpecialDefense()) / 50) + 2)+ degats_stat)

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Statut":
                #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                if self.adv.get_abilityStatutChangeByName(capa_adv) == "Empoisonnement":
                    degats_stat += 10 

                elif self.adv.get_abilityStatutChangeByName(capa_adv) == "Brûlure":
                        #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                        degats_stat = 10

                elif self.adv.get_abilityStatutChangeByName(capa_adv) == "Baisse de Précision":
                    #set de la reduction de precision du pokemon Joueur 
                    less_press = 10

            #Ajout de l'avantage type
            with open("data\pokemons\Type.json","r") as f: 
                file = json.load(f)
                #Calcul avantage type des capacité du joueur
                self.multiplicateur_degat = file[self.starter.get_abilityTypeByName(self.__attaque)][self.adv.get_type1()]* file[self.starter.get_abilityTypeByName(self.__attaque)][self.adv.get_type2()]

                #Mettre la valeurs des hp à jour pour la rappeler plus tard dans health_bar_adv
                self.hp_adv -= degats * self.multiplicateur_degat + degats_stat
                
                #Calcul avantage type des capacité de l'adverssaire
                self.multiplicateur_degat_adv = file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type1()]* file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type2()]

                #Mettre la valeurs des hp à jour pour la rappeler plus tard dans health_bar_player
                self.hp -= degats * self.multiplicateur_degat_adv
                        
                       
                


                #Condition changement de pokemon après K.O
                
                if self.hp_adv <= 0:
                                self.vu()
                                self.liste_poke_adv.pop(i) #Retirer le pokemon actuel
                                self.hp_adv = 0 # Si pv inferiure à 0 --> les set à 0
                                self.health_bar_player() #Afficher barre de vie player
                                self.health_bar_adv() #Afficher barre de vie Adversse

                                


                                # Reset les pv au max

                                self.max_hp_adv = self.adv.get_statHp()
                                self.hp_adv = self.max_hp_adv 
                                self.ratio_adv = self.hp_adv / self.max_hp_adv  


                                if len(self.liste_poke_adv) >= 1: #Si l'equipe pokemon possède un autres pokemon
                                    self.adv = self.liste_poke_adv[i] #Set le pokemon
                                    self.fight() #Retour au Combat

                                if len(self.liste_poke_adv) <=0: #Si aucun pokemon restant 
                                    self.lvl_up() #Gagne xp
                                    self.Victoire() #Ecran de Victoire

                if self.hp <= 0:
                                self.vu()
                                self.liste_poke.pop(i) # Retirer le pokemon actuel
                                self.hp = 0 # Si pv inferiure à 0 --> les set à 0
                                self.health_bar_player() #Afficher barre de vie player
                                self.health_bar_adv() #Afficher barre de vie Adversse

                                

                                # Reset les pv au max

                                self.max_hp = self.starter.get_statHp()
                                self.hp = self.max_hp
                                self.ratio = self.hp / self.max_hp

                                if len(self.liste_poke) >= 1: #Si l'equipe pokemon possède un autres pokemon
                                    self.starter = self.liste_poke[i] #Set le pokemon
                                    self.fight() #Retour au Combat

                                if len(self.liste_poke) <=0: #Si aucun pokemon restant 
                                    self.Defaite() # écran de défaite

                #Mettre à jour les barre de vie à chaque appel de la def 

                if self.hp_adv >= 1 and self.max_hp_adv >= 1:
                    self.ratio = self.hp / self.max_hp
                    self.ratio_adv = self.hp_adv / self.max_hp_adv
                    self.health_bar_player()
                    self.health_bar_adv()

                

        else: # Si l'on rate nôtre attaque 

            
            #Thread pour afficher les message sans freeze la page 
            def perform_delayed_task():
                while pygame.time.get_ticks() - self.start_time < delay_time:
                    self.rater = self.police_moyen.render("L'action a échoué", False, "red")
                    self.__SCREEN.blit(self.rater, (575, 575))
                    
                    
                    pygame.time.Clock().tick(60)

            task_thread = threading.Thread(target=perform_delayed_task)
            task_thread.start()
            

            if self.adv.get_abilityCategoryByName(capa_adv) == "Physique":
                #Calcul des dégats que va subir le joueur 
                degats = int((((((self.adv.get_level() * 0.4 + 2) * self.adv.get_statAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statDefense()) / 50) + 2)+ degats_stat)

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Special":
                #Calcul des dégats que va subir le joueur 
                degats = int((((((self.adv.get_level() * 0.4 + 2) *self.adv.get_statSpecialAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statSpecialDefense()) / 50) + 2)+ degats_stat)

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Statut":
                #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                if self.adv.get_abilityStatutChangeByName(capa_adv) == "Empoisonnement":
                    degats_stat += 10 

                elif self.adv.get_abilityStatutChangeByName(capa_adv) == "Brûlure":
                        #set des degat statut (le pokemon prendra x nombre de dégat en plus à cahque tour)
                        degats_stat = 10

                elif self.adv.get_abilityStatutChangeByName(capa_adv) == "Baisse de Précision":
                    #set de la reduction de precision du pokemon Joueur 
                    less_press = 10


           
            pygame.display.update()

            

            with open("data\pokemons\Type.json","r") as f: 
                file = json.load(f)
                #Calcul avantage type des capacité de l'adverssaire
                self.multiplicateur_degat_adv = file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type1()]* file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type2()]

                #Mettre la valeurs des hp à jour pour la rappeler plus tard dans health_bar_player
                self.hp -= degats * self.multiplicateur_degat_adv


            
            #Condition changement de pokemon après K.O
                
                if self.hp_adv <= 0:
                    self.vu()
                    self.liste_poke_adv.pop(i) #Retirer le pokemon actuel
                    self.hp_adv = 0 # Si pv inferiure à 0 --> les set à 0
                    self.health_bar_player() #Afficher barre de vie player
                    self.health_bar_adv() #Afficher barre de vie Adversse

                    

                    # Reset les pv au max
                    self.max_hp_adv = self.adv.get_statHp()
                    self.hp_adv = self.max_hp_adv 
                    self.ratio_adv = self.hp_adv / self.max_hp_adv 

                    if len(self.liste_poke_adv) >= 1: #Si l'equipe pokemon possède un autres pokemon
                        self.adv = self.liste_poke_adv[i] #Set le pokemon
                        self.fight() #Retour au Combat

                    if len(self.liste_poke_adv) <=0: #Si aucun pokemon restant 
                        self.lvl_up() #Gagne xp
                        self.Victoire() #Ecran de Victoire

                if self.hp <= 0:
                    self.vu()
                    self.liste_poke.pop(i) # Retirer le pokemon actuel
                    self.hp = 0 # Si pv inferiure à 0 --> les set à 0
                    self.health_bar_player() #Afficher barre de vie player
                    self.health_bar_adv() #Afficher barre de vie Adversse

                    

                    # Reset les pv au max
                    self.max_hp = self.starter.get_statHp()
                    self.hp = self.max_hp
                    self.ratio = self.hp / self.max_hp


                    if len(self.liste_poke) >= 1: #Si l'equipe pokemon possède un autres pokemon
                        self.starter = self.liste_poke[i] #Set le pokemon
                        self.fight() #Retour au Combat


                    if len(self.liste_poke) <=0: #Si aucun pokemon restant 
                        self.Defaite() # écran de défaite

            #Mettre à jour les barre de vie à chaque appel de la def 

            if self.hp >= 1 and self.max_hp >= 1:
                    self.ratio = self.hp / self.max_hp
                    self.ratio_adv = self.hp_adv / self.max_hp_adv
                    self.health_bar_player()
                    self.health_bar_adv()
            
          
                



    def vu(self):
    # Étape 1: Lire le fichier JSON existant
        with open("data/pokemons/pokemons.json", "r",encoding="utf-8") as f:
            file = json.load(f)

            for i in file['pokemons']:
                if i["id"] == self.starter.get_id():
                    i["vu"] += 1
                    print(i["vu"])

                if i["id"] == self.adv.get_id():
                    i["vu"] += 1
                    print(i["vu"])

    # Étape 2: Écrire dans le fichier JSON avec l'encodage UTF-8

        with open("data/pokemons/pokemons.json", "w",encoding="utf-8") as f:
            json.dump(file, f, indent=2,ensure_ascii=False)
         



    def start_anim(self):

        animationadversaire = Animation_dresseur()
        animationjoueur = Animation_dresseur()
        animationjoueur.load(isFront = False)
        animationadversaire.load()
        size_zone_text = (1000,200)
        self.zone_text = pygame.image.load("images\\background\menu\TextZone.png")
        self.zone_text = pygame.transform.scale(self.zone_text, size_zone_text)
        NEXT = pygame.image.load("images\\background\menu\\arrow_text.png")
        button_next_size = (30,30)
        NEXT = pygame.transform.scale(NEXT, button_next_size)
        NEXT = pygame.transform.rotate(NEXT,90)
        self.initialis_combat()
        while self.running: 

            self.__SCREEN.blit(self.__zone, (0, 0))
            self.__SCREEN.blit(self.zone_text,(0, 500))
            self.__SCREEN.blit(self.nom_dresseur,(50,520))
            rect = self.nom_dresseur.get_rect()
            pos = rect.topright
            
            self.__SCREEN.blit(NEXT, ((pos[0]+60),(pos[1])+530))
            animationadversaire.displayFrontSprite()
            animationjoueur.displayBackSprite()
            # appel de animation desserur 
            pygame.display.update()
          
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if 0 <= event.pos[0] <= 1000 and 500 <= event.pos[1] <= 700:
                            #revoyer fonction retour d'anim
                            
                            self.fight()