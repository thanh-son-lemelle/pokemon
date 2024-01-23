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
        self.__descriptif = None
        self.__typeg = []
        self.__stats = []
        self.__description = []
        self.__type1 = []
        self.__type2 = []
        self.__infostats = []
        self.__hp = []
        self.__attack = []
        self.__defense = []
        self.__speed = []
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
        self.__typeg = self.police_medium.render("Type :", True, "black")
        self.__stats = self.police_small.render("Statistiques : ", True, "black")
        self.__affHp = self.police_small.render("Hp : ", True, "black")
        self.__affAttack = self.police_small.render("Attack : ", True, "black")
        self.__affDefense = self.police_small.render("Defense : ", True, "black")
        self.__affSpeed = self.police_small.render("Speed : ", True, "black")

    def loadDescription(self):
        with open(r'data\\pokedex\\pokedex.json', 'r', encoding='utf-8') as file:
            pokemonsDescription = json.load(file)

        for pokemon in pokemonsDescription['pokemons']:
            self.__nom.append(pokemon['nom'])
            self.__description.append(pokemon['description'])


        return pokemon['id'], self.__nom, self.__description

    def loadStats(self):
        with open(r'data\\pokemons\\pokemons.json', 'r', encoding='utf-8') as file:
            pokemonsData = json.load(file)

        for pokemon in pokemonsData['pokemons']:
            self.__type1.append(pokemon['type1'])
            self.__type2.append(pokemon['type2'])
            self.__hp.append(pokemon['stats']['hp'])
            self.__attack.append(pokemon['stats']['attack'])
            self.__defense.append(pokemon['stats']['defense'])
            self.__speed.append(pokemon['stats']['speed'])
        
        return pokemon['id'], self.__type1, self.__type2, self.__infostats, self.__hp, self.__attack, self.__defense, self.__speed

    def loadGif(self, id):
        self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        self.__imageFace = Pokemon.resizeImage(self, self.__imageFace, 150)  

        return self.__imageFace

    def recupereNomById(self, id):
        self.loadDescription()

        return self.__nom[id - 1]
    
    def recupereDescriptionById(self, id):
        self.loadDescription()
        currentDescription = self.__description[id - 1]

        return currentDescription

    def recupereType1ById(self, id):
        self.loadStats()

        return self.__type1[id - 1]
    
    def recupereType2ById(self, id):
        self.loadStats()

        return self.__type2[id - 1]
    
    def recupereHpById(self, id):
        self.loadStats()

        return self.__hp[id - 1] 
    
    def recupereAttackById(self, id):
        self.loadStats()

        return self.__attack[id - 1]
    
    def recupereDefenseById(self, id):
        self.loadStats()

        return self.__defense[id - 1]

    def recupereSpeedById(self, id):
        self.loadStats()

        return self.__speed[id - 1]

    def affichePokedex(self):
        rectangle = Rect(330, 400, 100, 100)
        x, y = rectangle.topleft
        size = (400, 700)
        self.pokdx = pygame.transform.scale(self.pokdx, size)
        self.fond = pygame.transform.scale(self.fond, (self.WIDTH, self.HEIGHT))

        musique= pygame.mixer.music.load("musique\main menu\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        
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
            self.SCREEN.blit(self.__typeg, (330, 520))
            self.SCREEN.blit(self.__stats, (420, 570))
            self.SCREEN.blit(self.__affHp, (420, 592))
            self.SCREEN.blit(self.__affAttack, (420, 608))
            self.SCREEN.blit(self.__affDefense, (420, 624))
            self.SCREEN.blit(self.__affSpeed, (420, 640))

            name_rendered = self.police_larger.render(self.recupereNomById(self.__currentPos), True, "black")
            self.SCREEN.blit(name_rendered, (350, 120))

            self.SCREEN.blit(self.loadGif(self.__currentPos), (410, 190))

            description_lines = self.recupereDescriptionById(self.__currentPos).split('\n')
            y_position = 400
            for line in description_lines:
                description_rendered = self.police_small.render(line, True, "black")
                self.SCREEN.blit(description_rendered, (330, y_position))
                y_position += description_rendered.get_rect().height  

            type1_rendered = self.police_small.render(self.recupereType1ById(self.__currentPos), True, "black")
            self.SCREEN.blit(type1_rendered, (460, 527))

            type2_rendered = self.police_small.render(self.recupereType2ById(self.__currentPos), True, "black")
            self.SCREEN.blit(type2_rendered, (550, 527))

            hp_rendered = self.police_small.render(str(self.recupereHpById(self.__currentPos)), True, "black")
            self.SCREEN.blit(hp_rendered, (530,592))

            attack_rendered = self.police_small.render(str(self.recupereAttackById(self.__currentPos)), True, "black")
            self.SCREEN.blit(attack_rendered, (530,608))

            defense_rendered = self.police_small.render(str(self.recupereDefenseById(self.__currentPos)), True, "black")
            self.SCREEN.blit(defense_rendered, (530,624))

            speed_rendered = self.police_small.render(str(self.recupereSpeedById(self.__currentPos)), True, "black")
            self.SCREEN.blit(speed_rendered, (530,640))

            pygame.display.update()
