import json 
import pygame
# from class_Pokemon import * 
import sys
from pygame import *
from pygame.locals import *

pygame.init()

class Pokedex():
    def __init__(self, id):
        self.__id = id
        # self.__pokemonData = self.loadData()
        self.__name = None
        self.__type = None
        self.__stats = None
        self.__descriptif = None
        self.__evolution = None
        self.__imageFace = None
        # self.loadData()
        self.WIDTH = 1000
        self.HEIGHT = 700
       
        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.pokdx = pygame.image.load("images\\pokedex\\pokedex.png")
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf",12)
        self.__descriptif = self.police_medium.render("Descriptif :", True, "black")
        self.__type = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")
        
    # def loadData(self):
    #     with open(r"data\pokemons\pokemons.json", "r") as fichier:
    #         donnees = json.load(fichier)
    
    def loadDescription(self):

        with open(r'data\\pokedex\\description.json', 'r', encoding='utf-8') as file:
            pokemonsDescription = json.load(file)

        for pokemon in pokemonsDescription:
            return pokemon['id'], pokemon['nom'], pokemon['description']

    def affichePokedex(self):

        size = (400,700) 
        self.pokdx = pygame.transform.scale(self.pokdx, size)
        self.fond = pygame.transform.scale(self.fond, (self.WIDTH, self.HEIGHT))
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.SCREEN.blit(self.fond,(0,0))
        self.SCREEN.blit(self.pokdx, (self.WIDTH//3.5,0))
        self.SCREEN.blit(self.__descriptif, (330,350))
        self.SCREEN.blit(self.police_larger.render(pokedex.loadDescription()[1] ,True,"black"), (360,120))
        self.SCREEN.blit(self.__type, (330,520))
        self.SCREEN.blit(self.police_small.render(pokedex.loadDescription()[2], True, "black"), (330, 390))
        self.SCREEN.blit(self.__stats, (420, 570))

        # musique= pygame.mixer.music.load("musique\main menu\Pokemon BlackWhite Music - Pokemon Center.mp3")
        # mixer.music.set_volume(0.1)
        # mixer.music.play(-1)

    
        pygame.display.set_caption("Pokedex")
        
        pygame.display.update()

        current_pos = [0, 0]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        current_pos[0] += 1
                        
                    elif event.key == pygame.K_LEFT:
                        current_pos[0] -= 1
                       
          

   
pokedex = Pokedex(1)
pokedex.affichePokedex()
print(pokedex.loadDescription())

