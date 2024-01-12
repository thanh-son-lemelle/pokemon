import json 
import pygame
# from class_Pokemon import * 
import sys
from pygame import *
from pygame.locals import *

class Pokedex():
    def __init__(self, id):
        self.__id = id
        # self.__pokemonData = self.loadData()
        self.__name = None
        self.__type = None
        self.__stats = None
        self.__evolution = None
        self.__imageFace = None
        # self.loadData()
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.pokdx = pygame.image.load("images\\pokedex\\pokedex.png")
        self.police = pygame.font.Font("font\Pokemon Classic.ttf", 40)
        self.__nom = self.police.render("Pikachu",True,"black")

    # def loadData(self):
    #     with open(r"data\pokemons\pokemons.json", "r") as fichier:
    #         donnees = json.load(fichier)

    def pokedex(self):
        size = (400,700) 
        self.pokdx = pygame.transform.scale(self.pokdx, size)
        self.fond = pygame.transform.scale(self.fond, (self.WIDTH, self.HEIGHT))
        self.SCREEN.blit(self.fond,(0,0))
        self.SCREEN.blit(self.pokdx, (self.WIDTH//3.5,0))
        self.SCREEN.blit(self.__nom, (360,120))
      
        # musique= pygame.mixer.music.load("musique\main menu\Pokemon BlackWhite Music - Pokemon Center.mp3")
        # mixer.music.set_volume(0.1)
        # mixer.music.play(-1)
        pygame.display.set_caption("Pokedex")
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.flip()

    pygame.init()

pokemon = Pokedex(1)
pokemon.pokedex()