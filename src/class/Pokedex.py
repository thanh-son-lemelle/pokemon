import json
import pygame
from Pokemon import *
import sys
from pygame import *
from pygame.locals import *


class Pokedex():
    def __init__(self, id):
        pygame.init()
        self.__id = id
        self.__nom = []
        self.__description = []
        self.__type = []
        self.__stats = []
        self.__descriptif = None
        self.__imageFace = None
        self.__evolution = None
        self.__currentPos = 1
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokedex")

        self.fond = pygame.image.load("images\\pokedex\\fond pokedex.jpg")
        self.pokdx = pygame.image.load("images\\pokedex\\pokedex.png")
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.__descriptif = self.police_medium.render("Descriptif :", True, "black")
        self.__type = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")

    def loadDescription(self):
        with open(r'data\\pokedex\\description.json', 'r', encoding='utf-8') as file:
            pokemonsDescription = json.load(file)

        for pokemon in pokemonsDescription['pokemons']:
            self.__nom.append(pokemon['nom'])
            self.__description.append(pokemon['description'])

        return pokemon['id'], self.__nom, self.__description, self.__imageFace, self.__type, self.__stats

    def loadStats(self):
        with open(r'data\\pokemons\\pokemons.json', 'r', encoding='utf-8') as file:
            pokemonsData = json.load(file)

        for pokemon in pokemonsData['pokemons']:
            self.__type.append(pokemon['type'])
            self.__stats.append(pokemon['stats'])

    def loadGif(self, id):
        self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        self.__imageFace = Pokemon.resizeImage(self, self.__imageFace, 150)  # à voir si Utile ou pas
        return self.__imageFace

    def recupereDescriptionById(self, id):
        self.loadDescription()
        currentDescription = self.__description[id - 1]
        return currentDescription

    def recupereNomById(self, id):
        self.loadDescription()
        return self.__nom[id - 1]

    def affichePokedex(self):
        rectangle = Rect(330, 400, 100, 100)
        x, y = rectangle.topleft
        size = (400, 700)
        self.pokdx = pygame.transform.scale(self.pokdx, size)
        self.fond = pygame.transform.scale(self.fond, (self.WIDTH, self.HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.__currentPos += 1
                        if self.__currentPos > 20:
                            self.__currentPos = 1
                        print(self.__currentPos)

                    elif event.key == pygame.K_LEFT:
                        self.__currentPos -= 1
                        if self.__currentPos <= 0:
                            self.__currentPos = 20

            self.SCREEN.blit(self.fond, (0, 0))
            self.SCREEN.blit(self.pokdx, (self.WIDTH // 3.5, 0))
            self.SCREEN.blit(self.__descriptif, (330, 370))

            # Render and position the name
            name_rendered = self.police_larger.render(pokedex.recupereNomById(self.__currentPos), True, "black")
            self.SCREEN.blit(name_rendered, (350, 120))

            # Render and position the description with line breaks
            description_lines = pokedex.recupereDescriptionById(self.__currentPos).split('\n')
            y_position = 400
            for line in description_lines:
                description_rendered = self.police_small.render(line, True, "black")
                self.SCREEN.blit(description_rendered, (330, y_position))
                y_position += description_rendered.get_rect().height  # Move to the next line

            self.SCREEN.blit(self.__type, (330, 520))
            self.SCREEN.blit(self.__stats, (420, 570))
            self.SCREEN.blit(self.loadGif(self.__currentPos), (410, 190))

            pygame.display.update()


pokedex = Pokedex(1)
pokedex.affichePokedex()
