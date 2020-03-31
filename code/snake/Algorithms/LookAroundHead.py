from Algorithms.Algorithms import Algorithm
from GameData import GameData

FREE = 0
FOOD = 1
BLOCKED = 2


class LookAroundHead(Algorithm):
    """


    Best result: 47
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_head_view_with_food(info: GameData):
        surrounding = [[0 for x in range(-1, 2)] for x in range(-1, 2)]
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                can_move = info.can_move_to(info.head_x + dx, info.head_y + dy)
                is_food = info.is_food(info.head_x + dx, info.head_y + dy)

                if not can_move:
                    surrounding[dy + 1][dx + 1] = BLOCKED
                elif can_move and not is_food:
                    surrounding[dy + 1][dx + 1] = FREE
                elif can_move and is_food:
                    surrounding[dy + 1][dx + 1] = FOOD

        return surrounding

    def decide(self, info: GameData) -> str:
        head_view = self.get_head_view_with_food(info)

        direction = info.food_direction

        # Try going into the direction of the food
        if (-90 - 45) < direction <= (-90 + 45):  # food is above
            if head_view[0][1] in (FREE, FOOD):  # can go north
                return "north"

        elif (0 - 45) < direction <= (0 + 45):  # food is right
            if head_view[1][2] in (FREE, FOOD):  # can go east
                return "east"

        elif (90 - 45) < direction <= (90 + 45):  # food is below
            if head_view[2][1] in (FREE, FOOD):  # can go south
                return "south"

        elif direction > (90 + 45) or direction <= (-90 - 45):  # food is left
            if head_view[1][0] in (FREE, FOOD):  # can go west
                return "west"

        # If that's not possible, go anywhere if free
        if head_view[0][1] == FREE:
            return "north"
        if head_view[2][1] == FREE:
            return "south"
        if head_view[1][2] == FREE:
            return "east"
        if head_view[1][0] == FREE:
            return "west"

        # If this point is reached, the Snake will probably die
        return "straight"
