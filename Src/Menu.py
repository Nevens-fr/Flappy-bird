#Module affichant un menu

import Map
import Player
import Draw

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
            ecranNoir(screen)
            break

        if Draw.escapeKey():            # le joueur veut revenir au menu
            break