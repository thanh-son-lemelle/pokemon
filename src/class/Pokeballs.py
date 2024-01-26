# Importation des bibliothèques nécessaires
import json
import pygame
from Pokemon import Pokemon 
from Animation import Animation
import sys
from pygame import *
from pygame.locals import *
import random

# Initialisation de la classe Pokeballs : 
# en définissant divers attributs tels que la fenêtre Pygame, 
# les polices, les images, et les Pokemon.
class Pokeballs():
    def __init__(self, id):
        pygame.init()
        pygame.display.set_caption("Pokeballs")
        self.__id = id
        self.__nom = []
        self.__currentPos = 1
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.pokeballs = pygame.image.load("images\\pokeballs\\pokeballs.png")
        self.pokeballs = pygame.transform.scale(self.pokeballs, (1000, 500))
        self.police_larger = pygame.font.Font("font\\Pokemon Classic.ttf", 30)
        self.police_medium = pygame.font.Font("font\\Pokemon Classic.ttf", 20)
        self.police_small = pygame.font.Font("font\\Pokemon Classic.ttf", 12)
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (60,60))

# Création des boutons "Oui" et "Non"
        self.button_yes = pygame.image.load("images\\pokeballs\\yes.png")
        self.button_no = pygame.image.load("images\\pokeballs\\no.png")
        self.button_yes = pygame.transform.scale(self.button_yes, (100, 50))
        self.button_no = pygame.transform.scale(self.button_no, (100, 50))

# Création du texte de sélection
        self.__choix = self.police_medium.render("Veuillez choisir une pokeball : ", True, "black")
        
        largeur, hauteur = 1000, 700
        noir = (0, 0, 0)
        fenetre = pygame.display.set_mode((largeur, hauteur))
        fenetre.fill(noir)

# Création d'un Pokemon aléatoire
        self.pok1 = Pokemon(random.randint(1, 20))
        self.pok2 = Pokemon(random.randint(1, 20))
        self.pok3 = Pokemon(random.randint(1, 20))

# Texte de choix pour le Pokemon
        self.__choix1 = self.police_medium.render(f"Vous choisissez le pokemon : {self.pok1.get_nom()}", True, "black")
        self.__choix2 = self.police_medium.render(f"Vous choisissez le pokemon : {self.pok2.get_nom()}", True, "black")
        self.__choix3 = self.police_medium.render(f"Vous choisissez le pokemon : {self.pok3.get_nom()}", True, "black")

# Création d'une animation pour le Pokemon
        self.animation_pok1 = Animation(self.pok1)
        self.animation_pok2 = Animation(self.pok2)
        self.animation_pok3 = Animation(self.pok3)

# Méthode loadDescription : Cette méthode charge les descriptions des Pokemon à partir d'un fichier JSON dans la liste __nom.
    def loadDescription(self):
            with open(r'data\\pokedex\\pokedex.json', 'r', encoding='utf-8') as file:
                pokemonsDescription = json.load(file)

            for pokemon in pokemonsDescription['pokemons']:
                self.__nom.append(pokemon['nom'])
               
            return pokemon['id'], self.__nom
    
# Méthode loadGif : Cette méthode charge l'image animée (GIF) d'un Pokemon en fonction de son identifiant.
    def loadGif(self, id):
        image = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        image = pygame.transform.scale(image, (150, 150))
        return image

# Méthode affichePokeballs : Cette méthode affiche l'écran de sélection des Pokemon. 
# gère les événements, 
# affiche les éléments graphiques, 
# et gére les animations des Pokemon en fonction des choix du joueur.
    def affichePokeballs(self):

# Charge la musique de fond
        musique = pygame.mixer.music.load("musique\\main menu\\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

# Définit la taille de la zone de texte
        size_zone_text = (1000, 200)

# Charge l'image de fond pour la zone de texte
        zone_text = pygame.image.load("images\\background\\menu\\TextZone.png")
        zone_text = pygame.transform.scale(zone_text, size_zone_text)



# Charge les images pour l'animation de chaque Pokemon
        self.animation_pok1.loadFramesForPokeball()
        self.animation_pok2.loadFramesForPokeball()
        self.animation_pok3.loadFramesForPokeball()

# Variables de contrôle pour savoir quel Pokemon est sélectionné
        running = True
        click_pok1 = False
        click_pok2 = False
        click_pok3 = False

# Boucle principale d'événements Pygame
        while running:
            for event in pygame.event.get(): 

# Si l'utilisateur ferme la fenêtre, quitte le programme
                if event.type == pygame.QUIT:
                    pygame.quit()

# Si la touche ESC est enfoncée, quitte le programme
                    if event.key == pygame.K_ESCAPE:
                            pygame.quit()  

# Si un bouton de la souris est cliqué
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 

# Si le clic est dans la zone du bouton "Retour au menu"
                        if 875 <= event.pos[0] <= 975 and 575 <= event.pos[1] <= 675:

# Met fin à la boucle et retourne au menu principal
                            running = False

# Si le clic est dans la zone du Pokémon 1
                        if 331 <= event.pos[0] <= 388 and 215 <= event.pos[1] <= 260:
                            click_pok1 = True
                            click_pok2 = False
                            click_pok3 = False

# Si le clic est dans la zone du Pokémon 2
                        if 526 <= event.pos[0] <= 573 and 197 <= event.pos[1] <= 236:
                            click_pok1 = False
                            click_pok2 = True
                            click_pok3 = False

# Si le clic est dans la zone du Pokémon 3
                        if 673 <= event.pos[0] <= 714 and 179 <= event.pos[1] <= 217:
                            click_pok1 = False
                            click_pok2 = False
                            click_pok3 = True
                        
# Si le clic est dans la zone oui ou non 
                        if click_pok1 or click_pok2 or click_pok3:
                            if 100 <= event.pos[0] <= 200 and 600 <= event.pos[1] <= 650:
                                click_pok1 = False
                                click_pok2 = False
                                click_pok3 = False
                                running = False
                                print("yes")

                            if 300 <= event.pos[0] <= 400 and 600 <= event.pos[1] <= 650:
                                click_pok1 = False
                                click_pok2 = False
                                click_pok3 = False
                                print("no")
          
# Affichage du Pokémon sélectionné
            if click_pok1:
                self.SCREEN.blit(self.pokeballs, (0, 0))
                self.SCREEN.blit(zone_text, (0, 500))
                self.SCREEN.blit(self.__choix1, (80, 550))
                self.SCREEN.blit(self.button_menu, (926, 623))
                self.animation_pok1.displayPokemonForPokeball (350, 100)
                self.SCREEN.blit(self.button_yes, (100,600))
                self.SCREEN.blit(self.button_no, (300,600))

            elif click_pok2:
                self.SCREEN.blit(self.pokeballs, (0, 0))
                self.SCREEN.blit(zone_text, (0, 500))
                self.SCREEN.blit(self.__choix2, (80, 550))
                self.SCREEN.blit(self.button_menu, (926, 623))
                self.animation_pok2.displayPokemonForPokeball (540, 100)
                self.SCREEN.blit(self.button_yes, (100,600))
                self.SCREEN.blit(self.button_no, (300,600))

            elif click_pok3:
                self.SCREEN.blit(self.pokeballs, (0, 0))
                self.SCREEN.blit(zone_text, (0, 500))
                self.SCREEN.blit(self.__choix3, (80, 550))
                self.SCREEN.blit(self.button_menu, (926, 623))
                self.animation_pok3.displayPokemonForPokeball (690, 100)
                self.SCREEN.blit(self.button_yes, (100,600))
                self.SCREEN.blit(self.button_no, (300,600))
                
# Affiche les éléments de base sur la fenêtre
            else:
                self.SCREEN.blit(self.pokeballs, (0, 0))
                self.SCREEN.blit(zone_text, (0, 500))
                self.SCREEN.blit(self.__choix, (80, 550))
                self.SCREEN.blit(self.button_menu, (926, 623))

# Mise à jour de l'affichage
            pygame.display.flip()
            pygame.display.update()
            
pokeballs = Pokeballs(1)
pokeballs.affichePokeballs()




        
 

