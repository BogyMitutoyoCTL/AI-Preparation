from Algorithms.Algorithms import Algorithm
from GameData import GameData


class Nina(Algorithm):
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:

        if info.walldistance_n == 0:
            if info.head_x > info.food_x :
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_s == 0 :
            if info.head_x < info.food_x:
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_e == 0 :
            if info.head_y < info.food_y:
                return "turn left"
            else:
                return "turn right"
        if info.walldistance_w == 0 :
            if info.head_y > info.food_y :
                return "turn left"
            else:
                return "turn right"

        return "straight"




