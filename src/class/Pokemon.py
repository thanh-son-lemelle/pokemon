#!/usr/bin/env python3
import json
import pygame
import sys
import copy

class Pokemon:
    def __init__(self, id ) -> None:
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
        self.__imageFace = None
        self.__imageBack = None
        self.loadData()
        
        self.__abilities = self.get_currentAbilities()

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
    
    def get_imageFace(self):
        self.__imageFace = self.resizeImage(self.__imageFace, 2) # à voir si Utile ou pas
        return self.__imageFace
    
    def get_imageBack(self):
        self.__imageBack = self.resizeImage(self.__imageBack, 2) # à voir si Utile ou pas
        return self.__imageBack
    
    def get_level(self):
        return self.__level
    
    def set_level(self, level):
        while self.__level < level:
            self.level_up()
        
    
    def get_growth(self):
        return self.__growth
    
    def get_pokemonData(self):
        return self.__pokemonData
    
    def get_abilities(self):
        return self.__abilities
    
    def get_4abilities(self):
        if len(self.__abilities) < 4:
            while len(self.__abilities) < 4:
                self.__abilities.append("-")
            
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
        # Si les données ont été trouvées, on les charge
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

    # Test de l'affichage des stats
    def afficherBaseStats(self):
            
            print(f"#{self.__id} {self.__name} - Type: {self.__type1, self.__type2}")
            print("Stats de base:")
            for baseStat, value in self.__baseStats.items():
                print(f"  {baseStat.capitalize()}: {value}")
            print(f"  Level: {self.__level}")
            print(f"  XP: {self.__xp}")
            if self.__evolution:
                print(f"Évolution: Niveau {self.__evolution['level']} vers {self.__evolution['to']}")
            print("\n")

    def afficherStats(self):
        if self.__stats:

            print(f"#{self.__id} {self.__name} - Type: {self.__type1, self.__type2}")
            print("Stats actuelles:/niveau:")
            for stat, value in self.__stats.items():
                print(f"  {stat.capitalize()}: {value}")
            print(f"  Level: {self.__level}")
            print(f"  XP: {self.__xp}")
            print("\n")
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
        # gestion de l'xp, du level up et de l'évolution
#============================================================================

    def set_xp(self, AddXp): # xp gagnée à définir dans la class Combat
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
                        # break (utile ou pas ?)
    def level_up(self):

        self.__level += 1
        self.get_currentAbilities()

        self.growUp()
        self.afficherBaseStats()
        self.afficherStats()
    def updateStats(self):
        self.__stats = self.__baseStats.copy()

    def growUp(self):
            self.updateStats()
            for stat in self.__baseStats.keys():
                self.__stats[stat] = int(((2 * self.__baseStats[stat] * self.__level)/100) + self.__level +10)
  



        # Prend les valeurs de l'évolution id name stat etc...
    def evolue (self):
        evolutionName = self.get_name_by_id(self.__id + 1)
        print(f"{self.__name} a évolué en {evolutionName} !")

        self.__id = self.__evolution.get("to")
        self.loadData()
        self.updateStats()
        print(self.afficherBaseStats())

    def get_name_by_id(self, idDonne):
        with open(r"data\pokemons\pokemons.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
        # Rechercher les données du Pokémon avec l'ID correspondant
        pokemonName = None
        for pokemon in donnees["pokemons"]:
            if pokemon["id"] == idDonne:
                pokemonName = pokemon["name"]
                break
        if pokemonName:
            evolutionName = pokemonName
        return evolutionName
#============================================================================
        # gestion des abilities
#============================================================================

    def get_abilitiesFromPokemonData(self):

        self.__abilities = self.__pokemonData.get("abilities")


    def get_AbilitiesByLevel(self):

        abilities = []
        self.get_abilitiesFromPokemonData()
        print (abilities)
        for ability in self.__abilities:
            abilityLevel = ability ["level"]
            if abilityLevel <= self.__level:
                abilities.append(ability["name"])
        self.__abilities = abilities
        return self.__abilities
    
    def chooseAbilities(self):
        chooseAbilities = []
        self.get_AbilitiesByLevel()
        chooseAbilities = self.__abilities
        self.__abilities = []
        print(f"Choisissez les abilities de {self.__name}:")
        dialogue1 =f"Choisissez les abilities de {self.__name}:"
        dialogue2 = ""
        for ability in chooseAbilities:
            print(f"  {ability}")
            dialogue2 += f"  {ability}"
        print("\n")
        for i in range(4):
            ability = input(f"Ability {i+1}: ")
            while True:
                # Verifier que l'ability existe
                if ability not in chooseAbilities:
                    print("Ability invalide !")
                    dialogue3 = "Ability invalide !"
                    ability = input(f"Ability {i+1}: ")
                # Verifier que l'ability n'est pas déjà dans la liste
                elif ability in self.__abilities:
                    print(f"{ability} est déjà dans la liste !")
                    dialogue4 = f"{ability} est déjà dans la liste !"
                    ability = input(f"Ability {i+1}: ")
            self.__abilities.append(ability)
            print(self.__abilities)
        print("\n")
        print(f"Les abilities de {self.__name} sont maintenant:")
        for ability in self.__abilities:
            print(f"  {ability}")
        print("\n")
        return self.__abilities
    
    def get_currentAbilities(self):
        print("test") # a revoir me ressor deux listes vide
        self.get_AbilitiesByLevel()
        if len(self.get_AbilitiesByLevel()) > 4:
            # L'utilisateur choisi les 4 abilities qu'il veut garder
            self.chooseAbilities()
        self.__abilities = self.__abilities[0:4]
        return self.__abilities
    
    def get_ability(self, index):   #fonctionnel
        return self.__abilities[index]
    
    def get_ability_by_name(self, name): #fonctionnel
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
    # Renvoie les stats de l'ability à l'index donné vu avec Lyes Hamici pour l'appel de la fonction plus facile à utiliser par la suite
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
#============================================================================
    # Traitement des images
#============================================================================
    
    def resizeImage(self, image, multiplier):
        newHeight = None
        originalWidth, originalHeight = image.get_size()
        newHeight = int(multiplier * originalHeight)
        newWidth = int(multiplier * originalWidth)
        image = pygame.transform.scale(image, (newWidth, newHeight))
        return image

    
"""
# Test de la class
"""
starter = Pokemon (4)
starter.set_level(50)
print(starter.get_4abilities())
print(starter.get_abilityStatsByIndex(0)) #marche pas
print(starter.get_abilities())
print(starter.get_abilityStats("Poudre Toxik")) #marche pas
print(starter.get_AbilitiesByLevel())
print(starter.get_ability_by_name("Poudre Toxik"))
print(starter.get_abilityAccuracyByName("Poudre Toxik"))
print(starter.get_abilityCategoryByName("Poudre Toxik"))
print(starter.get_abilityPowerByName("Poudre Toxik"))
print(starter.get_abilityTypeByName("Poudre Toxik"))
print(starter.get_abilityStats("Poudre Toxik"))
print(starter.get_abilityStatutChangeByName("Poudre Toxik")["turns"])
print(starter.get_abilityStatutChangeByName("Poudre Toxik"))

print(starter.get_ability(0))
print(starter.get_pokemonData())



pygame.init()

largeur_fenetre = 1000
hauteur_fenetre = 500


fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Fenêtre Pygame avec Image')



image = starter.get_imageFace()

# Obtenir la position de l'image dans la fenêtre
image_rect = image.get_rect()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill((255,255,255))  # Fond blanc

    # Dessiner l'image
<<<<<<< HEAD
    fenetre.blit(image, image_rect)

=======
    fenetre.blit(starter.get_imageFace(), image_rect)
    fenetre.blit(starter.get_imageBack(), image_rect)
    fenetre.blit(starter.get_imageBack(), image_rect2)
    fenetre.blit(starter.get_imageFace(), image_rect3)
    fenetre.blit(image, (0, 25))
>>>>>>> Pokedex

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Quitter Pygame
pygame.quit()
sys.exit()
