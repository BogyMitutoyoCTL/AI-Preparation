from Algorithms.Algorithms import Algorithm
from GameData import GameData


class Thomas(Algorithm):
    def __init__(self):
        super().__init__()

    def decide(self, info: GameData) -> str:
        print("Kopf ist bei ", info.head_x, " / ", info.head_y)
        print("Abstand zur Wand im Norden: ", info.walldistance_n)

        # Versuche näher zum Futter zu kommen
        if info.food_x < info.head_x:
            # Eigentlich return "west"
            # Aber lass mal vorher prüfen, ob das überhaupt geht
            if info.can_move_to(info.head_x - 1, info.head_y):
                return "west"
        if info.food_x > info.head_x:
            #Eigentlich return "east"
            if info.can_move_to(info.head_x + 1, info.head_y):
                return "east"
        if info.food_y < info.head_y:
            #Eigentlich return "north"
            if info.can_move_to(info.head_x , info.head_y - 1):
                return "north"
        if info.food_y > info.head_y:
            #Eigentlich return "south"
            if info.can_move_to(info.head_x , info.head_y + 1):
                return "south"

        # Die Schlange konnte nicht in Richtung Futter laufen, weil der Weg dorthin blockiert war
        # Daher: irgendeinen Weg suchen, wo man hinlaufen kann
        #if info.can_move_to(info.head_x - 1, info.head_y):
        #    return "west"
        #if info.can_move_to(info.head_x + 1, info.head_y):
        #    return "east"
        #if info.can_move_to(info.head_x, info.head_y - 1):
        #    return "north"
        #if info.can_move_to(info.head_x, info.head_y + 1):
        #    return "south"

        for max_distance in range(5, 0, -1):
            can_walk_north = True
            can_walk_east = True
            can_walk_south = True
            can_walk_west = True
            for distance in range(1, max_distance + 1):
                if not info.can_move_to(info.head_x - distance, info.head_y):
                    can_walk_west = False
                if not info.can_move_to(info.head_x + distance, info.head_y):
                    can_walk_east = False
                if not info.can_move_to(info.head_x, info.head_y - distance):
                    can_walk_north = False
                if not info.can_move_to(info.head_x, info.head_y + distance):
                    can_walk_south = False
            if can_walk_west:
                return "west"
            if can_walk_east:
                return "east"
            if can_walk_north:
                return "north"
            if can_walk_south:
                return "south"

        # Nix gefunden? Dann hab ich mich wohl eingezingelt
        return "straight"