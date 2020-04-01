import glob
import json

from Algorithms.Algorithms import Algorithm
from GameData import GameData


class HumanDecisions(Algorithm):
    def __init__(self):
        super().__init__()
        self.impossible_move = "-"
        self.keine_entscheidung = ""
        self.anzahl_blickrichtungen = 5
        self.file_name_pattern = "../decisionrecorder/output*.json"
        self.maske = "111 101 111"
        self.kantenlänge = 3

    def anzahl_felder_im_blickfeld(self):
        anzahl = 0
        for buchstabe in self.maske:
            if buchstabe == "1":
                anzahl += 1
        return anzahl

    def decide(self, info: GameData) -> str:
        struktur = self.leere_struktur_aufbauen()

        # Dateien suchen
        dateinamen = glob.glob(self.file_name_pattern)
        dateinamen.sort()

        # alle gefundenen Dateien lesen
        for dateiname in dateinamen:
            self.eine_datei_einlesen(dateiname, struktur)

        situation = self.situation_number(self.kantenlänge, self.maske, info)
        alle_entscheidungen_für_situation = struktur[situation]

        essensrichtung = self.blickrichtung_zum_essen(info)
        entscheidung = alle_entscheidungen_für_situation[essensrichtung]

        aktion = self.entscheidung_zu_aktion(entscheidung)
        return aktion

    def entscheidung_zu_aktion(self, entscheidung):
        wörterbuch = {"N": "north", "S": "south", "E": "east", "W": "west"}
        aktion = wörterbuch[entscheidung]
        return aktion

    def blickrichtung_zum_essen(self, info):
        winkel = info.food_direction + 360  # negative Zahlen loswerden
        winkel = winkel % 360  # Zahlen über 360 loswerden
        essensrichtung = int(winkel / (360 / self.anzahl_blickrichtungen))
        return essensrichtung

    def leere_struktur_aufbauen(self):
        struktur = []
        for spielfeldnummer in range(2 ** self.anzahl_felder_im_blickfeld()):
            struktur.append([self.keine_entscheidung] * self.anzahl_blickrichtungen)
        return struktur

    def eine_datei_einlesen(self, dateiname, struktur):
        with open(dateiname) as datei:  # entspricht: datei = open(dateiname)
            datensätze = json.load(datei)

            for datensatz in datensätze:
                situationsnummer = datensatz["field"]
                essensrichtung = datensatz["food"]
                entscheidung = datensatz["decision"]
                existierende_entscheidung = struktur[situationsnummer][essensrichtung]
                if existierende_entscheidung == self.keine_entscheidung:
                    struktur[situationsnummer][essensrichtung] = entscheidung
                else:
                    if existierende_entscheidung != entscheidung:
                        if existierende_entscheidung == self.impossible_move:
                            struktur[situationsnummer][essensrichtung] = entscheidung
                        elif entscheidung != self.impossible_move:
                            # print("Ungleiche Entscheidung gefunden für ", situationsnummer, essensrichtung)
                            # print("     bisherige Entscheidung: ", existierende_entscheidung)
                            # print("     zusätzlich gefunden:    ", entscheidung)
                            pass

    def situation_number(self, kantenlänge: int, maske: str, field: GameData):
        maske = maske.replace(" ", "")
        binary_digits = self.get_binary_digits(field, kantenlänge)
        decimal = self.decimal_from_binary(binary_digits, kantenlänge, maske)
        return decimal

    def decimal_from_binary(self, ausschnitt, kantenlänge, maske):
        # 0   1    0   0   1   0  0  0  0  Eingang
        # 1   1    1   1   0   1  1  1  1  Maske
        # 128 64   32  16      8  4  2  1  Wertigkeit

        wertigkeit = 1
        summe = 0
        for stelle in range(kantenlänge ** 2):
            binärziffer = ausschnitt[stelle]
            maskiert = int(maske[stelle])
            if maskiert != 0:
                if binärziffer == 1:
                    summe += wertigkeit
                wertigkeit = wertigkeit * 2

        return summe

    def get_binary_digits(self, field, kantenlänge):
        # Wir suchen den Ausschnitt um den Kopf herum
        # Bei einer Kantenlänge von 3 müssen wir bei -1 links vom Kopf anfangen
        # und bei +1 rechts vom Kopf aufhören.
        # Kantenlänge 5: von -2 bis +2
        # Kantenlänge 7: von -3 bis +3
        beginn = int(- (kantenlänge - 1) / 2)
        ende = int((kantenlänge - 1) / 2)
        ausschnitt = []
        for deltay in range(beginn, ende + 1):
            for deltax in range(beginn, ende + 1):
                kästchen_x = field.head_x + deltax
                kästchen_y = field.head_y + deltay
                leer = field.can_move_to(kästchen_x, kästchen_y)
                if leer:
                    ausschnitt.append(0)
                else:
                    ausschnitt.append(1)
        return ausschnitt
