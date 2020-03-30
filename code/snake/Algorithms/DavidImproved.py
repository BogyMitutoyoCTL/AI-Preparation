from Algorithms.Algorithms import Algorithm
from GameData import GameData


class DavidImproved(Algorithm):
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:
        if info.food_y == info.head_y:
            if info.food_x > info.head_x:
                return "east"
            else:
                return "west"
        if info.food_x == info.head_x:
            if info.food_y > info.head_y:
                return "south"
            else:
                return "north"
        if info.distance_to_wall_in_current_direction == 0:
            return "turn left"
        return "straight"
