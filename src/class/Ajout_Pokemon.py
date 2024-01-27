import pygame
import sys
import json
import os

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
        self.BG = pygame.image.load("images\\background\\menu\\Fond pokemon.jpg")
        self.__playgame = False
        self.__descriptif = None
        self.__typeg = None
        self.__stats = None
        self.__affHp = None
        self.__affAttack = None
        self.__affDefense = None
        self.__affSpeed = None
        self.__affvu = None
        self.__id = None
        self.__nom = []
        self.__description = []
        self.__type1 = []
        self.__type2 = []
        self.__infostats = []
        self.__hp = []
        self.__attack = []
        self.__defense = []
        self.__speed = []
        self.__vu = []
        self.__currentPos = 1
        self.pokdx = pygame.image.load("images\\pokedex\\pokedex.png")
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.__descriptif = self.police_medium.render("Descriptif :", True, "black")
        self.__typeg = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")
        self.__affHp = self.police_small.render("Hp : ", True, "black")
        self.__affAttack = self.police_small.render("Attack : ", True, "black")
        self.__affDefense = self.police_small.render("Defense : ", True, "black")
        self.__affSpeed = self.police_small.render("Speed : ", True, "black")
        self.__affvu = self.police_small.render("Pokemon apperçu : ", True, "black")
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (100, 100))
        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.fond = pygame.transform.scale(self.fond, (1000, 700))
        self.pokdx = pygame.image.load("images\\pokedex\\pokedex.png")
        self.pokdx = pygame.transform.scale(self.pokdx, (1000, 700))

    

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
        self.BG = pygame.image.load("images\\background\\menu\\Fond pokemon.jpg")
        self.__playgame = False
        self.__descriptif = None
        self.__typeg = None
        self.__stats = None
        self.__affHp = None
        self.__affAttack = None
        self.__affDefense = None
        self.__affSpeed = None
        self.__affvu = None
        self.__id = None
        self.__nom = []
        self.__description = []
        self.__type1 = []
        self.__type2 = []
        self.__infostats = []
        self.__hp = []
        self.__attack = []
        self.__defense = []
        self.__speed = []
        self.__vu = []
        self.__currentPos = 1
        self.pokdx = pygame.image.load(os.path.join("images", "background", "menu", "ajoutPokemonBackground.webp"))
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_medium_small = pygame.font.Font("font\\Pokemon Classic.ttf", 16)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.__descriptif = self.police_medium.render("Descriptif :", True, "black")
        self.__typeg = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")
        self.__affHp = self.police_small.render("Hp : ", True, "black")
        self.__affAttack = self.police_small.render("Atk : ", True, "black")
        self.__affDefense = self.police_small.render("Def : ", True, "black")
        self.__affSpeed = self.police_small.render("Spd : ", True, "black")
        self.__affSpAttack = self.police_small.render("Sp-Atk : ", True, "black")
        self.__affSpDefense = self.police_small.render("Sp-Def : ", True, "black")
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (100, 100))
        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.fond = pygame.transform.scale(self.fond, (1000, 700))
        self.pokdx = pygame.transform.scale(self.pokdx, (self.WIDTH, self.HEIGHT))

    

#===============================================================================
#                               display ajout pokedex
#===============================================================================
    # methode qui affiche la page d'ajout d'un pokemon dans le fichier pokemon.json
        
    def displayAjoutPokemon(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.SCREEN.blit(self.pokdx, (0, 0))
            self.SCREEN.blit(self.__descriptif, (330, 370))
            self.SCREEN.blit(self.__typeg, (70, 645))
            self.SCREEN.blit(self.__stats, (810, 130))
            self.SCREEN.blit(self.__affHp, (820, 150))
            self.SCREEN.blit(self.__affAttack, (820, 170))
            self.SCREEN.blit(self.__affDefense, (820, 190))
            self.SCREEN.blit(self.__affSpeed, (820, 210))
            self.SCREEN.blit(self.__affSpAttack, (820, 230))
            self.SCREEN.blit(self.__affSpDefense, (820, 250))
            self.SCREEN.blit(self.button_menu, (875, 5))
            

            pygame.display.flip()

screen = AjoutPokemon()
screen.displayAjoutPokemon()