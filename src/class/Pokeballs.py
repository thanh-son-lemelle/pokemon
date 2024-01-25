import json
import pygame
from Pokemon import Pokemon
import sys
from pygame import *
from pygame.locals import *

class Pokeballs():
    def __init__(self, id):
        pygame.init()
        self.__id = id
        self.__nom = []
        self.__imageFace = None
        self.__currentPos = 1
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokeballs")
        self.pokeballs = pygame.image.load("images\\pokeballs\\pokeballs.png")
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (100, 100))
        largeur, hauteur = 1000, 700
        noir = (0, 0, 0)
        fenetre = pygame.display.set_mode((largeur, hauteur))
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, noir, (100, 50, 200, 200))

    def loadDescription(self):
            with open(r'data\\pokedex\\pokedex.json', 'r', encoding='utf-8') as file:
                pokemonsDescription = json.load(file)

            for pokemon in pokemonsDescription['pokemons']:
                self.__nom.append(pokemon['nom'])
               
            return pokemon['id'], self.__nom

    def loadGif(self, id):
        self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        self.__imageFace = pygame.transform.scale(self.__imageFace, (150, 150))
        return self.__imageFace

    def recupereNomById(self, id):
        self.loadDescription()
        return self.__nom[id - 1]
    
    def affichePokeballs(self):
        self.pokeballs = pygame.transform.scale(self.pokeballs, (self.WIDTH, self.HEIGHT))

        musique = pygame.mixer.music.load("musique\\main menu\\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.__currentPos += 1
                        if self.__currentPos > 20:
                            self.__currentPos = 1

                    elif event.key == pygame.K_LEFT:
                        self.__currentPos -= 1
                        if self.__currentPos <= 0:
                            self.__currentPos = 20

                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()  

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        if 875 <= event.pos[0] <= 975 and 575 <= event.pos[1] <= 675:
                            running = False

                        if 329 <= event.pos[0] <= 389 and 303 <= event.pos[1] <= 360:
                            print("Poke1")
                    
                        if 526 <= event.pos[0] <= 575 and 273 <= event.pos[1] <= 328:
                            print("Poke2")

                        if 670 <= event.pos[0] <= 717 and 253 <= event.pos[1] <= 299:
                            print("Poke3")

            self.SCREEN.blit(self.pokeballs, (0, 0))
            self.SCREEN.blit(self.button_menu, (875, 575))

            pygame.display.flip()
            pygame.display.update()
            
pokeballs= Pokeballs(1)
pokeballs.affichePokeballs()





        
 

