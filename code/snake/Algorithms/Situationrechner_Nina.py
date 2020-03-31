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

    # Schritt 1: wir suchen den Ausschnitt um den Kopf herum
    # Bei einer Kantenlänge von 3 müssen wir bei -1 links vom Kopf anfangen
    # und bei +1 rechts vom Kopf aufhören.
    # Kantenlänge 5: von -2 bis +2
    # Kantenlänge 7: von -3 bis +3
    beginn = int(- (kantenlänge - 1) / 2)
    ende = int((kantenlänge - 1) / 2)
    ausschnitt = []
    for deltay in range(beginn, ende + 1):
        for deltax in range(beginn, ende + 1):
            print(deltax, deltay)
            kästchen_x = field.head_x + deltax
            kästchen_y = field.head_y + deltay
            leer = field.can_move_to(kästchen_x, kästchen_y)
            if leer:
                ausschnitt.append(0)
            else:
                ausschnitt.append(1)

    # Schritt 2: in eine Zahl umwandeln
    wertigkeit = 1
    summe = 0
    # for binärziffer in ausschnitt:
    for stelle in range(kantenlänge ** 2):
        binärziffer = ausschnitt[stelle]
        maskiert = int(maske[stelle])
        if maskiert != 0:
            if binärziffer == 1:
                summe += wertigkeit
            wertigkeit = wertigkeit * 2
    # 0   1    0   0   1   0  0  0  0  Eingang
    # 1   1    1   1   0   1  1  1  1  Maske
    # 128 64   32  16      8  4  2  1

    return summe


if __name__ == "__main__":
    field = Field(10, 20)
    snake = Snake(field)

    number = situation_number(3, "111 111 111", snake.get_info())
    assert number == 16 + 128
    number = situation_number(3, "111 101 111", snake.get_info())

