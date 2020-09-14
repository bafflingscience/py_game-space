sheen_green = (113,119,32)    
paradise_pink = (232,63,111)
raisin_black =  (25,25,35)
honeydew = (226,252,239)
trump_jacket = (8,76,97)

class Settings:
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = raisin_black

        # ship settings
        self.ship_speed = 3.0
        self.ship_limit = 3

        # bullet settings w x h are in pixels
        self.bullet_speed = 2.0
        self.bullet_width = 10.0
        self.bullet_height = 10.0
        self.bullet_color = paradise_pink
        self.bullets_allowed = 6

        # alien settings
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.5

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.2

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)