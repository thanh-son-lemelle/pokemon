#!/usr/bin/env python3
import json

class Pokemon:
    def __init__(self, id ) -> None:
        self.__id = id
        self.__pokemonData = self.loadData()
        self.__name = None
        self.__type = None
        self.__stats = None
        self.__evolution = None
        self.__level = 10
        self.__xp = 0
        self.loadData()
        self.__abilities = []


    def get_id(self):
        return self.__id

    def get_nom(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_stats(self):
        return self.__stats

    def get_evolution(self):
        return self.__evolution
    
    def get_xp(self):
        return self.__xp
    
    # Charge les données du fichier pokemon.json
    def loadData(self):
        with open('data\pokemons\pokemons.json', 'r') as fichier:
            donnees = json.load(fichier)

        # Rechercher les données du Pokémon avec l'ID correspondant
        pokemon_data = next((pokemon for pokemon in donnees["pokemons"] if pokemon["id"] == self.__id), None)
        
        if pokemon_data:
            self.__name = pokemon_data.get("name")
            self.__type = pokemon_data.get("type")
            self.__stats = pokemon_data.get("stats")
            self.__evolution = pokemon_data.get("evolution")
        return pokemon_data

    # Test de l'affichage des stats
    def afficher_infos(self):
            print(f"#{self.__id} {self.__name} - Type: {self.__type}")
            print("Stats:")
            for stat, value in self.__stats.items():
                print(f"  {stat.capitalize()}: {value}")
            print(f"  Level: {self.__level}")
            
            if self.__evolution:
                print(f"Évolution: Niveau {self.__evolution['level']} vers {self.__evolution['to']}")
            print("\n")

    def set_xp(self,AddXp): # xpGagnée à définir dans la class Combat
        self.__xp += AddXp

    def get_abilities(self):
        self.__abilities = self.__pokemonData.get("abilities")


    def get_AbilitiesByLevel(self):
        abilities = []
        self.get_abilities()
        for ability in self.__abilities:
            abilityLevel = ability ["level"]
            if abilityLevel <= self.__level:
                abilities.append(ability["name"])
        self.__abilities = abilities
        return self.__abilities



    # Prend les valeurs de l'évolution id name stat etc...
    def evolue (self):
        self.__id = self.__evolution.get("to")
        self.loadData()

    

# Test de la class
starter = Pokemon (1)
starter.afficher_infos()
starter.evolue()
starter.afficher_infos()
print(starter.get_AbilitiesByLevel())
