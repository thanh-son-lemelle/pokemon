import json
import pygame
from Pokemon import Pokemon 
from Animation import Animation
import sys
from pygame import *
from pygame.locals import *
import random

class Pokeballs():
    def __init__(self, id):
        pygame.init()
        self.__id = id
        self.__nom = []
        self.__currentPos = 1
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokeballs")
        self.pokeballs = pygame.image.load("images\\pokeballs\\pokeballs.png")
        self.pokeballs = pygame.transform.scale(self.pokeballs, (1000, 500))
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (60,60))
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.__choix = self.police_medium.render("Veuillez choisir une pokeball :", True, "black")
        largeur, hauteur = 1000, 700
        noir = (0, 0, 0)
        fenetre = pygame.display.set_mode((largeur, hauteur))
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, noir, (100, 50, 200, 200))
        
        self.pok1 = Pokemon(random.randint(1, 20))
        self.pok2 = Pokemon(random.randint(1, 20))
        self.pok3 = Pokemon(random.randint(1, 20))

        self.animation_pok1 = Animation(self.pok1)
        self.animation_pok2 = Animation(self.pok2)
        self.animation_pok3 = Animation(self.pok3)

    def get_id(self):
        return self.__id
    
    def loadDescription(self):
            with open(r'data\\pokedex\\pokedex.json', 'r', encoding='utf-8') as file:
                pokemonsDescription = json.load(file)

            for pokemon in pokemonsDescription['pokemons']:
                self.__nom.append(pokemon['nom'])
               
            return pokemon['id'], self.__nom

    def loadGif(self, id):
        image = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        image = pygame.transform.scale(image, (150, 150))
        return image

    def recupereNomById(self, id):
        self.loadDescription()
        return self.__nom[id - 1]

    def affichePokeballs(self):
        size_zone_text = (1000, 200)
        zone_text = pygame.image.load("images\\background\\menu\\TextZone.png")
        zone_text = pygame.transform.scale(zone_text, size_zone_text)

        musique = pygame.mixer.music.load("musique\\main menu\\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        self.SCREEN.blit(self.pokeballs, (0, 0))
        self.SCREEN.blit(zone_text, (0, 500))
        self.SCREEN.blit(self.__choix, (80, 550))
        self.SCREEN.blit(self.button_menu, (926, 623))

        self.animation_pok1.loadFramesForPokeball()
        self.animation_pok2.loadFramesForPokeball()
        self.animation_pok3.loadFramesForPokeball()

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

                        if 331 <= event.pos[0] <= 388 and 215 <= event.pos[1] <= 260:
                            self.SCREEN.blit(self.pokeballs, (0, 0))
                            self.SCREEN.blit(zone_text, (0, 500))
                            self.SCREEN.blit(self.__choix, (80, 550))
                            self.SCREEN.blit(self.button_menu, (926, 623))
                            self.animation_pok1.displayPokemonForPokeball (300, 100)
                            pygame.display.update()
                       
                        if 526 <= event.pos[0] <= 573 and 197 <= event.pos[1] <= 236:
                            self.SCREEN.blit(self.pokeballs, (0, 0))
                            self.SCREEN.blit(zone_text, (0, 500))
                            self.SCREEN.blit(self.__choix, (80, 550))
                            self.SCREEN.blit(self.button_menu, (926, 623))
                            self.animation_pok2.displayPokemonForPokeball (400, 100)
                            pygame.display.update()
                         
                        if 673 <= event.pos[0] <= 714 and 179 <= event.pos[1] <= 217:
                            self.SCREEN.blit(self.pokeballs, (0, 0))
                            self.SCREEN.blit(zone_text, (0, 500))
                            self.SCREEN.blit(self.__choix, (80, 550))
                            self.SCREEN.blit(self.button_menu, (926, 623))
                            self.animation_pok3.displayPokemonForPokeball (500, 100)
                            pygame.display.update()

            pygame.display.flip()
            pygame.display.update()
            
pokeballs = Pokeballs(1)
pokeballs.affichePokeballs()




        
 

