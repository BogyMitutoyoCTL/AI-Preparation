from Algorithms.Algorithms import Algorithm
from GameData import GameData


class David(Algorithm):  # Passe den Klassen-Namen hier an
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:
        if info.nearest_wall_distance == 0:
            return "turn left"

        if info.food_y == info.head_y:
            return "east"
        if info.food_x == info.head_x:
            return "north"
        return "straight"
