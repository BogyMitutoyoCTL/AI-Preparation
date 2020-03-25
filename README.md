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

Wie bereits am ersten Tag kurz vorgestellt, haben wir ein "Daily Scrum" Meeting durchgeführt. Die Themen im BOGY weichen etwas von den üblichen Fragen für Entwickler ab. Wir wollten wissen, ob die Hausaufgaben erledigt sind und ob es sonstige Vorkommnisse gab, die das BOGY betreffen könnten.

Bereits am ersten Nachmittag haben wir zum Schluss den Raspberry Pi in Betrieb genommen und die Oberfläche vom Betriebssystem Raspbian kennengelernt. Heute haben wir uns etwas mehr mit den Innereien von Linux beschäftigt: Die [Linux Präsentation](presentation/Linux.pptx) erklärt den grundsätzlichen Aufbau, ist allerdings theoretischer Natur. Daher haben wir diese Präsentation gekürzt, indem wir Teile in ausgeblendeten Folien versteckt haben. Die [Bash Präsentation](presentation/Bash.pptx) zeigt, was man auf er Linux Kommandozeile alles tun kann und hat den deutlich höheren Praxisanteil. 

Wir schließen diese beiden Teile ab mit der Behauptung: wer ein guter Hacker werden möchte, kommt um Linux nicht herum. (Der Begriff Hacker wird hier in seinem positiven Sinn als Tüftler mit Sinn für kreativen Umgang mit Technik verstanden)

## Dritter Nachmittag, 4.3.2020

Wir starteten mit der [Einführung in PyCharm](presentation/Pycharm.pptx). Da wir PyCharm bereits auf dem Raspberry Pi installiert hatten, haben wir den Installations-Teil übersprungen (die Anleitung verbleibt in versteckten Folien) und haben uns ganz auf die Features dieser IDE (Integrated Development Environment) konzentriert.

Danach legten wir los mit den ersten Schritten in der [Programmiersprache Python](presentation/Python%20Einführung.pptx), um Unterschiede zu anderen Programmiersprachen kennen zu lernen und mit der Syntax vertraut zu werden.

Hausaufgaben:

* Python 3 zu Hause installieren

* [PyCharm Community Edition](https://www.jetbrains.com/de-de/pycharm/download/#section=windows) zu Hause installieren

* bei Interesse eine mathematische [Aufgabe von Project Euler](https://projecteuler.net/archives) lösen

## Vierter Nachmittag, 11.3.2020

Beim Standup Meeting haben wir uns erkundigt, ob die Hausaufgaben Probleme bereitet haben. Dann haben wir bei Folie 44 der [Python Präsentation](presentation/Python%20Einführung.pptx) weitergemacht, wo wir letztes Mal aus Zeitgründen aufgehört haben.

Hinzu kam dann eine Einführung in [Objektorientierung mit Python](presentation/Python%20Objektorientierung.pptx). Dort kamen wir bis Folie 17 und haben mehrere tausend Hunde (Objekte vom Typ Hund) das virtuelle Licht der virtuellen Welt erblicken lassen. Es gab auch für uns Neues zu erlernen, z.B. dass es Jack Russel Jack Parson Terrier Mischlinge gibt.

## Fünfter Nachmittag, 18.3.2020

Aufgrund des Corona-Virus fiel die Berufsorientierung schulweit aus. Auch die Mitutoyo CTL Germany GmbH befand sich komplett im Home Office. Wir haben unser Team gefragt, ob es an einer Fortführung online interessiert wäre. Alle vier Teilnehmer waren dafür. Darüber freuten wir uns sehr 😊. Als Plattform haben wir [GotoMeeting](https://www.gotomeeting.com/de-de/meeting/meeting-beitreten?sc_lang=de-de) verwendet. Davon hat unsere Firma Lizenzen, so dass wir unbegrenzt konferieren konnten.

Wir haben mit der [Objektorientierung mit Python](presentation/Python%20Objektorientierung.pptx) ab Folie 18 weitergemacht, d.h. gleich mit der nächsten Aufgabe, eine Klasse Quader zu erstellen.

Im Anschluss haben wir uns mit dem Thema [Versionskontrolle allgemein](presentation/Versionskontrolle.pptx) beschäftigt, bevor wir dann konkret auf Git eingegangen sind. Für den heutigen Tag haben wir extra eine Präsentation für [Git unter Windows](presentation/Git%20Grundlagen%20-%20Windows.pptx) angelegt. Normalerweise würden wir [Git für Linux](presentation/Git%20Grundlagen.pptx) erklären, da der Raspberry ein Linux Betriebssystem hat. Die Unterschiede halten sich in Grenzen. Es unterscheidet sich lediglich die Installation der Tools. 

Wir finden Versionskontrolle praktisch und können nur empfehlen, das auch privat einzusetzen, beispielsweise für Ausarbeitungen im Rahmen einer GFS (gleichwertige Feststellung von Schülerleistungen).

## Sechster Nachmittag, 25.3.2020

Der heutige Tag befasste sich mit dem Thema [Künstliche Intelligenz](presentation/Künstliche%20Intelligenz.pptx). Ebenfalls in einer Online-Session haben wir geschaut, wie der Stand der Technik bei künstlicher Intelligenz ist, wo sich maschinelles Lernen in der Informatik einordnet und welche Probleme es dabei geben kann.

Ebenfalls besprochen haben wir, wie wir in der Praktikumswoche verfahren möchten. Dieser Vorschlag kam von uns:

* Wir treffen uns morgens um **9:00 Uhr** für eine gemeinsame Besprechung, ggf. mit Präsentation oder Erklärungen.

* Danach gibt es eine Programmieraufgabe, die jeder daheim implementieren kann.

* Bei Fragen und Problemen gibt es die Möglichkeit, die Betreuer bei Mitutoyo anzurufen.

* Von 12:00 bis 13:00 Uhr ist Mittagspause

* Um **13:00 Uhr** treffen wir uns wieder, um die Ergebnisse der Programmieraufgabe zu besprechen.

* Direkt im Anschluss folgt wieder eine Präsentation o.ä., gefolgt von einer weiteren Programmieraufgabe, genau wie am Vormittag.

* Um **16:30 Uhr** kommen wir wieder gemeinsam zusammen, um die Aufgabe zu besprechen.

Da wir bei Mitutoyo nicht genügend GotoMeeting Lizenzen haben, um täglich drei Meetings online zu halten, haben wir die Firma [Discord](https://discordapp.com/) gefragt, ob wir für das Praktikum Discord auch kommerziell nutzen dürfen. Wir freuen uns über die Zusage.

# Projekt-Umgebung

## Software

Wir verwenden kostenlose Software: 

* das Betriebssystem [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
* die Programmiersprache [Python](https://www.python.org/)
* die Versionsverwaltung [Git](https://git-scm.com/) mit dem Provider [Github](https://github.com/)
* dazu unter Windows den [Editor Notepad++](https://notepad-plus-plus.org/) und das Difftool [Winmerge](https://winmerge.org/?lang=de)
* die Bibliotheken [Tensorflow](https://www.tensorflow.org/), [Keras](https://keras.io/) und [OpenAI Gym](https://gym.openai.com/)
* die Entwicklungsumgebung [PyCharm von JetBrains](https://www.jetbrains.com/de-de/pycharm/) (Community Edition)

## Daten

Im Rahmen des Projekts erzeugen sich die Daten aus dem Spielverlauf selbst.

Zum Verständnis der unterschiedlichen Arten von Machine Learning verwenden wir jedoch auch:

* die [MNIST Datenbank von handgeschriebenen Ziffern](http://www.pymvpa.org/datadb/mnist.html), lizensiert unter [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

