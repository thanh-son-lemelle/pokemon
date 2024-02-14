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

    def load_skills(self):
        with open(self.__abilitiesPath, 'r', encoding="utf-8") as file:
            skills_data = json.load(file)
        return [ability['name'] for ability in skills_data['abilities']]

    def get_selected_skill(self):
        return self.selected_skill

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.button_rect)  # Fond blanc pour le bouton
        pygame.draw.rect(screen, (0, 0, 0), self.button_rect, 2)
        if self.selected_skill:
            text = self.font.render(self.selected_skill, True, (0, 0, 0))  # Couleur du texte en noir
            screen.blit(text, (self.x + 10, self.y + self.height // 2 - text.get_height() // 2))
        else:
            text = self.font.render("Select a skill", True, (0, 0, 0))  # Couleur du texte en noir
            screen.blit(text, (self.x + 10, self.y + self.height // 2 - text.get_height() // 2))

        if self.is_open:
            visible_skills = self.skills[self.scroll_offset:self.scroll_offset + self.max_display_items]
            for i, skill in enumerate(visible_skills):
                menu_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                pygame.draw.rect(screen, (255, 255, 255), menu_rect)  # Fond blanc pour le bouton
                pygame.draw.rect(screen, (0, 0, 0), menu_rect, 2)
                text = self.font.render(skill, True, (0, 0, 0))  # Couleur du texte en noir
                screen.blit(text, (self.x + 10, self.y + (i + 1) * self.height + self.height // 2 - text.get_height() // 2))
                self.menu_rects.append(menu_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    self.is_open = True
                elif self.is_open:
                    elementSelected = False
                    for i, rect in enumerate(self.menu_rects):
                        if rect.collidepoint(event.pos):
                            index = self.scroll_offset + i
                            
                            if index < len(self.skills) and not elementSelected:
                                self.selected_skill = self.skills[index]
                                self.is_open = False
                                elementSelected = True
                    else:
                        self.is_open = False
                
        elif event.type == pygame.MOUSEWHEEL:
            if self.is_open:
                if event.y > 0:
                    self.scroll_offset = max(0, self.scroll_offset - 1)
                else:
                    self.scroll_offset = min(len(self.skills) - self.max_display_items, self.scroll_offset + 1)