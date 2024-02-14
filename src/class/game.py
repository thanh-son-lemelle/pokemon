from Menu import Menu
from Dresseurs import Dresseurs 
from Pokemon import Pokemon
from Combat import Combat
from Pokeballs import Pokeballs

while True:
    menu = Menu()
    menu.main_menu()
    print(menu.get_playgame())
    if menu.get_playgame() == True:

        
        joueur = Dresseurs("Sasha") #nom = input
        joueur.addToRoster(menu.get_pokemonChoisi())
        print(Pokemon.get_nom(joueur.get_lisPokemons()[0]))
        


        
        adversaire = Dresseurs()
        adversaire.setRandomName()
        adversaire.getRoster(1,1)


        combat = Combat()
        combat.get_liste_dresseurs(joueur.get_lisPokemons(),adversaire.get_lisPokemons())
        combat.get_nom_adv(adversaire.get_nom())
        combat.start_anim()



