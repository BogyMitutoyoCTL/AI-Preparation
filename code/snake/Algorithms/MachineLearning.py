import glob
import json
import os
import pickle
from Algorithms.Algorithms import Algorithm
from GameData import GameData
from RewardSystem import RewardSystem


class MachineLearning(Algorithm):
    def __init__(self):
        super().__init__()
        self.wörterbuch = {"north": 0, "east": 1, "south": 2, "west": 3, 0: "north", 1: "east", 2: "south", 3: "west"}
        self.impossible_move = "-"
        self.keine_entscheidung = ""
        self.anzahl_blickrichtungen = 5
        self.maske = "01110 11111 11011 11111 01110"
        self.kantenlänge = 5
        self.dateiname = "gelernt "+self.maske + " " + str(self.anzahl_blickrichtungen) + ".pickle"
        if os.path.exists(self.dateiname):
            with open(self.dateiname, "rb") as datei:
                self.würfel = pickle.load(datei)
        else:
            self.würfel = self.leere_struktur_aufbauen()
        self.iq = 0
        self.last_saved_iq = 0

        self.reward_system = RewardSystem()
        # Belohnungen
        self.reward_system.reward_eat_food = 1
        self.reward_system.reward_win = 1
        self.reward_system.reward_closer_function = lambda distance: 1 if distance > 0 else -1
        # Bestrafungen
        self.reward_system.reward_killed_by_wall = -1
        self.reward_system.reward_killed_by_tail = -1
        self.reward_system.reward_impossible_move = -1
        self.reward_system.reward_killed_by_starving_function = lambda step, length: 0

    def anzahl_felder_im_blickfeld(self):
        anzahl = 0
        for buchstabe in self.maske:
            if buchstabe == "1":
                anzahl += 1
        return anzahl

    def decide(self, info: GameData) -> str:
        situation = self.situation_number(self.kantenlänge, self.maske, info)
        scheibe = self.würfel[situation]

        essensrichtung = self.blickrichtung_zum_essen(info)
        säule = scheibe[essensrichtung]

        aktion = self.beste_aktion_wählen(säule)
        return aktion

    def beste_aktion_wählen(self, säule):
        maximum = 0
        position_des_maximums = -1
        for position in range(len(säule)):
            zuversichtlichkeit = säule[position]
            if zuversichtlichkeit > maximum:
                maximum = zuversichtlichkeit
                position_des_maximums = position

        aktion = self.wörterbuch[position_des_maximums]
        return aktion

    def blickrichtung_zum_essen(self, info):
        winkel = info.food_direction + 360  # negative Zahlen loswerden
        winkel = winkel % 360  # Zahlen über 360 loswerden
        essensrichtung = int(winkel / (360 / self.anzahl_blickrichtungen))
        return essensrichtung

    def leere_struktur_aufbauen(self):
        # Aufbau siehe Präsentation Folie 9
        würfel = []
        for spielfeldnummer in range(2 ** self.anzahl_felder_im_blickfeld()):
            scheibe = []
            for blickrichtung in range(self.anzahl_blickrichtungen):
                säule = []
                for aktion in range(4):
                    säule.append(0.5)
                scheibe.append(säule)
            würfel.append(scheibe)
        return würfel

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

    def train(self, info: GameData, action, reward) -> None:
        situation = self.situation_number(self.kantenlänge, self.maske, info)
        essensrichtung = self.blickrichtung_zum_essen(info)

        aktionsnummer = self.wörterbuch[action]

        # Zuversichtlichkeit anpassen basierend auf reward
        scheibe = self.würfel[situation]
        säule = scheibe[essensrichtung]

        if säule == [0.5, 0.5, 0.5, 0.5] and reward != 0:
            self.iq += 1
            print("Wieder was gelernt! ", self.iq)

        if reward == 1:
            säule[aktionsnummer] *= 1.1
            if säule[aktionsnummer] > 1:
                säule[aktionsnummer] = 1
        elif reward == 0:
            pass
        else:  # -1
            säule[aktionsnummer] *= 0.9
            if säule[aktionsnummer] < 0.01:
                säule[aktionsnummer] = 0.01

    def epochfinished(self) -> (object, float):
        if self.iq > self.last_saved_iq + 50:
            with open(self.dateiname, "wb") as datei:
                pickle.dump(self.würfel, datei)
            self.last_saved_iq = self.iq
        return None, 0.0

    def epsilon(self, epoch: int, maxepochs: int) -> float:
        if epoch < maxepochs/2:
            return 0.3

        return 0
