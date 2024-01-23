from Button import *
import pygame
import sys
from pygame import *
from pygame.locals import *
import random
from Pokemon import *
import json
from Animation import Animation



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


        self.starter = Pokemon(8)
        self.max_hp = self.starter.get_statHp()
        random_id = random.randint(1,20)
        self.adv = Pokemon(random_id)


        self.animation = Animation(self.starter)
        self.animation.loadFrames(isFront=False)
        self.animationAdversaire = Animation(self.adv)
        self.animationAdversaire.loadFrames()

        self.max_hp_adv = self.adv.get_statHp()

        self.multiplicateur_degat_adv = 1
        self.multiplicateur_degat = 1
        self.__attaque = ""
                    

        self.hp = self.max_hp 
        self.hp_adv = self.max_hp_adv 

        
        self.ratio = self.hp / self.max_hp
        self.ratio_adv = self.hp_adv / self.max_hp_adv

        self.police = pygame.font.Font("font\Pokemon Classic.ttf", 10)
        self.police_moyen = pygame.font.Font("font\Pokemon Classic.ttf", 20)
        self.police_grande = pygame.font.Font("font\Pokemon Classic.ttf", 40)
        self.__nom = self.police.render(self.starter.get_nom() + " :", True, "black")
        
        self.__adversaire = self.police.render(self.adv.get_nom() + " :", True, "black")
        self.win = self.police_grande.render("Victoire",True,"white")
        self.loose = self.police_grande.render("Défaite",True,"white")

        self.rater = self.police_moyen.render("L'action a échoué",True,"red")
        self.lvl_start = self.police.render(str(self.starter.get_level()) , True, "black")
        self.lvl_adv = self.police.render(str(self.adv.get_level()), True, "black")
        self.aff_lvl = self.police.render("Lv : ", True, "black")
        self.liste_poke = [3,5,5]
        self.liste_poke_adv = []
    
        




    def fight(self):
        self.max_hp_adv = self.adv.get_statHp()
        self.hp_adv = self.max_hp_adv 
        self.ratio_adv = self.hp_adv / self.max_hp_adv
        self.starter.set_level(10)
        self.__nom = self.police.render(self.starter.get_nom() + " :", True, "black")
        self.__adversaire = self.police.render(self.adv.get_nom() + " :", True, "black")
        self.lvl_start = self.police.render(str(self.starter.get_level()) , True, "black")
        self.max_hp = self.starter.get_statHp()
        self.hp = self.max_hp
        self.ratio = self.hp / self.max_hp
        size_capa = (1000,200)
        press = False
        capa = pygame.image.load("images\\background\combat\panel.png")
        capa = pygame.transform.scale(capa, size_capa)
        
        jouer = True
        pygame.display.set_caption("Fight")
        musique = pygame.mixer.music.load(self.__choice_musique)
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)
        

        self.animation.displayBackAnimation()

        self.animationAdversaire.displayFrontAnimation()
                
                
        
        self.animation.clock = pygame.time.Clock()
        self.vu()
        while jouer:
            self.__SCREEN.blit(capa, (0, 500))
            self.__SCREEN.blit(self.__zone, (0, 0))
            self.__SCREEN.blit(self.__nom, (30, 10))
            self.__SCREEN.blit(self.__adversaire, (700, 10))
            self.__SCREEN.blit(self.aff_lvl,(30,40))
            self.__SCREEN.blit(self.aff_lvl,(700,40))
            self.__SCREEN.blit(self.lvl_start,(60,40))
            self.__SCREEN.blit(self.lvl_adv,(730,40))
            self.animation.displayBackAnimation()

            self.animationAdversaire.displayFrontAnimation()
            self.health_bar()
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            ATT1 = Button(image=pygame.image.load("images\\button\images\\sprite_test3.png"), pos=(250, 550), 
                                text_input=self.starter.get_4abilities()[0], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT2 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(250, 650), 
                                text_input=self.starter.get_4abilities()[1], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT3 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(750, 550), 
                                text_input=self.starter.get_4abilities()[2], font=self.police, base_color="#000000", hovering_color="White")
            
            ATT4 = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(750, 650), 
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
                

            





    def health_bar(self):
        # Dessiner la barre de vie du joueur
        pygame.draw.rect(self.__SCREEN, (255,255,255), (30, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (30, 30,250*self.ratio, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (30, 30,250, 10),1)

        # Dessiner la barre de vie de l'adversaire
        pygame.draw.rect(self.__SCREEN, (255,255,255), (700, 30, 250, 10))
        pygame.draw.rect(self.__SCREEN, (0,255,0), (700, 30,250*self.ratio_adv, 10))
        pygame.draw.rect(self.__SCREEN, (0,0,0), (700, 30,250, 10),1)





        
                   


    def lvl_up(self):
        if self.starter.get_level() <= 5:
            self.starter.set_xp(1000)
            print(self.starter.get_level())

        elif 10 > self.starter.get_level() <= 16:
            self.starter.set_xp(300)
            print(self.starter.get_level())
            


        elif 16 >self.starter.get_level() <= 30:
            self.starter.set_xp(150)
            print(self.starter.get_level())


        elif 30 >self.starter.get_level() <= 50:
            self.starter.set_xp(100)
            print(self.starter.get_level())
        
        elif 50 >self.starter.get_level():
            self.starter.set_xp(30)
            print(self.starter.get_level())



    def Victoire(self):
        pygame.display.update()
        pygame.display.set_caption("Win Menu")
        size_capa = (1000, 700)
        Back = pygame.image.load("images\\background\menu\Win.jpg")
        Back = pygame.transform.scale(Back, size_capa)
        self.__SCREEN.blit(Back, (0, 0))
        self.__SCREEN.blit(self.win, (50, 10))
        pygame.display.update()

        while True:
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
                        self.choix_pokemon()
                       


                    #if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                        
                            



                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()

                        sys.exit()
                            


            pygame.display.update()



    def Defaite(self):
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
        i = 0
        less_press = 0
        degats_stat = 0
        capa_adv = self.adv.get_4abilities()[random.randint(0,3)]
        while capa_adv == "-":
            capa_adv = self.adv.get_4abilities()[random.randint(0,3)]
             
        size_capa = (1000,200)
        capa = pygame.image.load("images\\background\combat\panel.png")
        capa = pygame.transform.scale(capa, size_capa)


        probabilite_reussite = self.starter.get_abilityAccuracyByName(self.__attaque) 
        nombre_aleatoire = random.uniform(0, 100)

        if probabilite_reussite >= nombre_aleatoire:

            if self.starter.get_abilityCategoryByName(self.__attaque) == "Physique":
                degats = int((((((self.starter.get_level() * 0.4 + 2) * self.starter.get_statAttack() * self.starter.get_abilityPowerByName(self.__attaque)) / self.adv.get_statDefense()) / 50) + 2))

            elif self.starter.get_abilityCategoryByName(self.__attaque) == "Special":
                degats = int((((((self.starter.get_level() * 0.4 + 2) *self.starter.get_statSpecialAttack() * self.starter.get_abilityPowerByName(self.__attaque)) / self.adv.get_statSpecialDefense()) / 50) + 2))


            #elif = status --> if feu / poison / etc ... ---> baise hp de x hp par tour (fonction a dupliquer pour l'adv)
                
            elif self.starter.get_abilityCategoryByName(self.__attaque) == "Statut":
                if self.starter.get_abilityStatutChangeByName == "Empoisonnement":
                    degats_stat += 10 

                elif self.starter.get_abilityStatutChangeByName == "Brûlure":
                    degats_stat = 10

                elif self.starter.get_abilityStatutChangeByName == "Baisse de Précision":
                    less_press = 10


            if self.adv.get_abilityCategoryByName(capa_adv) == "Physique":
                degats = int((((((self.adv.get_level() * 0.4 + 2) * self.adv.get_statAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statDefense()) / 50) + 2)+ degats_stat)

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Special":
                degats = int((((((self.adv.get_level() * 0.4 + 2) *self.adv.get_statSpecialAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statSpecialDefense()) / 50) + 2)+ degats_stat)


            with open("data\pokemons\Type.json","r") as f: 
                file = json.load(f)
                self.multiplicateur_degat = file[self.starter.get_abilityTypeByName(self.__attaque)][self.adv.get_type1()]* file[self.starter.get_abilityTypeByName(self.__attaque)][self.adv.get_type2()]
                self.hp_adv -= degats * self.multiplicateur_degat + degats_stat

                self.multiplicateur_degat_adv = file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type1()]* file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type2()]
                self.hp -= degats * self.multiplicateur_degat_adv


                self.ratio = self.hp / self.max_hp
                self.ratio_adv = self.hp_adv / self.max_hp_adv
                self.health_bar()
                
                if self.hp_adv <= 0:
                                self.vu()
                                self.hp_adv = 0
                                self.lvl_up()
                                self.health_bar()
                                self.Victoire()

                if self.hp <= 0:
                                self.vu()
                                self.liste_poke.pop(i)
                                self.hp = 0
                                self.health_bar()
                                if len(self.liste_poke) >= 1:
                                    self.starter = Pokemon(self.liste_poke[i])
                                    self.fight()
                                self.max_hp_adv = self.hp_adv
                                if len(self.liste_poke) <=0: 
                                    self.Defaite()

        else:

            if self.adv.get_abilityCategoryByName(capa_adv) == "Physique":
                degats = int((((((self.adv.get_level() * 0.4 + 2) * self.adv.get_statAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statDefense()) / 50) + 2))

            elif self.adv.get_abilityCategoryByName(capa_adv) == "Special":
                degats = int((((((self.adv.get_level() * 0.4 + 2) *self.adv.get_statSpecialAttack() * self.adv.get_abilityPowerByName(capa_adv)) / self.starter.get_statSpecialDefense()) / 50) + 2))


            self.rater = self.police_moyen.render("L'action a échoué", False, "red")
            self.__SCREEN.blit(self.rater, (150, 250))
            pygame.display.update()

            delay_time = 1000
            start_time = pygame.time.get_ticks()

            with open("data\pokemons\Type.json","r") as f: 
                file = json.load(f)
                self.multiplicateur_degat_adv = file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type1()]* file[self.adv.get_abilityTypeByName(capa_adv)][self.starter.get_type2()]
                self.hp -= degats * self.multiplicateur_degat_adv


            self.ratio = self.hp / self.max_hp
            self.ratio_adv = self.hp_adv / self.max_hp_adv
            self.health_bar()
            
            if self.hp_adv <= 0:
                                self.vu()
                                self.hp_adv = 0
                                self.lvl_up()
                                self.health_bar()
                                self.Victoire()

            if self.hp <= 0:
                            self.vu()
                            self.liste_poke.pop(i)
                            self.hp = 0
                            self.health_bar()
                            if len(self.liste_poke) >= 1:
                                self.starter = Pokemon(self.liste_poke[i])
                                self.fight()
                            self.max_hp_adv = self.hp_adv
                            if len(self.liste_poke) <=0: 
                                self.Defaite()

            while pygame.time.get_ticks() - start_time < delay_time:
                self.__SCREEN.blit(capa, (0, 500))
                self.__SCREEN.blit(self.__zone, (0, 0))
                self.__SCREEN.blit(self.starter.get_imageBack(),(150,290))
                self.__SCREEN.blit(self.__nom, (30, 10))
                self.__SCREEN.blit(self.__adversaire, (700, 10))
                self.__SCREEN.blit(self.adv.get_imageFace(),(650,120))
                self.__SCREEN.blit(self.aff_lvl,(30,40))
                self.__SCREEN.blit(self.aff_lvl,(700,40))
                self.__SCREEN.blit(self.lvl_start,(60,40))
                self.__SCREEN.blit(self.lvl_adv,(730,40))
                self.health_bar()
                pygame.time.Clock().tick(60)



    def choix_pokemon(self):
        pygame.display.set_caption("Choix Pokemon")
        pygame.display.update()

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()


            REPLAY_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(100, 130), 
                                text_input="???", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")
            
            MENU_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(100, 230), 
                                text_input="???", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=pygame.image.load("images\\button\images\sprite_test3.png"), pos=(50, 330), 
                                text_input="???", font=self.police_moyen, base_color="#d7fcd4", hovering_color="White")


            for button in [REPLAY_BUTTON, MENU_BUTTON,QUIT_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.__SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        num1 = random.randint(1,20)
                        self.starter = Pokemon(num1)
                        self.liste_poke.append(num1)
                        self.animation = Animation(self.starter)
                        self.animation.loadFrames(isFront=False)
                        self.fight()
                       


                    if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                        num2 = random.randint(1,20)
                        self.liste_poke.append(num2)
                        self.starter = Pokemon(num2)
                        self.animation = Animation(self.starter)
                        self.animation.loadFrames(isFront=False)
                        self.fight()
                        
                            



                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        num3 = random.randint(1,20)
                        self.liste_poke.append(num3)
                        self.starter = Pokemon(num3)
                        self.animation = Animation(self.starter)
                        self.animation.loadFrames(isFront=False)
                        self.fight()
                            


            pygame.display.update()


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

        with open("data/pokemons/pokemons.json", "w",encoding="utf-8") as f:
            json.dump(file, f, indent=2,ensure_ascii=False)
         

        

                    


        
        


        
            


        





combat = Combat()
combat.fight()


