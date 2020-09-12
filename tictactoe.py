def spieler_mausklick(pygame, breite, hoehe):
    # Mauskoordinaten abfragen
    x, y = pygame.mouse.get_pos()

    # Spalte bestimmen (1-3)
    if (x < breite / 3):
        spalte = 1
    elif (x < breite / 3 * 2):
        spalte = 2

    elif (x < breite):
        spalte = 3
    else:
        spalte = None

    # Zeile bestimmen (1-3)
    if (y < hoehe / 3):
        zeile = 1

    elif (y < hoehe / 3 * 2):
        zeile = 2

    elif (y < hoehe):
        zeile = 3

    else:
        zeile = None

    return spalte, zeile

class Spieler:
    nummer = None
    __geschützt = "irgendein privates Attribut der Klasse" #nur als Beispiel
    grafik = None

    #Konstruktor
    def __init__(self, nummer):
        self.nummer = nummer

class Spielbrett:

    __spielfeld = [0,0,0,0,0,0,0,0,0] #3x3 Felder also 9 Elemente, 0 ist links oben, 9 = rechts unten
    __letztePosition = None
    def __init__(self):
        pass

    def pruefeSpielfeld(self, koordinaten):
        spalte = koordinaten[0]
        zeile = koordinaten[1]
        if zeile == 1:
            position = spalte
        if zeile == 2:
            position = spalte + 3
        if zeile == 3:
            position = spalte + 6
        self.__letztePosition = position
        return (self.__spielfeld[position - 1] == 0)  #Achtung! Index beginnt bei 0 daher 1 abziehen

    def holeLetztePosition(self):
        return self.__letztePosition

    def setzeSpielfeld(self, position, spielernummer, grafik, fenster, breite, höhe):
        self.__spielfeld[position - 1] = spielernummer #Achtung! Index beginnt bei 0 daher 1 abziehen
        zbreite = (round(breite / 3) / 3)
        zhoehe = round(höhe / 3) / 3
        if position == 1:
            x = zbreite
            y = zhoehe
        if position == 2:
            x = zbreite + round(breite / 3)
            y = zhoehe
        if position == 3:
            x = zbreite +  3 * zbreite + round(breite / 3)
            y = zhoehe
        if position == 4:
            x = zbreite
            y = zhoehe + round(höhe / 3)
        if position == 5:
            x = zbreite + round(breite / 3)
            y = zhoehe + round(höhe / 3)
        if position == 6:
            x = zbreite +  3 * zbreite + round(breite / 3)
            y = zhoehe + round(höhe / 3)
        if position == 7:
            x = zbreite
            y = zhoehe +  2 * round(höhe / 3)
        if position == 8:
            x = zbreite + round(breite / 3)
            y = zhoehe +  2 * round(höhe / 3)
        if position == 9:
            x = zbreite +  3 * zbreite + round(breite / 3)
            y = zhoehe +  2 * round(höhe / 3)

        fenster.blit(grafik, (x, y))

    def prüfeSpielGewonnen(self, aktiverspieler):
        #index beginnt bei 0, spielfeld für menschen bei 1, also ist der höchste index 8 und nicht 9
        #erste reihe , felder 1-3, komplett?
        if (self.__spielfeld[0] == aktiverspieler) and (self.__spielfeld[1] == aktiverspieler) and (self.__spielfeld[2] == aktiverspieler):
            return True
        # zweite reihe , felder 4-6, komplett?
        if (self.__spielfeld[3] == aktiverspieler) and (self.__spielfeld[4] == aktiverspieler) and (self.__spielfeld[5] == aktiverspieler):
            return True
        # dritte reihe , felder 7-9, komplett?
        if (self.__spielfeld[6] == aktiverspieler) and (self.__spielfeld[7] == aktiverspieler) and (self.__spielfeld[8] == aktiverspieler):
            return True
        # erste spalte , felder 1,4,7 komplett?
        if (self.__spielfeld[0] == aktiverspieler) and (self.__spielfeld[3] == aktiverspieler) and (self.__spielfeld[6] == aktiverspieler):
            return True
        # zweite spalte , felder 2,5,8 komplett?
        if (self.__spielfeld[1] == aktiverspieler) and (self.__spielfeld[4] == aktiverspieler) and (self.__spielfeld[7] == aktiverspieler):
            return True
        # dritte spalte , felder 3,6,9 komplett?
        if (self.__spielfeld[2] == aktiverspieler) and (self.__spielfeld[5] == aktiverspieler) and (self.__spielfeld[8] == aktiverspieler):
            return True
        #Diagonale über felder 1,5,9 komplett?
        if (self.__spielfeld[0] == aktiverspieler) and (self.__spielfeld[4] == aktiverspieler) and (self.__spielfeld[8] == aktiverspieler):
            return True
        #Diagonale über felder 3,5,7 komplett?
        if (self.__spielfeld[2] == aktiverspieler) and (self.__spielfeld[4] == aktiverspieler) and (self.__spielfeld[6] == aktiverspieler):
            return True
        return False;

    def istUnentschieden(self):
        return (0 not in self.__spielfeld)