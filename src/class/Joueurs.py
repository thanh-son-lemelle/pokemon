import json
import Dresseurs
from Dresseurs import *

class Joueurs(Dresseurs): 
    def __init__(self, nom, x, y, listePokemons):
        Dresseurs.__init__(self, nom, x, y)
        self.__nom = nom
        self.x = x
        self.y = y 
        self.__listePokemons = listePokemons 
        self.itemsInventaire = ()

with open('data\Dresseurs.json', 'r') as file:
    data = json.load(file)

for joueur in data["dresseurs"]:
    print(f"\nJoueur : {joueur['nom']}")
    print("Pokémon :")
    for pokemon in joueur['pokemon']:
        print(f" - {pokemon}") 