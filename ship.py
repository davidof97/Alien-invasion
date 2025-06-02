import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class created for ship managing"""
    
    def __init__(self, ai_game):
        """Ship initialization and his starting position"""
        
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the picture of ship
        self.image = pygame.image.load('D:/Python_projects/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #Every ship appear on the bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Position of ship is float type
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        """Update the position of ship"""
        
        #Update of X ship coordinate
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed
        
        #Update the rect object based on self.x 
        self.rect.x = self.x
        
        
    def blitime(self):
        """Display ship on his current position"""
        
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Placing the ship in the center on the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
        
        