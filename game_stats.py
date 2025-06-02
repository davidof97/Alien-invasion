class GameStats:
    """Game stats monitoring in Alien Invasion game"""
    
    def __init__(self, ai_game):
        """Initialization of statistical data"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start game in active mode
        self.game_active = False
        
        #Best score
        self.high_score = 0
    
    
    def reset_stats(self):
        """Initialization of statistical data which can be change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1