import json
import os
import random
from Pokemon import Pokemon

class Dresseurs(): 
    def __init__(self, nom=None):
        self.__nom = nom
        self.__listePokemons = []
        self.itemsInventaire = ()

    def get_nom(self):
        return self.__nom
    
    def get_lisPokemons(self):
        return self.__listePokemons

    def loadData(self):
        # Get the directory of the current script
        dresseurPath = os.path.join('data', 'dresseurs', 'Dresseurs.json')
        with open(dresseurPath, 'r') as file:
            data = json.load(file)
        return data

    def setRandomName(self):
        data = self.loadData()
        self.__nom = random.choice(data['dresseurs'])
        return self.__nom
    
    def randomId(self):
        return random.randint(1, 20)
    
    def getRoster(self, level, nombrePokemons ):
        while len(self.__listePokemons) < nombrePokemons:
            pokemon = Pokemon(random.randint(1, 20))
            pokemon.set_level(level)
            self.__listePokemons.append(pokemon)        
        return self.__listePokemons
    
    def addToRoster(self, pokemon):
        self.__listePokemons.append(pokemon)