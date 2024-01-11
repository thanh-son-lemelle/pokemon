import json
import random 

class Dresseurs: 
    def __init__(self, x, y):
        self.__nom = None
        self.__x = x
        self.__y = y 
        self.__listePokemons = []

    
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
        self.__nom = input ("veuillez rentrez le nom du joueur: ")
        

        
joueur1 = Dresseurs(1, 2)
print(joueur1.get_nom())
joueur1.set_nomJoueur()

adversaire1 = Dresseurs(4, 8)
print(adversaire1.loadData())
adversaire1.set_nomAdversaire()
print(joueur1.get_nom())
print(adversaire1.get_nom())
