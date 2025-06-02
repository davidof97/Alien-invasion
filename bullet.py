import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullet managing"""
    
    def __init__(self, ai_game):
        """Bullet creating on the actual ship position"""
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Create rectangle on the position (0,0) and then defining his proper position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #The bullet position is float
        self.y = float(self.rect.y)
        
        
    def update(self):
        """Moving the bullet on the screen"""
        #Update bullet position
        self.y -= self.settings.bullet_speed
        #Update the rectangle of bullet position
        self.rect.y = self.y
            
            
    def draw_bullet(self):
        """Display the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    