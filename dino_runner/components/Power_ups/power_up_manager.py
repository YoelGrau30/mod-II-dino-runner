from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import SHIELD
import random


class PowerUpManager:

    POWER_UP_PROBABILITY = 1

    def __init__(self):
        self.power_ups = []

    def generate_power_up(self):
        if random.randint(0, 100) < self.POWER_UP_PROBABILITY:
            self.power_ups.append(Shield(SHIELD))
        
    def update(self, game):
        if len(self.power_ups) == 0:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)