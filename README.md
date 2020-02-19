# AI-Preparation
Vorbereitung auf die Umsetzung von Machine Learning (eine Untermenge von künstlicher Intelligenz) für das Spiel "Snake".

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

Dann haben wir uns mit dem Thema der Berufsorientierung auseinandergesetzt. Das Spielprinzip ist vermutlich hinreichend bekannt: es handelt sich um ein Snake-Spiel. Die Schlange (grün) frisst mit ihrem Kopf (blau) einen Apfel (rot) und wächst dabei. Zum Glück sind wir hier nicht an fächerübergreifenden Unterricht gebunden, ansonsten müsste man sich fragen, seit wann Schlangen vegetarisch sind (Biologie), ob nicht Adam und Eva den Apfel gegessen haben, anstatt der Schlange (Religion) und ob Schlangen mit künstlicher Intelligenz ein Bewusstsein haben, und somit überhaupt in Tierversuchen einsetzbar sind (Ethik).

Die von uns bereitgestellte Spieleumgebung ist bereits auf KI-Experimente vorbereitet, d.h. ein beliebiger Algorithmus kann in der Umgebung mehrere Spiele nacheinander ohne menschliches Zutun spielen. Zur Spieleumgebung gibt es eine Visualisierung, die folgendermaßen aufgebaut ist:

* der linke Bereich liefert statistische Daten
  * grün: Daten zur Visualisierung, derzeit nur die aktuelle Visualisierungsgeschwindigkeit in Bildern pro Sekunde (fps; frames per second)
  * hellblau: Daten zum Training, d.h. mehrere Spiele übergreifend
  * violett: Daten zum aktuell laufenden Spiel. Ein Teil dieser Daten könnte als Input für Neuronen dienen.
* der rechte Bereich visualisiert das Spielfeld
  * rot: das Futter (angeblich ein Apfel)
  * blau: der Kopf der Schlange
  * grün: Körper der Schlange, wobei die hellere Teile früher verschwinden als dunklere Teile

Im Bild sieht man einen von Mitutoyo programmierten Algorithmus, der noch keine künstliche Intelligenz nutzt. Dabei handelt es sich bewusst um einen Algorithmus, der nicht mathematisch als perfekt bewiesen ist. Unsere KI wird sich mit diesem Algorithmus messen müssen. Bei 1000 Spielen erreicht er eine Länge von bis zu 80 Kästchen, was einer Abdeckung von 40% der Fläche entspricht. 

![Snake Spiel](images/Snake.png)

Hausaufgaben:

* Github Account einrichten, damit wir später gemeinsam an einem Projekt arbeiten können

* Fotofreigabe von den Eltern ausfüllen und unterschreiben lassen

* der Whatsapp-Gruppe für das Praktikum beitreten

* bei Interesse unserem [Instagram Account](https://www.instagram.com/mitutoyoctlg/) folgen.

## Zweiter Nachmittag, 19.2.2020

Wie bereits am ersten Tag kurz vorgestellt, haben wir ein "Daily Scrum" Meeting durchgeführt, d.h. ein Meeting am Stehtisch. Die Themen im BOGY weichen etwas von den üblichen Fragen für Entwickler ab. Wir wollten wissen, ob die Hausaufgaben erledigt sind und ob es sonstige Vorkommnisse gab, die das BOGY betreffen könnten.

Bereits am ersten Nachmittag haben wir zum Schluss den Raspberry Pi in Betrieb genommen und die Oberfläche vom Betriebssystem Raspbian kennengelernt. Heute haben wir uns etwas mehr mit den Innereien von Linux beschäftigt: Die [Linux Präsentation](presentation/Linux.pptx) erklärt den grundsätzlichen Aufbau, ist allerdings theoretischer Natur. Daher haben wir diese Präsentation gekürzt, indem wir Teile in ausgeblendeten Folien versteckt haben. Die [Bash Präsentation](presentation/Bash.pptx) zeigt, was man auf er Linux Kommandozeile alles tun kann und hat den deutlich höheren Praxisanteil. 

Wir schließen diese beiden Teile ab mit der Behauptung: wer ein guter Hacker werden möchte, kommt um Linux nicht herum. (Der Begriff Hacker wird hier in seinem positiven Sinn als Tüftler mit Sinn für kreativen Umgang mit Technik verstanden)

Uns blieb dann noch Zeit für die [Einführung in PyCharm](presentation/Pycharm.pptx). Da wir PyCharm bereits auf dem Raspberry Pi installiert hatten, haben wir den Installations-Teil übersprungen (Anleitung verbleibt auch hier in versteckten Folien) und haben uns ganz auf die Features dieser IDE (Integrated Development Environment) konzentriert.



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

