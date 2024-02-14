import pygame

class TextInputBox:
    def __init__(self, x, y, width, height,fontSize=32, default_text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('black')
        self.color_active = pygame.Color('red')
        self.font = pygame.font.Font(None, fontSize) # Police de caractère fontsize def à 32 si pas défini
        self.text = default_text # Texte par défaut set a '' en attribut si pas défini
        self.txt_surface = self.font.render(default_text, True, self.color_inactive) # Surface de texte
        self.active = False # Par défaut, le rectangle n'est pas actif
        self.color = self.color_inactive # Couleur par défaut
    # Gère les événements de la class
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color_inactive)
    # Met à jour la taille du rectangle
    def update(self):
        if self.text != '':
            width = max(40, self.txt_surface.get_width()+10)
        
            self.rect.w = width
    # Dessine le rectangle
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
    # Récupère le texte saisie
    def get_text(self):
        return self.text