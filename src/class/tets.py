import pygame
import sys

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Initialiser la fenêtre Pygame
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Tableau avec Pygame')

# Charger une police
police = pygame.font.Font(None, 36)

# Données du tableau
tableau_data = [
    ["Cpt 0", "Cpt 1", "Cpt 2", "Cpt 3", "Cpt 4"],
    ["Cpt 5", "Cpt 6", "Cpt 7", "Cpt 8", "Cpt 9"],	
    ["Cpt 10", "Cpt 11", "Cpt 12", "Cpt 13", "Cpt 14"],
]

# Dimensions du tableau
cellule_largeur = 85
cellule_hauteur = 35
margeHauteur = 10
margeLargeur = 100

# Position initiale du tableau
x = margeHauteur
y = margeLargeur

# Boucle principale
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Dessiner le tableau
    for i, ligne in enumerate(tableau_data):
        for j, cellule in enumerate(ligne):
            pygame.draw.rect(fenetre, NOIR, (x + j * (cellule_largeur + margeLargeur), y + i * (cellule_hauteur + margeHauteur), cellule_largeur, cellule_hauteur), 2)
            texte_surface = police.render(cellule, True, NOIR)
            texte_rect = texte_surface.get_rect(center=(x + j * (cellule_largeur + margeLargeur) + cellule_largeur // 2,
                                                        y + i * (cellule_hauteur + margeHauteur) + cellule_hauteur // 2))
            fenetre.blit(texte_surface, texte_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()