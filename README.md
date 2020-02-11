# AI-Preparation
Vorbereitung auf die Umsetzung von Machine Learning für das Spiel "Snake".

Dieses Projekt entstand als Teil der Berufsorientierung für Gymnasien (BOGY) für das [Leibnitz-Gymnasium in Rottweil](https://lg.rw.schule-bw.de/home/?page_id=11268) im Schuljahr 2019/2020. Als Firmenpartner steht [Mitutoyo CTL in Oberndorf](http://www.mitutoyo-ctl.de/de/karriere/ausbildungundstudium) mit Hardware, Räumlichkeiten und Ansprechpartnern zur Verfügung.

Inspiration für dieses Projekt war das [Leibniz Forschungszentrum](https://lg.rw.schule-bw.de/home/?cat=120) mit einer Idee, die Bewegung von Ameisen vom Computer vorherzusagen. Die Original-Idee beinhaltete ein Terrarium mit echten Ameisen, Kamera usw. Eine solch reale Umgebung birgt jedoch Schwierigkeiten, die mit den Rahmenbedingungen eines Praktikums schlecht vereinbar sind, z.B.:

* wer kümmert sich um die Ameisen? Möglicherweise sterben sie ausgerechnet alle am ersten Tag der Praktikumswoche.
* wie nehmen die Teilnehmer das Ergebnis samt Ameisen mit nach Hause, um es Eltern und Freunden zu zeigen?
* sind die Ergebnisse reproduzierbar? Wir können bei einer fehlerhaften Umsetzung nicht nochmal am gleichen Startpunkt begonnen.
* passt das Projekt in den Zeitrahmen?

Aus diesem Grund haben wir uns entschlossen, zwar ein Machine Learning Projekt durchzuführen, aber die Bedingungen zu unseren Gunsten anzupassen. Entstanden ist ein Snake-Spiel, bei dem der Computer selbst die Spielregeln erlernen soll.

# Vorbereitung / Einführung

## Erster Nachmittag, 12.2.2020

Am ersten Nachmittag haben wir uns zunächst vorgestellt und dann durch die Firma geführt, um die Räumlichkeiten kennenzulernen.

Die [Firmenpräsentation](presentation/Firmenpräsentation.pptx) ging noch etwas darüber hinaus und erklärt unser Motto, nennt die von uns entwickelte Software, erklärt das duale Studium und zeigt Beispiele von Praktikumsprojekten.

Wir haben uns die Hardware angeschaut, auf dem wir das Projekt durchführen möchten. Es handelt sich um einen [Raspberry Pi 4](presentation/Raspberry%20Hardware.pptx), der Dank der Speichererweiterung auf 4 GB auch größere Datenmengen verarbeiten kann, wie sie bei Machine Learning auftreten.

# Projekt-Umgebung

## Software

Wir verwenden kostenlose Software: 

* das Betriebssystem [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
* die Programmiersprache [Python](https://www.python.org/)
* die Bibliotheken [Tensorflow](https://www.tensorflow.org/), [Keras](https://keras.io/) und [OpenAI Gym](https://gym.openai.com/)
* die Entwicklungsumgebung [PyCharm von JetBrains](https://www.jetbrains.com/de-de/pycharm/)

## Daten

Im Rahmen des Projekts erzeugen sich die Daten aus dem Spielverlauf selbst.

Zum Verständnis der unterschiedlichen Arten von Machine Learning verwenden wir jedoch auch:

* die [MNIST Datenbank von handgeschriebenen Ziffern](http://www.pymvpa.org/datadb/mnist.html), lizensiert unter [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

