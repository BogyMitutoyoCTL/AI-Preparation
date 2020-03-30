from Algorithms.Algorithms import Algorithm
from GameData import GameData


class Blerijan(Algorithm):  # Passe den Klassen-Namen hier an
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:
        print("Kopf ist bei",info.head_x," / ",info.head_y)
        print("Abstand zur Wand im Norden: ", info.walldistance_n)
        if info.walldistance_n == 0:
            return "turn left"
            return "turn left"
        print("Kopf zur Wand im Süden: ",info.walldistance_s)
        if info.walldistance_s == 0:
            return "turn left"
        print("Kopf zur Wand im Westen: ", info.walldistance_w)
        if info.walldistance_w == 0:
            return "turn left"
        print("Kopf zur Wand im Osten: ", info.walldistance_e)
        if info.walldistance_e == 0:
            return "turn left"
        return "straight"
        if info.food < 2:
            return "turn right"






