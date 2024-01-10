import json
import Personnages

class Dresseurs(Personnages): 
    def __init__(self, nom, x, y, listePokemons):
        Personnages.__init__(self)
        self.__nom = nom
        self.x = x
        self.y = y 
        self.__listePokemons = listePokemons 
        self.itemsInventaire = ()

with open('Dresseurs.json', 'r') as file:
    data = json.load(file)

for dresseur in data["dresseurs"]:
    print(f"\nDresseur : {dresseur['nom']}")
    print("Pokémon :")
    for pokemon in dresseur['pokemon']:
        print(f" - {pokemon}")

    