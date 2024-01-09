from Button import *
import pygame
import sys
from pygame import *
from pygame.locals import *


pygame.init()

WIDTH = 722

HEIGHT = 541

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255 , 255 , 255)

pygame.display.set_caption("Menu")

BG = pygame.image.load("images\\background\menu\Fond pokemon.jpg")


def get_font(size): 
    return pygame.font.Font("C:\Windows\Fonts\Arial.ttf", size)


def main_menu():
    musique= pygame.mixer.music.load("musique\main menu\Pokemon BlackWhite Music - Pokemon Center.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.image.load("images\\button\images\Play Rect.png"), pos=(200, 300), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("images\\button\images\Quit Rect.png"), pos=(200, 450), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")


        for button in [PLAY_BUTTON, QUIT_BUTTON]:

            button.changeColor(MENU_MOUSE_POS)

            button.update(SCREEN)

        
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


main_menu()