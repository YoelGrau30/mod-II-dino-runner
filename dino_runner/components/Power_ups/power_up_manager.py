from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import SHIELD


class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        
    def update(self, game):
        if len(self.power_ups) == 0:
            self.power_ups.append(Shield(SHIELD))
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)