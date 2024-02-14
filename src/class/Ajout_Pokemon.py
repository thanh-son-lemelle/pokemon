import pygame
import sys
import json
import os
import tkinter as tk
from tkinter import filedialog

from Button import Button
from TextInput import TextInputBox
from Dropdown_menu import DropdownMenu

NOIR = (0, 0, 0)    

#===============================================================================
#                               display ajout pokedex
#===============================================================================
    # methode qui affiche la page d'ajout d'un pokemon dans le fichier pokemon.json
class AjoutPokemon():
    def __init__(self):
        self.__ospath = os.path.dirname(__file__)
        self.__pokedexPath = os.path.join(self.__ospath, "data", "pokemons", "pokemon.json")
        self.__descriptionPath = os.path.join(self.__ospath, "data", "pokedex", "pokedex.json")
        
        pygame.init()
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.white = (255 , 255 , 255)
        self.displayImage = False
        self.BG = pygame.image.load("images\\background\\menu\\Fond pokemon.jpg")
        self.__imagePokemon = None
        self.pokdx = pygame.image.load(os.path.join("images", "background", "menu", "ajoutPokemonBackground.webp"))
        
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.police_smallsmall = pygame.font.Font("font\\Pokemon Classic.ttf", 8)
        
        self.__descriptif = self.police_medium.render("Descriptif :", True, "black")
        self.__affId = self.police_medium.render("Id : ", True, "black")
        self.__affname = self.police_medium.render("Nom : ", True, "black")
        self.__typeg = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")
        self.__affcomp = self.police_medium.render("Compétences : ", True, "black")
        
        self.__tablcomp = [
                            ["Cpt 0 : ", "Cpt 1 : ", "Cpt 2 : ",],
                            ["Cpt 3 : ", "Cpt 4 : ", "Cpt 5 : ",],
                            ["Cpt 6 : ", "Cpt 7 : ", "Cpt 8 : ",],
                            ["Cpt 9 : ", "Cpt 10 : ", "Cpt 11 : ",],
                            ["Cpt 12 : ", "Cpt 13 : ", "Cpt 14 : ",],
                            ]
        self.__tabllvl = [ ["Lvl : ", "Lvl : ", "Lvl : ",],
                            ["Lvl : ", "Lvl : ", "Lvl : ",],
                            ["Lvl : ", "Lvl : ", "Lvl : ",],
                            ["Lvl : ", "Lvl : ", "Lvl : ",],
                            ["Lvl : ", "Lvl : ", "Lvl : ",],
                            ]
        self.__cellule_largeur = 60
        self.__cellule_largeurlvl = 35
        self.__cellule_hauteur = 20
        self.__margeHauteur = 10
        self.__margeLargeur = 180
        self.__margeLargeurlvl = 200
        self.__x = 20
        self.__xlvl = -300
        self.__y = 340
        self.__ylvl = 340
        
        self.__affHp = self.police_small.render("Hp : ", True, "black")
        self.__affAttack = self.police_small.render("Atk : ", True, "black")
        self.__affDefense = self.police_small.render("Def : ", True, "black")
        self.__affSpeed = self.police_small.render("Spd : ", True, "black")
        self.__affSpAttack = self.police_small.render("Sp-Atk : ", True, "black")
        self.__affSpDefense = self.police_small.render("Sp-Def : ", True, "black")
        self.__affEvol1 = self.police_small.render("Evolution 1 : ", True, "black")
        self.__affEvol2 = self.police_small.render("Evolution 2 : ", True, "black")
        self.__affEvol3 = self.police_small.render("Evolution 3 : ", True, "black")
        
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (100, 100))
        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.fond = pygame.transform.scale(self.fond, (1000, 700))
        self.pokdx = pygame.transform.scale(self.pokdx, (self.WIDTH, self.HEIGHT))
        self.__fontbutton = pygame.image.load("images\\button\\images\\button main.png")
        self.__fontbutton = pygame.transform.scale(self.__fontbutton, (200, 50))
        self.__loadImageBUTTON = Button(image=self.__fontbutton, pos=(115, 167), 
                                        text_input="Load Image", font=self.police_small, base_color="#d7fcd4", hovering_color="white")
        
        self.input_box_name = TextInputBox(320, 148, 140, 32)
        self.input_box_id = TextInputBox(620, 148, 100, 32)
        self.__input_box_hp = TextInputBox(900, 170, 50, 24)
        self.__input_box_attack = TextInputBox(900, 200, 50, 24)
        self.__input_box_defense = TextInputBox(900, 230, 50, 24)
        self.__input_box_speed = TextInputBox(900, 260, 50, 24)
        self.__input_box_spAttack = TextInputBox(900, 290, 50, 24)
        self.__input_box_spDefense = TextInputBox(900, 320, 50, 24)
        self.__input_box_evol1 = TextInputBox(850, 500, 50, 32)
        self.__input_box_evol2 = TextInputBox(850, 560, 50, 32)
        self.__input_box_evol3 = TextInputBox(850, 620, 50, 32)
        self.__input_description = TextInputBox(40, 540, 300, 100, 24)
        self.__dropdown = DropdownMenu(0, 0, 80, 16)

        self.previousPage = False

    

    #===============================================================================
    #                               display ajout pokedex
    #===============================================================================
    # methode qui affiche la page d'ajout d'un pokemon dans le fichier pokemon.json
        
    def displayAjoutPokemon(self):
        running = True
        while running:

            if isinstance(self.__imagePokemon, str):
                self.__imagePokemon = pygame.image.load(self.__imagePokemon)
                self.displayImage = True
                
            MOUSE_POS = pygame.mouse.get_pos()
            for button in [self.__loadImageBUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(self.SCREEN)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__loadImageBUTTON.checkForInput(MOUSE_POS):
                        self.displayImage = False
                        self.__imagePokemon = self.choisirImage()
                       
                        
                self.input_box_name.handle_event(event)
                self.input_box_id.handle_event(event)
                self.__input_box_hp.handle_event(event)
                self.__input_box_attack.handle_event(event)
                self.__input_box_defense.handle_event(event)
                self.__input_box_speed.handle_event(event)
                self.__input_box_spAttack.handle_event(event)
                self.__input_box_spDefense.handle_event(event)
                self.__input_box_evol1.handle_event(event)
                self.__input_box_evol2.handle_event(event)
                self.__input_box_evol3.handle_event(event)
                self.__input_description.handle_event(event)
                self.__dropdown.handle_event(event)


            # Effacer l'écran
            self.SCREEN.fill(NOIR)

            self.SCREEN.blit(self.pokdx, (0, 0))
            if self.displayImage:
                self.SCREEN.blit(self.__imagePokemon, (80, 200))
            self.__loadImageBUTTON.update(self.SCREEN)

            for i, ligne in enumerate(self.__tablcomp):
                for j, cellule in enumerate(ligne):
                    pygame.draw.rect(self.SCREEN, NOIR, (self.__x + j * (self.__cellule_largeur + self.__margeLargeur), self.__y + i * (self.__cellule_hauteur + self.__margeHauteur), self.__cellule_largeur, self.__cellule_hauteur), 2)
                    texte_surface = self.police_smallsmall.render(cellule, True, NOIR)
                    texte_rect = texte_surface.get_rect(center=(self.__x + j * (self.__cellule_largeur + self.__margeLargeur) + self.__cellule_largeur // 2,
                                                                self.__y + i * (self.__cellule_hauteur + self.__margeHauteur) + self.__cellule_hauteur // 2))
                    self.SCREEN.blit(texte_surface, texte_rect)

            for i, ligne in enumerate(self.__tabllvl):
                for j, cellule in enumerate(ligne):
                    pygame.draw.rect(self.SCREEN, NOIR, (self.__xlvl + j * (self.__cellule_largeurlvl + self.__margeLargeurlvl) + 500, self.__ylvl + i * (self.__cellule_hauteur + self.__margeHauteur), self.__cellule_largeurlvl, self.__cellule_hauteur), 2)
                    texte_surface = self.police_smallsmall.render(cellule, True, NOIR)
                    texte_rect = texte_surface.get_rect(center=(self.__xlvl + j * (self.__cellule_largeurlvl + self.__margeLargeurlvl) + self.__cellule_largeurlvl // 2 + 500,
                                                                self.__ylvl + i * (self.__cellule_hauteur + self.__margeHauteur) + self.__cellule_hauteur // 2))
                    self.SCREEN.blit(texte_surface, texte_rect)



            self.SCREEN.blit(self.__descriptif, (40, 500))
            self.SCREEN.blit(self.__affname, (230, 140))
            self.__dropdown.draw(self.SCREEN)
            self.input_box_name.update()
            self.input_box_name.draw(self.SCREEN)
            self.input_box_id.draw(self.SCREEN)
            self.input_box_id.update()
            self.__input_box_hp.update()
            self.__input_box_hp.draw(self.SCREEN)
            self.__input_box_attack.update()
            self.__input_box_attack.draw(self.SCREEN)
            self.__input_box_defense.update()
            self.__input_box_defense.draw(self.SCREEN)
            self.__input_box_speed.update()
            self.__input_box_speed.draw(self.SCREEN)
            self.__input_box_spAttack.update()
            self.__input_box_spAttack.draw(self.SCREEN)
            self.__input_box_spDefense.update()
            self.__input_box_spDefense.draw(self.SCREEN)
            self.__input_box_evol1.update()
            self.__input_box_evol1.draw(self.SCREEN)
            self.__input_box_evol2.update()
            self.__input_box_evol2.draw(self.SCREEN)
            self.__input_box_evol3.update()
            self.__input_box_evol3.draw(self.SCREEN)
            self.__input_description.update()
            self.__input_description.draw(self.SCREEN)


            self.SCREEN.blit(self.__affId, (560, 140))
            self.SCREEN.blit(self.__affcomp, (40, 290))
            self.SCREEN.blit(self.__typeg, (70, 645))
            self.SCREEN.blit(self.__stats, (810, 130))
            self.SCREEN.blit(self.__affHp, (800, 170))
            self.SCREEN.blit(self.__affAttack, (800, 200))
            self.SCREEN.blit(self.__affDefense, (800, 230))
            self.SCREEN.blit(self.__affSpeed, (800, 260))
            self.SCREEN.blit(self.__affSpAttack, (800, 290))
            self.SCREEN.blit(self.__affSpDefense, (800, 320))
            self.SCREEN.blit(self.__affEvol1, (820, 480))
            self.SCREEN.blit(self.__affEvol2, (820, 540))
            self.SCREEN.blit(self.__affEvol3, (820, 600))
            self.SCREEN.blit(self.button_menu, (875, 5))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        
                        if 875 <= event.pos[0] <= 1000 and 5 <= event.pos[1] <= 105:
                            self.previousPage = True
                            running = False
            

            pygame.display.flip()



    #===============================================================================
    #                               Méthode pour choisir une image
    #===============================================================================
            
    def choisirImage(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path
    


    def get_previousPage(self):
        return self.previousPage
