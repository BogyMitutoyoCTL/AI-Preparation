from Algorithms.Algorithms import Algorithm
from GameData import GameData


class PerfectButBoring(Algorithm):
    """
    This algorithm implements the most obvious Hamilton cycle.
    Thus, the result will be perfect, but the snake is very slow because it simply visits every available
    pixel of the playfield to make sure it will eat the food eventually.

    Best result: length 200 on a 10x20 field in 1 epoch. Plays perfect!
    """

    def __init__(self):
        super().__init__()
        self.state = 0

    def decide(self, info: GameData) -> str:
        if info.head_y == 0:
            if info.head_x == 0:
                return "south"
            return "west"

        if info.walldistance_e == 0:
            if info.head_y > 0:
                return "north"
        if info.walldistance_s == 0:
            return "east"

        if info.head_x < info.field_width - 2:
            if not info.is_body(info.head_x + 1, info.head_y):
                return "east"
        if info.head_x > 0:
            if not (info.is_body(info.head_x - 1, info.head_y)):
                return "west"

        if info.walldistance_e == 1:
            return "south"

        return "south"