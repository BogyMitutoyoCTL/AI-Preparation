from Field import Field
from GameData import GameData
from Snake import Snake

#   1    2    4
#
#   8    -    16
#
#   32   64   128

def situation_number(kantenlänge: int, maske: str, field: GameData):
    if field.can_move_to(field.head_x, field.head_y) == False:
        # belegt

    return 0 # was ausgerechnetes

if __name__ == "__main__":
    field = Field(10, 20)
    snake = Snake(field)
    number = situation_number(3, "111 111 111", field)
    assert number == 16+128
    number = situation_number(3, "111 101 111", field)
    assert number == 64