# Snake

## Python unter Windows 10 installieren

Für dieses Projekt brauchen wir Python 3.7! Python 3.8 funktioniert leider nicht, weil Tensorflow dafür noch nicht vorbereitet ist.
Außerdem wird zwingend die 64-Bit Version von Python 3.7 benötigt.

Python kann hier heruntergeladen werden: https://www.python.org/downloads/

## Virtuelle Umgebung anlegen

1. Im Menü: File / Setting auswählen.
2. Im Baum: Project xxx / Project Interpreter auswählen.
3. Auf das Zahnrad klicken und *Add...* auswählen.
4. *Virtualenv Environment* auswählen.
5. *New Environment* auswählen und auf Python 3.7 einstellen.
6. *Ok* anklicken
7. Warten, bis die virtuelle Umgebung eingerichtet ist. 

## PIP und Setuptools aktualisieren

Bei der Aktualisierung von PIP und SetupTools in Pycharm kommt es derzeit zu einem Fehler. Führe daher folgende Schritte aus:

1. Wechsle zum Terminal
2. Gib ein: `py -m pip install --upgrade --ignore-installed pip`
3. Gib ein: `py -m pip install --upgrade --ignore-installed setuptools`


## Pakete für Snake installieren

Die Pakete, die wir für das Spiel Snake brauchen, findet Ihr in der Datei **requirements.txt**. 

Um diese Pakete in unserer virtuellen Umgebung zu installieren, müssen wir das Terminal nochmals bemühen:

1. Gib ein: `pip install -r requirements.txt`

## Snake starten

Um Snake zu starten könnt ihr auf der Konsole eingeben:

```bash
(venv) C:\snake>py snake.py
```
