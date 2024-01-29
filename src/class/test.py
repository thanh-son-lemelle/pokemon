import pygame
import sys

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Initialiser la fenêtre Pygame
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Zone de texte avec Pygame')

# Charger une police
police = pygame.font.Font(None, 36)

# Créer une zone de texte
zone_texte = pygame.Rect(200, 200, 400, 50)
texte = ''
saisie_active = False

# Boucle principale
while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if zone_texte.collidepoint(evenement.pos):
                saisie_active = not saisie_active
            else:
                saisie_active = False
        elif evenement.type == pygame.KEYDOWN:
            if saisie_active:
                if evenement.key == pygame.K_RETURN:
                    print(texte)  # Faites quelque chose avec le texte saisi
                    texte = ''
                elif evenement.key == pygame.K_BACKSPACE:
                    texte = texte[:-1]
                else:
                    texte += evenement.unicode
    # Effacer l'écran
    fenetre.fill(BLANC)

    # Dessiner la zone de texte
    pygame.draw.rect(fenetre, NOIR, zone_texte, 2)
    
    # Dessiner le texte saisi
    texte_surface = police.render(texte, True, NOIR)
    fenetre.blit(texte_surface, (zone_texte.x + 5, zone_texte.y + 5))

    # Mettre à jour l'affichage
    pygame.display.flip()