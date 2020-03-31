from Field import Field
from GameData import GameData
from Snake import Snake


#   1    2    4
#
#   8    -    16
#
#   32   64   128

def situation_number(kantenlänge: int, maske: str, field: GameData):
    maske = maske.replace(" ", "")

    beginn = int(- (kantenlänge - 1) / 2)
    ende = int((kantenlänge - 1) / 2)
    auschnitt = []
    for deltay in range(beginn, ende + 1):
        for deltax in range(beginn, ende + 1):
            print(deltax, deltay)
            kästchen_x = field.head_x + deltax
            kästchen_y = field.head_y + deltay
            leer = field.can_move_to(kästchen_x, kästchen_y)
            if leer:
                auschnitt.append(0)
            else:
                auschnitt.append(1)
    # Schritt 2: in eine Zahl umwandeln
    wertigkeit = 1
    summe = 0
    # for Binearziffer in auschnitt:
    for stelle in range(kantenlänge ** 2):
        Binearziffer = auschnitt[stelle]
        maskiert = int(maske[stelle])
        if maskiert != 0:
            if Binearziffer == 1:
                summe += wertigkeit
            wertigkeit = wertigkeit * 2

    return summe


if __name__ == "__main__":
    field = Field(10, 20)
    snake = Snake(field)
    number = situation_number(3, "111 111 111", snake.get_info())
    assert number == 16 + 128
    number = situation_number(3, "111 101 111", snake.get_info())
    assert number == 64
