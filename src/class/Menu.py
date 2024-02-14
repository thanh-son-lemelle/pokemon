from Button import Button
from Pokedex import Pokedex
from Pokeballs import Pokeballs
import pygame
import sys
from pygame import *
from pygame.locals import *
from Ajout_Pokemon import AjoutPokemon

class Menu():

    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.white = (255 , 255 , 255)
        self.BG = pygame.image.load("images\\background\\menu\\Fond pokemon.jpg")
        self.__playgame = False
        self.__pokemonChoisi = None

    def get_pokemonChoisi(self):
        return self.__pokemonChoisi

    def set_playgame(self):
        self.__playgame = False
        
    def get_playgame (self):
        return self.__playgame
    
    def get_font(self,size): 
        return pygame.font.Font("font\\Pokemon Classic.ttf", size)


    def main_menu(self):
        pygame.init()
        size = (1000,700)
        self.BG = pygame.transform.scale(self.BG, size)
        pygame.display.set_caption("Menu")
        musique= pygame.mixer.music.load("musique\\main menu\\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
        running = True
        while running:

            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()


            PLAY_BUTTON = Button(image=pygame.image.load("images\\button\\images\\button main.png"), pos=(100, 350), 
                                text_input="PLAY", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")
            
            POKEDEX_BUTTON = Button(image=pygame.image.load("images\\button\images\\button main.png"), pos=(100, 450), 
                                text_input="POKEDEX", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")
            
            AJOUT_BUTTON = Button(image=pygame.image.load("images\\button\images\\button main.png"), pos=(100, 550), 
                                text_input="AJOUT", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=pygame.image.load("images\\button\images\\button main.png"), pos=(100, 650), 
                                text_input="QUIT", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")


            for button in [PLAY_BUTTON,POKEDEX_BUTTON,AJOUT_BUTTON,QUIT_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        choixPokemon = Pokeballs()
                        choixPokemon.affichePokeballs()
                        self.__pokemonChoisi = choixPokemon.get_PokemonChoisi()
                        previousPage = choixPokemon.get_previousPage()
                        if previousPage == True:
                            self.__playgame = False
                        else:
                            self.__playgame = True
                        break
                        
                    



                    if POKEDEX_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pokedex = Pokedex(1)
                        pokedex.affichePokedex()




                    if AJOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        new_poke = AjoutPokemon()
                        new_poke.displayAjoutPokemon()
                        previousPage1 = new_poke.get_previousPage()
                        if previousPage1 == True:
                            self.__playgame = False
                        else:
                            self.__playgame = True
                        break
                        

                    
                        

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):

                        pygame.quit()

                        sys.exit()
            if self.__playgame:
                break


            pygame.display.update()


