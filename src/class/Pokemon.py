#!/usr/bin/env python3
import json
import pygame
import sys

class Pokemon:
    def __init__(self, id ) -> None:
        self.__id = id
        self.__pokemonData = self.loadData()
        self.__name = None
        self.__type = None
        self.__baseStats = None
        self.__stats = None
        self.__evolution = None
        self.__level = 1
        self.__xp = 0
        self.__abilities = []
        self.__imageFace = None
        self.__imageBack = None
        self.loadData()


    def get_id(self):
        return self.__id

    def get_nom(self):
        return self.__name

    def get_type(self):
        return self.__type
    
    def get_baseStats(self):
        return self.__baseStats

    def get_stats(self):
        return self.__stats

    def get_evolution(self):
        return self.__evolution
    
    def get_xp(self):
        return self.__xp
    
    def get_imageFace(self):
        return self.__imageFace
    
    def get_imageBack(self):
        return self.__imageBack
    
    # Charge les données du fichier pokemon.json
    def loadData(self):
        with open(r"data\pokemons\pokemons.json", "r") as fichier:
            donnees = json.load(fichier)

        # Rechercher les données du Pokémon avec l'ID correspondant
        pokemon_data = next((pokemon for pokemon in donnees["pokemons"] if pokemon["id"] == self.__id), None)
        
        if pokemon_data:
            self.__name = pokemon_data.get("name")
            self.__type = pokemon_data.get("type")
            self.__baseStats = pokemon_data.get("stats")
            self.__evolution = pokemon_data.get("evolution")           
            self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{self.__id}.gif")
            self.__imageBack = pygame.image.load(f"images\\sprite_pokemon\\back\\{self.__id}.gif")
        return pokemon_data

    # Test de l'affichage des stats
    def afficherBaseInfos(self):
            print(f"#{self.__id} {self.__name} - Type: {self.__type}")
            print("Stats:")
            for stat, value in self.__stats.items():
                print(f"  {stat.capitalize()}: {value}")
            print(f"  Level: {self.__level}")
            print(f"  XP: {self.__xp}")
            if self.__evolution:
                print(f"Évolution: Niveau {self.__evolution['level']} vers {self.__evolution['to']}")
            print("\n")

    def set_xp(self, AddXp): # xpGagnée à définir dans la class Combat
        self.__xp += AddXp

        print(f"{self.__name} a gagné {AddXp} xp !") 
        if self.__xp >= 100:
            while self.__xp >= 100:
                self.level_up()
                print(f"{self.__name} est maintenant niveau {self.__level} !")
                self.__xp -= 100
                if self.__evolution is not None:
                    if self.__level >= self.__evolution["level"]:
                        self.evolue()

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

    def level_up(self):
        self.__level += 1
        self.get_AbilitiesByLevel()

        growth = self.__pokemonData.get("growth", {})
        for stat, value in growth.items():
            self.__stats[stat] = self.__baseStats[stat] + value * self.__level
        print(self.afficherBaseInfos())

    # Prend les valeurs de l'évolution id name stat etc...
    def evolue (self):
        evolutionName = self.get_name_by_id(self.__id + 1)
        print(f"{self.__name} a évolué en {evolutionName} !")
        self.__id = self.__evolution.get("to")
        self.loadData()
        print(self.afficherBaseInfos())

    def get_name_by_id(self, idDonne):
        with open(r"data\pokemons\pokemons.json", "r") as fichier:
            donnees = json.load(fichier)

        # Rechercher les données du Pokémon avec l'ID correspondant
        pokemonName = next((pokemon for pokemon in donnees["pokemons"] if pokemon["id"] == idDonne), None)
        
        if pokemonName:
            evolutionName = pokemonName.get("name")
        return evolutionName
    

# Test de la class

starter = Pokemon (1)
starter.afficherBaseInfos()
starter.set_xp(250)
starter.afficherBaseInfos()
starter.set_xp (1600)

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600


fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Fenêtre Pygame avec Image')



image = starter.get_imageFace()
imageModifier = pygame.transform.scale(image, (200, 200))

# Obtenir la position de l'image dans la fenêtre
image_rect = image.get_rect()
image_rect.center = (largeur_fenetre // 2, hauteur_fenetre // 2)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill((0, 0, 0))  # Fond blanc

    # Dessiner l'image
    fenetre.blit(imageModifier, image_rect)
    fenetre.blit(image, (0, 25))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()