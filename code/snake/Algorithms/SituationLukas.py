from GameData import GameData

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
                    pass

    def situation_berechnen(self, field: GameData):
        ergebnis = 0
        wertigkeit = 1
        for i in range(0, len(self.vektoren)):
            vektor = tuple(self.vektoren[i])
            if field.can_move_to(field.head_x + vektor[0], field.head_y + vektor[1]) == False:
                ergebnis += wertigkeit
            wertigkeit *= 2
        return ergebnis
