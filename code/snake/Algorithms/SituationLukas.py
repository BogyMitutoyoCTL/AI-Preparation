from Field import Field
from GameData import GameData
from Snake import Snake

#   1    2    4
#
#   8    -    16
#
#   32   64   128


#   1   2   4   8   16
#   32  64  -   128 256


class maske:

    def __init__(self, kantenlaenge, maskenbezeichnung: str):
        self.bezeichnung = maskenbezeichnung
        self.kantenlaenge = kantenlaenge
        self.fields = []
        self.vektoren = []

    def maskenbezeichnungAuswerten(self):
        self.bezeichnung = self.bezeichnung.replace(" ","")
        for number in self.bezeichnung:
            self.fields.append(number)

    def vektorenBerechnen(self):
        self.maskenbezeichnungAuswerten()
        ende = int((self.kantenlaenge - 1) / 2)    #beginn = -ende
        beginn = 0 - ende

        for y in range(beginn, ende+1):
            for x in range(beginn, ende+1):
                if self.fields.pop(0) == "1":
                    self.vektoren.append((x,y))
                else:
                    self.vektoren.append(0)

def situation_number(maske: maske, field: GameData):
    ergebnis = 0
    wertigkeit = 1
    for i in range(0, maske.kantenlaenge ** 2):
        if maske.vektoren[i] == 0:
            pass
        else:
            vektor = tuple(maske.vektoren[i])
            if field.can_move_to(field.head_x + vektor[0], field.head_y + vektor[1]) == False:
                ergebnis += wertigkeit
            wertigkeit *= 2


    return ergebnis # was ausgerechnetes

if __name__ == "__main__":
    field = Field(10, 20)
    snake = Snake(field)
    Game = GameData()
    maske = maske(3,"111 111 111")
    maske.vektorenBerechnen()
    print(situation_number(maske, snake.get_info()))

