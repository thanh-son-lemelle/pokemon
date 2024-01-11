import json
import random 

class Dresseurs: 
    def __init__(self, x, y):
        self.__nom = None
        self.__x = x
        self.__y = y 
        self.__listePokemons = []
        self.loadData()
    
    def get_nom(self):
        return self.__nom
    
    def position(self):
        position = (self.__x, self.__y) 
        return position 
    
    def loadData(self):
        with open(r"data\Dresseurs.json", "r") as fichier_json:
            listeNom = json.load(fichier_json)
    
        dresseursnom = [dresseurs["nom"] for dresseurs in listeNom["dresseurs"]]
        self.__nom = random.choice(dresseursnom)
        

dresseur1 = Dresseurs(1, 2)
print(dresseur1.get_nom())