import pygame
import json
import os

class DropdownMenu:
    def __init__(self, x, y, width, height):
        self.__abilitiesPath = os.path.join('data', 'abilities', 'abilities.json')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_display_items = 8
        self.skills = self.load_skills()
        self.selected_skill = None
        self.is_open = False
        self.font = pygame.font.Font(None, 14)
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.menu_rects = []
        self.scroll_offset = 0 

    # Charge les compétences depuis le fichier abilities.json
    def load_skills(self):
        with open(self.__abilitiesPath, 'r', encoding="utf-8") as file:
            skills_data = json.load(file)
        return [ability['name'] for ability in skills_data['abilities']]

    # Récupère la compétence sélectionnée
    def get_selected_skill(self):
        return self.selected_skill

    # Dessine le menu déroulant
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.button_rect)  # Fond blanc pour le bouton
        pygame.draw.rect(screen, (0, 0, 0), self.button_rect, 2) # Bordure noire pour le bouton
        if self.selected_skill:
            text = self.font.render(self.selected_skill, True, (0, 0, 0))  # Couleur du texte en noir
            screen.blit(text, (self.x + 10, self.y + self.height // 2 - text.get_height() // 2))
        else:
            text = self.font.render("Select a skill", True, (0, 0, 0))  # Couleur du texte en noir
            screen.blit(text, (self.x + 10, self.y + self.height // 2 - text.get_height() // 2))

        if self.is_open:
            visible_skills = self.skills[self.scroll_offset:self.scroll_offset + self.max_display_items] # On affiche seulement les éléments visibles
            for i, skill in enumerate(visible_skills):
                menu_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                pygame.draw.rect(screen, (255, 255, 255), menu_rect)  # Fond blanc pour le bouton
                pygame.draw.rect(screen, (0, 0, 0), menu_rect, 2)
                text = self.font.render(skill, True, (0, 0, 0))  # Couleur du texte en noir
                screen.blit(text, (self.x + 10, self.y + (i + 1) * self.height + self.height // 2 - text.get_height() // 2)) # On ajoute le texte au menu
                self.menu_rects.append(menu_rect) # On ajoute le rectangle du menu à la liste des rectangles

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button_rect.collidepoint(event.pos): # Si on clique sur le bouton, on ouvre le menu
                    self.is_open = True
                elif self.is_open: #
                    elementSelected = False
                    for i, rect in enumerate(self.menu_rects): # On parcourt les rectangles des éléments du menu
                        if rect.collidepoint(event.pos):
                            index = self.scroll_offset + i
                            
                            if index < len(self.skills) and not elementSelected: # Si on clique sur un élément du menu, on le sélectionne
                                self.selected_skill = self.skills[index]
                                self.is_open = False
                                elementSelected = True
                    else: # Si on clique en dehors du menu, on le ferme
                        self.is_open = False
                
        elif event.type == pygame.MOUSEWHEEL: # Gestion de la molette de la souris pour le défilement
            if self.is_open:
                if event.y > 0: # Si on scroll vers le haut
                    self.scroll_offset = max(0, self.scroll_offset - 1) # On décrémente le décalage
                else:
                    self.scroll_offset = min(len(self.skills) - self.max_display_items, self.scroll_offset + 1) # On incrémente le décalage