import json
import random 
import pygame

class Dresseurs: 
    def __init__(self, x, y):
        self.__nom = None
        self.__x = x
        self.__y = y 
        self.__listePokemons = []
        self.__imageFace = None
        self.__imageBack = None

    def get_nom(self):
        return self.__nom
    
    def position(self):
        position = (self.__x, self.__y) 
        return position 
    
    def loadData(self):
        with open("data\\Dresseurs.json", 'r') as fichier:
            donnees = json.load(fichier)
            return donnees['dresseurs']
    
    def set_nomAdversaire (self):
        adversaire = self.loadData()
        self.__nom = random.choice(adversaire)
    
    def set_nomJoueur(self):
        self.__nom = input ("veuillez entrer le nom du joueur: ")

    def image(self):
        self.__imageFace = pygame.image.load(f"images\\sprite_characters\\ennemies\\{self.__nom}.gif")
        self.__imageBack = pygame.image.load(f"images\\sprite_characters\\SelfCharacter\\{self.__nom}.gif")

        
joueur1 = Dresseurs(1, 2)
joueur1.set_nomJoueur()
print(joueur1.get_nom())
print("VS")
adversaire1 = Dresseurs(4, 8)
adversaire1.set_nomAdversaire()
print(adversaire1.get_nom())




