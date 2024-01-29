# Importation des bibliothèques nécessaires
import json
import pygame
from Pokemon import Pokemon
import sys
from pygame import *
from pygame.locals import *

# Définition de la classe Pokedex
class Pokedex():
    def __init__(self, id):
        pygame.init()

# Initialisation des attributs de la classe
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
        self.__vu = []
        self.__imageFace = None
        self.__evolution = None
        self.__currentPos = 1
        self.WIDTH = 1000
        self.HEIGHT = 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pokedex")

# Chargement des images et polices nécessaires
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
        self.__affvu = self.police_small.render("Pokemon apperçu : ", True, "black")
        self.button_menu = pygame.image.load("images\\pokedex\\bouton exit.png")
        self.button_menu = pygame.transform.scale(self.button_menu, (100, 100))
        
# Méthode pour récupérer l'attribut vu
    def get_vu(self):
        return self.__vu
    
# Méthode pour charger les descriptions depuis un fichier JSON
    def loadDescription(self):
        with open(r'data\\pokedex\\pokedex.json', 'r', encoding='utf-8') as file:
            pokemonsDescription = json.load(file)

# Parcours des données pour récupérer les noms et descriptions des Pokemons
        for pokemon in pokemonsDescription['pokemons']:
            self.__nom.append(pokemon['nom'])
            self.__description.append(pokemon['description'])
        return pokemon['id'], self.__nom, self.__description

# Méthode pour charger les statistiques depuis un fichier JSON
    def loadStats(self):
        with open(r'data\\pokemons\\pokemons.json', 'r', encoding='utf-8') as file:
            pokemonsData = json.load(file)

# Parcours des données pour récupérer les types, statistiques et autres informations des Pokemons
        for pokemon in pokemonsData['pokemons']:
            self.__type1.append(pokemon['type1'])
            self.__type2.append(pokemon['type2'])
            self.__hp.append(pokemon['stats']['hp'])
            self.__attack.append(pokemon['stats']['attack'])
            self.__defense.append(pokemon['stats']['defense'])
            self.__speed.append(pokemon['stats']['speed'])
            self.__vu.append(pokemon['vu'])
        return (pokemon['id'], self.__type1, self.__type2, self.__infostats, self.__hp, self.__attack, self.__defense, self.__speed, self.__vu)

# Méthode pour charger une image gif du Pokemon
    def loadGif(self, id):
        self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{id}.gif")
        self.__imageFace = pygame.transform.scale(self.__imageFace, (150, 150))
        return self.__imageFace

# Méthode pour charger une image représentant un point d'interrogation
    def loadPoint(self, id):
        self.__imagePoint = pygame.image.load("images\\pokedex\\point d'interrogation.jpg")
        self.__imagePoint = pygame.transform.scale(self.__imagePoint, (130, 120))
        return self.__imagePoint

# Méthode pour récupérer le nom d'un Pokemon par son ID
    def recupereNomById(self, id):
        self.loadDescription()
        return self.__nom[id - 1]

# Méthode pour récupérer la description d'un Pokemon par son ID
    def recupereDescriptionById(self, id):
        self.loadDescription()
        currentDescription = self.__description[id - 1]
        return currentDescription

# Méthode pour récupérer le type 1 d'un Pokemon par son ID
    def recupereType1ById(self, id):
        self.loadStats()
        return self.__type1[id - 1]

# Méthode pour récupérer le type 2 d'un Pokemon par son ID
    def recupereType2ById(self, id):
        self.loadStats()
        return self.__type2[id - 1]

# Méthode pour récupérer les points de vie d'un Pokemon par son ID
    def recupereHpById(self, id):
        self.loadStats()
        return self.__hp[id - 1]

# Méthode pour récupérer l'attaque d'un Pokemon par son ID
    def recupereAttackById(self, id):
        self.loadStats()
        return self.__attack[id - 1]

# Méthode pour récupérer la défense d'un Pokemon par son ID
    def recupereDefenseById(self, id):
        self.loadStats()
        return self.__defense[id - 1]

 # Méthode pour récupérer la vitesse d'un Pokemon par son ID
    def recupereSpeedById(self, id):
        self.loadStats()
        return self.__speed[id - 1]

# Méthode pour récupérer l'attribut vu d'un Pokemon par son ID
    def recupereVu(self, id):
        self.loadStats()
        return self.__vu[id - 1]

# Méthode pour afficher l'écran du Pokedex
    def affichePokedex(self):

# Définition du rectangle d'affichage du Pokedex
        rectangle = Rect(330, 400, 100, 100)
        x, y = rectangle.topleft
        size = (400, 700)

# Redimensionnement des images du Pokedex et du fond
        self.pokdx = pygame.transform.scale(self.pokdx, size)
        self.fond = pygame.transform.scale(self.fond, (self.WIDTH, self.HEIGHT))

# Chargement de la musique de fond
        musique = pygame.mixer.music.load("musique\\main menu\\Pokemon BlackWhite Music - Pokemon Center.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

# Chargement des statistiques des Pokemons
        self.loadStats()

# Boucle principale d'événements Pygame
        running = True
        while running:
            for event in pygame.event.get():
# Si l'utilisateur ferme la fenêtre, quitte le programme
                if event.type == pygame.QUIT:
                    pygame.quit()
# Si une touche du clavier est enfoncée
                if event.type == pygame.KEYDOWN:
# Déplacement à droite dans le Pokedex
                    if event.key == pygame.K_RIGHT:
                        self.__currentPos += 1
                        if self.__currentPos > 30:
                            self.__currentPos = 1
# Déplacement à gauche dans le Pokedex
                    elif event.key == pygame.K_LEFT:
                        self.__currentPos -= 1
                        if self.__currentPos <= 0:
                            self.__currentPos = 30
# Touche ESC pour quitter le programme
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()  
# Si un bouton de la souris est cliqué
                elif event.type == pygame.MOUSEBUTTONDOWN:
# Si le bouton gauche est cliqué
                    if event.button == 1: 
# Si le clic est dans la zone du bouton "Retour au menu"
                        if 875 <= event.pos[0] <= 975 and 575 <= event.pos[1] <= 675:
# Met fin à la boucle et retourne au menu principal
                            running = False
                            
# Affichage des éléments graphiques
            self.SCREEN.blit(self.fond, (0, 0))
            self.SCREEN.blit(self.pokdx, (self.WIDTH // 3.5, 0))
            self.SCREEN.blit(self.__descriptif, (330, 370))
            self.SCREEN.blit(self.__typeg, (330, 520))
            self.SCREEN.blit(self.__stats, (420, 570))
            self.SCREEN.blit(self.__affHp, (420, 592))
            self.SCREEN.blit(self.__affAttack, (420, 608))
            self.SCREEN.blit(self.__affDefense, (420, 624))
            self.SCREEN.blit(self.__affSpeed, (420, 640))
            self.SCREEN.blit(self.__affvu, (350, 180))
            self.SCREEN.blit(self.button_menu, (875, 575))

# Affiche les détails du Pokemon actuellement sélectionné
            if self.recupereVu(self.__currentPos) >= 1:

# Affiche le nom du Pokemon
                name_rendered = self.police_larger.render(self.recupereNomById(self.__currentPos), True, "black")
                self.SCREEN.blit(name_rendered, (350, 120))

# Affiche l'image du Pokemon
                self.__imageFace = self.loadGif(self.__currentPos)
                rect = self.__imageFace.get_rect()
                rect.midbottom = (490, self.WIDTH // 3 + 30)
                self.SCREEN.blit(self.__imageFace, rect)

# Affiche la description du Pokemon
                description_lines = self.recupereDescriptionById(self.__currentPos).split('\n')
                y_position = 400
                for line in description_lines:
                    description_rendered = self.police_small.render(line, True, "black")
                    self.SCREEN.blit(description_rendered, (330, y_position))
                    y_position += description_rendered.get_rect().height

# Affiche les types et statistiques du Pokemon
                type1_rendered = self.police_small.render(self.recupereType1ById(self.__currentPos), True, "black")
                self.SCREEN.blit(type1_rendered, (460, 527))

                type2_rendered = self.police_small.render(self.recupereType2ById(self.__currentPos), True, "black")
                self.SCREEN.blit(type2_rendered, (550, 527))

                hp_rendered = self.police_small.render(str(self.recupereHpById(self.__currentPos)), True, "black")
                self.SCREEN.blit(hp_rendered, (530, 592))

                attack_rendered = self.police_small.render(str(self.recupereAttackById(self.__currentPos)), True, "black")
                self.SCREEN.blit(attack_rendered, (530, 608))

                defense_rendered = self.police_small.render(str(self.recupereDefenseById(self.__currentPos)), True, "black")
                self.SCREEN.blit(defense_rendered, (530, 624))

                speed_rendered = self.police_small.render(str(self.recupereSpeedById(self.__currentPos)), True, "black")
                self.SCREEN.blit(speed_rendered, (530, 640))

                vu_rendered = self.police_medium.render(str(self.recupereVu(self.__currentPos)), True, "black")
                self.SCREEN.blit(vu_rendered, (550, 171))

            else:
# Si le Pokemon n'a pas encore été vu, affiche un point d'interrogation
                self.SCREEN.blit(self.loadPoint(self.__currentPos), (420, 230))

# Mise à jour de l'affichage
            pygame.display.update()











