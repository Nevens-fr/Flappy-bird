#Module affichant un menu

import Map
import Player
import Draw
from Affichable import affichable

#Affichage d'un menu
def menu(screen, WIDTH, HEIGHT):
    m = Map.tilemap() 
    p = Player.joueur(WIDTH*0.1, HEIGHT/2)

    while True :
        Draw.clearScreen(screen)
        m.afficheMap(screen)
        p.drawPlayer(screen)
        Draw.drawScreenUpdate()
        Draw.quit()
        p.animation()
        if Draw.spaceBarKey():#lance le jeu en mettant une attente de quelques instants 
            ecranNoir(screen)
            jeu(screen, WIDTH, HEIGHT)
        if Draw.escapeKey():
            exit()

def ecranNoir(screen):
    screen.fill(0)
    Draw.drawScreenUpdate()
    Draw.attente(250)

def gameOver(screen, WIDTH, HEIGHT):
    t = affichable((WIDTH *0.25,HEIGHT* 0.25), "Assets/gameOver.png")
    screen.fill(0)
    Draw.drawBlit(screen, t)
    Draw.drawScreenUpdate()
    Draw.attente(1000)

#Lance une partie
def jeu(screen, WIDTH, HEIGHT):
    m = Map.tilemap() 
    p = Player.joueur(WIDTH*0.1, HEIGHT/2)

    while True :
        Draw.clearScreen(screen)        # nettoie l'écran
        m.afficheMap(screen)            # affichage map
        p.updatePlayerMovement(screen)  # Mouvements du joueur
        p.drawPlayer(screen)            # affichage du joueur
        Draw.drawScreenUpdate()         # actualisation de l'écran
        Draw.quit()                     # vérification de l'état de la fenêtre (croix)
        m.updateMap()                   # Change la carte au fur et à mesure
        if p.collisions(m):                 # vérifie les collisions
            gameOver(screen, WIDTH, HEIGHT)
            break

        if Draw.escapeKey():            # le joueur veut revenir au menu
            break