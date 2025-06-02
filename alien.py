import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class presenting one alien on the fleet"""
    
    def __init__(self, ai_game):
        """Alien initialization and defining his entry position"""
            
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('D:/Python_projects/alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    
    
    def check_edges(self):
        """Return true if alien reach the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
        
    def update(self):
        """Moving the alien to the rigth or left side"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x