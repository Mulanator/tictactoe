import sys
import pygame
import tictactoe

DIMENSION = [1344,756]
ROT = (0,0,255)
BLAU = (255,0,0)

#pygame und Fenster initialisieren
pygame.init()
hintergrund = pygame.image.load("grafiken/Forest_klein.png")
fenster = pygame.display.set_mode(DIMENSION) #Auflösung gibt das Hintergrundbild vor!
zeitgeber = pygame.time.Clock()
pygame.display.set_caption("TicTacToe mit pygame") #Fenstertitel setzen

#Schriftart vorbereiten
schriftfarbe = ROT #RGB Werte für Rot, Grün, Blau
schriftart = pygame.font.SysFont("Arial", 80)
überschrift = "Mein erstes kleines Spiel in Python"
gerenderteÜbeschrift = schriftart.render(überschrift, 1, schriftfarbe)
schriftart = pygame.font.SysFont("Arial", 50)
text = "Drücke die Leertaste"
textgröße = schriftart.size(text)
schriftfarbe = BLAU
gerenderterText = schriftart.render(text, 1, schriftfarbe)

hauptmenü = True #Hilfsvariable für die nachfolgende while-Schleife

#Hauptschleife, wird solange ausgeführt bis man im Fenster oben rechts auf das X klickt oder ESCAPE drückt
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
            spieler1 = tictactoe.Spieler
            spieler2 = tictactoe.Spieler
            pass #TODO hier neuen Screen initalisieren und tictactoe brett anzeigen