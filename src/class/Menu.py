from Button import *
import pygame
import sys
from pygame import *
from pygame.locals import *

class Menu():

    def __init__(self):
        self.WIDTH = 722
        self.HEIGHT = 541
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.white = (255 , 255 , 255)
        self.BG = pygame.image.load("images\\background\menu\Fond pokemon.jpg")

    def get_font(self,size): 
        return pygame.font.Font("font\Pokemon Classic.ttf", size)


    def main_menu(self):
        pygame.init()
        size = (722,541)
        'self.BG = pygame.transform.scale(self.BG, size)'
        pygame.display.set_caption("Menu")
        musique= pygame.mixer.music.load("musique\main menu\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

        while True:

            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()


            PLAY_BUTTON = Button(image=pygame.image.load("images\\button\\images\\button main.png"), pos=(100, 300), 
                                text_input="PLAY", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=pygame.image.load("images\\button\\images\\button main.png"), pos=(100, 450), 
                                text_input="QUIT", font=self.get_font(20), base_color="#d7fcd4", hovering_color="White")


            for button in [PLAY_BUTTON, QUIT_BUTTON]:

                button.changeColor(MENU_MOUSE_POS)

                button.update(self.SCREEN)

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    #if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):

                    
                        

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):

                        pygame.quit()

                        sys.exit()


            pygame.display.update()


