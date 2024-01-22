import json
import Dresseurs
from Dresseurs import *

class Adversaires(Dresseurs): 
    def __init__(self, nom, x, y, listePokemons):
        Dresseurs.__init__(self, nom, x, y)
        self.__nom = nom
        self.x = x
        self.y = y 
        self.__listePokemons = listePokemons 
        self.itemsInventaire = ()

with open('data\Dresseurs.json', 'r') as file:
    data = json.load(file)

for adversaire in data["dresseurs"]:
    print(f"\n Adversaire : {adversaire['nom']}")
    print("Pokémon :")
    for pokemon in adversaire['pokemon']:
        print(f" - {pokemon}") 