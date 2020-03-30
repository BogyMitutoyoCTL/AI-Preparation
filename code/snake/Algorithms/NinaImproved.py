from Algorithms.Algorithms import Algorithm
from GameData import GameData


class NinaImproved(Algorithm):
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:
        if info.walldistance_n == 0:
            if info.head_x > info.food_x:
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_s == 0:
            if info.head_x < info.food_x:
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_e == 0:
            if info.head_y > info.food_y:
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_w == 0:
            if info.head_y < info.food_y:
                return "turn left"
            else:
                return "turn right"

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

        return "straight"
