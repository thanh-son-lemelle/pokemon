#!/usr/bin/env python3
import json
import pygame
import random

class Pokemon:
    def __init__(self, id ) -> None:
        # Initialisation de l'objet Pokemon avec un ID
        self.__id = id
        self.__pokemonData = None
        self.__name = None
        self.__type1 = None
        self.__type2 = None
        self.__stats = None
        self.__baseStats = None
        self.__growth = None 
        self.__evolution = None
        self.__level = 1
        self.__xp = 0
        self.__abilities = []
        self.loadData() # Chargement des données du Pokémon depuis pokémon.json
        
        self.__abilities = self.get_initAbilities()

#============================================================================
        # setter et getter
#============================================================================
    def get_id(self):
        return self.__id

    def get_nom(self):
        return self.__name

    def get_type1(self):
        return self.__type1
    
    def get_type2(self):
        return self.__type2
    
    def get_baseStats(self):
        return self.__baseStats

    def get_stats(self):
        return self.__stats

    def get_evolution(self):
        return self.__evolution
    
    def get_xp(self):
        return self.__xp
    
    
    def get_level(self):
        return self.__level
    
    def set_level(self, level):
        while self.__level < level:
            self.level_up() # Monter de niveau jusqu'au niveau spécifié
          
    def get_growth(self):
        return self.__growth
    
    def get_pokemonData(self):
        return self.__pokemonData
    
    def get_abilities(self):
        return self.__abilities
    
    def get_4abilities(self):
        if len(self.__abilities) < 4:
            while len(self.__abilities) < 4:
                self.__abilities.append("-") # Ajouter des capacités vides si nécessaire
        
        return self.__abilities[0:4]
    
    def get_vu(self):
        return self.__pokemonData["vu"]

#============================================================================
        # stat de base
#============================================================================
    
    # Charge les données du fichier pokemon.json
    def loadData(self):
        with open(r"data\pokemons\pokemons.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
        # Rechercher les données du Pokémon avec l'ID correspondant
        self.__pokemonData = None
        for pokemon in donnees["pokemons"]:
            if pokemon["id"] == self.__id:
                self.__pokemonData = pokemon
                break
        # Si les données ont été trouvées, on les charges
        if self.__pokemonData:
            self.__name = self.__pokemonData.get("name")
            self.__type1 = self.__pokemonData.get("type1")
            self.__type2 = self.__pokemonData.get("type2")
            self.__baseStats = self.__pokemonData.get("stats")
            if self.__stats is None:
                self.growUp()
            self.__evolution = self.__pokemonData.get("evolution")
            # Chargement des images           
            self.__imageFace = pygame.image.load(f"images\\sprite_pokemon\\front\\{self.__id}.gif")
            self.__imageBack = pygame.image.load(f"images\\sprite_pokemon\\back\\{self.__id}.gif")

#============================================================================
            # getter des stats
#============================================================================

    def get_statHp(self):
        return self.__stats["hp"]
    
    def get_statAttack(self):
        return self.__stats["attack"]
    
    def get_statDefense(self):
        return self.__stats["defense"]
    
    def get_statSpeed(self):
        return self.__stats["speed"]
    
    def get_statSpecialAttack(self):
        return self.__stats["sp_attack"]
    
    def get_statSpecialDefense(self):  
        return self.__stats["sp_defense"]
    
#============================================================================
            # setter des stats
#============================================================================
    def set_statHp(self, value):
        self.__stats["hp"] += value
    
    def set_statAttack(self, value):
        self.__stats["attack"] += value

    def set_statDefense(self, value):
        self.__stats["defense"] += value

    def set_statSpeed(self, value):
        self.__stats["speed"] += value
    
    def set_statSpecialAttack(self, value):
        self.__stats["sp_attack"] += value

    def set_statSpecialDefense(self, value):
        self.__stats["sp_defense"] += value
        
#============================================================================
        # gestion de l'xp, du level up et de l'évolution
#============================================================================

    def set_xp(self, AddXp): # xp gagnée à définir dans la class Combat
        self.__xp += AddXp

        if self.__xp >= 100:
            while self.__xp >= 100:
                self.level_up()
                self.__xp -= 100
                if self.__evolution is not None:
                    if self.__level >= self.__evolution["level"]:
                        self.evolue()
    
    def level_up(self):
        self.__level += 1
        self.get_currentAbilities()

        self.growUp()
    
    def updateStats(self):
        self.__stats = self.__baseStats.copy()

    def growUp(self):
            self.updateStats()
            for stat in self.__baseStats.keys():
                self.__stats[stat] = int(((2 * self.__baseStats[stat] * self.__level)/100) + self.__level +10)
  

    # Prend les valeurs de l'évolution id name stat etc...
    def evolue (self):
        self.__id = self.__evolution.get("to")
        self.loadData()
        self.updateStats()

#============================================================================
        # gestion des abilities
#============================================================================

    def get_abilitiesFromPokemonData(self):
        self.__abilities = self.__pokemonData.get("abilities")


    def get_AbilitiesByLevel(self):
        abilities = []
        self.get_abilitiesFromPokemonData()
        for ability in self.__abilities:
            abilityLevel = ability ["level"]
            if abilityLevel <= self.__level:
                abilities.append(ability["name"])
        self.__abilities = abilities
        return self.__abilities
    
    def chooseAbilities(self, newlist): #test pending
        self.__abilities = newlist
        return self.__abilities
    
    
    def get_currentAbilities(self):
        self.__abilities=self.get_AbilitiesByLevel()
        return self.__abilities
    
    def get_initAbilities(self):
        self.get_AbilitiesByLevel()
        if len(self.get_AbilitiesByLevel()) > 4:
            self.chooseRandomAbility()
        self.__abilities = self.__abilities[0:4]
        return self.__abilities
    
    def chooseRandomAbility(self):
        self.get_AbilitiesByLevel()
        chooseAbilities = self.__abilities.copy()
        self.__abilities = []
        for i in range(4):
            ability = random.choice(chooseAbilities)
            self.__abilities.append(ability)
            chooseAbilities.remove(ability)

        return self.__abilities
    
    def get_ability(self, index):
        return self.__abilities[index]
    
    def get_ability_by_name(self, name):
        for ability in self.__abilities:
            if ability == name:
                return ability
        return None
    
    def get_abilityStats(self, name):
        ability = self.get_ability_by_name(name)
        with open(r"data\abilities\abilities.json", "r", encoding="utf-8") as fichier:
            abilityStats = json.load(fichier)
        for ability in abilityStats["abilities"]:
            if ability["name"] == name:
                return ability["stats"]
        return None
    
    # Renvoie les stats de la compétence à l'index donné vu avec Lyes Hamici pour l'appel de la fonction plus facile à utiliser par la suite
    def get_abilityStatsByIndex(self, index):
        name = self.get_ability(index)
        return self.get_abilityStats(name)
    
    def get_abilityNameByIndex(self, index):
        return self.get_ability(index)
#============================================================================
        # gestion des stats des attaques
#============================================================================
    
    def get_abilityPowerByName(self, name):
        abilityStats = self.get_abilityStats(name)
        return abilityStats["power"]
    
    def get_abilityAccuracyByName(self, name):
        abilityStats = self.get_abilityStats(name)
        return abilityStats["accuracy"]
    
    def get_abilityTypeByName(self, name):
        abilityStats = self.get_abilityStats(name)
        return abilityStats["type"] 
    
    def get_abilityCategoryByName(self, name):
        abilityStats = self.get_abilityStats(name)
        return abilityStats["category"]
    
    def get_abilityStatutChangeByName(self, name):
        abilityStats = self.get_abilityStats(name)
        return abilityStats["status_changes"]



