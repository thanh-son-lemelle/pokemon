from Menu import Menu
from Dresseurs import Dresseurs 
from Pokemon import Pokemon
from Combat import Combat
from Pokeballs import Pokeballs

while True:
    menu = Menu()   # Create an instance of the Menu
    menu.main_menu()    # Call the main_menu() method
    if menu.get_playgame() == True:
        #creation du joueur
        #display pour rentrer en input le nom du joueur
        
        joueur = Dresseurs("Sasha") #nom = input
        joueur.addToRoster(menu.get_pokemonChoisi())
        


        
        adversaire = Dresseurs()
        adversaire.getRoster(1,3)


        combat = Combat()
        combat.get_liste_dresseurs(joueur.get_lisPokemons(),adversaire.get_lisPokemons())
        combat.get_nom_adv(adversaire.get_nom())
        combat.start_anim()



