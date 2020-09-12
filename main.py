import sys
import pygame
import tictactoe

#Hilfsfunktion, um Text formatiert auszugeben und nicht alle zeilen bei jedem Text nochmal schreiben zu müssen
def renderText(parameterText, parameterSchriftGröße, parameterSchriftArt, parameterSchriftFarbe):
    schriftart = pygame.font.SysFont(parameterSchriftArt, parameterSchriftGröße)
    gerenderterText = schriftart.render(parameterText, 1, parameterSchriftFarbe)
    return gerenderterText


#Konstanten (d.h. Werte die sich nie verändern)
BREITE = 1344
HÖHE = 756
DIMENSION = [BREITE,HÖHE]  #x/y Koordinatensystem, (0,0) ist links oben!
BLAU = (0,0,255)
ROT = (255,0,0)
SCHWARZ = (0,0,0)
WEISS = (255,255,255)

#pygame und Fenster initialisieren
pygame.init()
hintergrund = pygame.image.load("grafiken/Forest_klein.png")
fenster = pygame.display.set_mode(DIMENSION) #Auflösung gibt das Hintergrundbild vor!
zeitgeber = pygame.time.Clock()
pygame.display.set_caption("TicTacToe mit pygame") #Fenstertitel setzen

#Texte fürs Hauptmenü vorbereiten
gerenderteÜbeschrift = renderText("Jonas erstes kleines Spiel in Python", 80, "Arial", ROT)
gerenderterText = renderText("Drücke die Leertaste", 50, "Arial", BLAU)

#Hilfsvariable für die nachfolgende while-Schleife
hauptmenü = True

#Hauptmenüschleife, wird solange ausgeführt bis man im Fenster oben rechts auf das X klickt oder ESCAPE drückt
while hauptmenü:
    fenster.blit(hintergrund, (0,0))
    fenster.blit(gerenderteÜbeschrift, (180,300))
    fenster.blit(gerenderterText, (450, 400))
    pygame.display.update()
    zeitgeber.tick(60) #60 Bilder pro Sekunde (fps)
    for ereignis in pygame.event.get(): #Ereignisse abfragen
        if ereignis.type == pygame.QUIT or (ereignis.type == pygame.KEYUP and ereignis.key == pygame.K_ESCAPE):
            sys.exit()
        if ereignis.type == pygame.KEYUP and ereignis.key == pygame.K_SPACE:
            hauptmenü = False
            imSpiel = True

#jetzt wird das Hauptmenü mit dem Spielbrett ausgetauscht
#Notwendige Variablen und Angaben für das eigentliche Spiel
spieler1 = tictactoe.Spieler(1)
spieler2 = tictactoe.Spieler(2)
spielbrett = tictactoe.Spielbrett()
aktiverSpieler = spieler1  #das muss sich bei jedem Zug auf den anderen Spieler ändern
spieler1.grafik = pygame.image.load("grafiken/X.png")
spieler2.grafik = pygame.image.load("grafiken/O.png")
gewonnen = False
unentschieden = False
linienfarbe = SCHWARZ
fenster.fill(WEISS)
#vertikalen Linien vom Spielfeld zeichnen
pygame.draw.line(fenster, linienfarbe, (round(BREITE / 3), 0), (round(BREITE / 3), HÖHE), 7)
pygame.draw.line(fenster, linienfarbe, (round(BREITE / 3 * 2), 0), (round(BREITE / 3 * 2), HÖHE), 7)
#horizontalen Linien vom Spielfeld zeichnen
pygame.draw.line(fenster, linienfarbe, (0, round(HÖHE / 3)), (BREITE, round(HÖHE / 3)), 7)
pygame.draw.line(fenster, linienfarbe, (0, round(HÖHE / 3 * 2)), (BREITE, round(HÖHE / 3 * 2)), 7)

#Spielschleife, wird solange ausgeführt bis man im Fenster oben rechts auf das X klickt oder ESCAPE drückt
while imSpiel:
    pygame.draw.rect(fenster, WEISS, (1,1, 200,40)) #weiße Fläche zur Anzeige des aktiven Spielers schaffen
    gerenderterText = renderText("Aktiver Spieler: " + format(aktiverSpieler.nummer), 20, "Arial", SCHWARZ)
    fenster.blit(gerenderterText, (1, 1))
    pygame.display.update()
    zeitgeber.tick(60) #60 Bilder pro Sekunde (fps)
    for ereignis in pygame.event.get():  # Ereignisse abfragen
        if ereignis.type == pygame.QUIT or (ereignis.type == pygame.KEYUP and ereignis.key == pygame.K_ESCAPE):
            sys.exit()
        elif ereignis.type is pygame.MOUSEBUTTONDOWN:
            feld = tictactoe.spieler_mausklick(pygame, BREITE, HÖHE)  #erhält als antwort (spalte, zeile) jeweils 1-3
            print(feld)  # debug ausgabe auf konsole
            #prüfen ob Zug erlaubt ist
            if spielbrett.pruefeSpielfeld(feld) == True and (not gewonnen or not unentschieden):
                print(spielbrett.holeLetztePosition()) #debug
                # Grafik in das feld zeichnen
                spielbrett.setzeSpielfeld(spielbrett.holeLetztePosition(),
                                          aktiverSpieler.nummer, aktiverSpieler.grafik, fenster, BREITE, HÖHE)
                #Hier wird nun geprüft ob das SPiel gewonnen wurde
                if spielbrett.prüfeSpielGewonnen(aktiverSpieler.nummer):
                    gewonnen = True
                    gerenderterText = renderText("Gewonnen hat Spieler " + format(aktiverSpieler.nummer), 100, "Arial", ROT)
                    fenster.blit(gerenderterText, (300, 300))
                #ist überhaupt noch ein Zug möglich (oder unentschieden?)
                if spielbrett.istUnentschieden():
                    unentschieden = True
                    gerenderterText = renderText("Unentschieden", 120, "Arial", ROT)
                    fenster.blit(gerenderterText, (300, 300))
                #aktiven Spieler wechseln
                if aktiverSpieler.nummer == 1:
                    aktiverSpieler = spieler2
                else:
                    aktiverSpieler = spieler1
            else:
                print("Spiel vorbei oder ungültiger Zug erkannt auf Feld", spielbrett.holeLetztePosition())



