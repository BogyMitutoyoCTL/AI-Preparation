# Command Line Magic
http://www.climagic.org/

## Wer ist im selben Netzwerk

```bash
for i in `seq 1 254` ; do ping -W1 -c 1 192.168.1.$i > /dev/null && echo 192.168.1.$i ; done
```

## Irgendwas zu einem bestimmten Zeitpunkt machen

```bash
at 12pm -f some_script.sh
```


## Files finden die größer sind als...

```bash
find / -size +5M -ls | sort -k7nr
```

andersrum sortieren...

```bash
find /etc -size +5M -ls | sort -k7n
```

## Sachen in Dateien suchen

Mit grep lassen sich Text in Dateien suchen

```bash
grep -r suchtext /etc
```

Wenn ihr *Permission denied* Fehler bekommt, könnt ihr die so loswerden:

```bash
grep -r suchtext /etc/ 2>&1 | grep -v "Permission denied" 
```

## Webserver im akutellen Verzeichnis starten

Eine einfache Möglichkeit einen Webserver zu starten:

```bash
python3 -m http.server 8080
```
Um den Zugang dazu auf die lokale Maschine zu begrenzen:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

## Tron in der Konsole

```bash
clear;x=$(($COLUMNS/2)); y=$LINES;unset spacesused[*];declare -a spacesused;xdir=0;ydir=-1;while true ; do read -s -r -t0.02 -n3 direction ; case "${direction:2:1}" in A) ydir=-1;xdir=0 ;; B)ydir=1;xdir=0 ;; C) ydir=0;xdir=1 ;; D) ydir=0;xdir=-1 ;; esac ; space=$(( $COLUMNS * $y + $x )) ; if [[ "${spacesused[$space]}" == "1" || $x -gt $COLUMNS || $x -lt 0 || $y -gt $LINES || $y -lt 0 ]]; then printf '\033[%d;%dHBOOM!\nEND OF LINE.\n' $y $x; break ; else spacesused[$space]=1 ; fi ; ox=$x; oy=$y ; x=$(( $x + $xdir )) ; y=$(( $y + $ydir )) ; printf "\033[%s;%sH\033[46m \033[0m\033[%s;%sH\033[44m \033[0m\033[0;0H" $y $x $oy $ox ; sleep 0.01 ; done
```
