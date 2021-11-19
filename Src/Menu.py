#Module affichant un menu

import Map
import Player
import Draw
from Affichable import affichable
import Spacebar
import Points
import Utils

#Affichage d'un menu
def menu(screen, WIDTH, HEIGHT):
    m = Map.tilemap() 
    p = Player.joueur(WIDTH*0.1, HEIGHT/2)
    s = Spacebar.spaceBarKey(WIDTH * 0.35, HEIGHT * 0.6)
    t = affichable((WIDTH *0.3,HEIGHT* 0.1), "Assets/title.png")
    score = affichable((WIDTH * 0.8, HEIGHT*0.8), "Assets/score.png")
    pts = Points.Points(WIDTH * 0.87, HEIGHT*0.9)
    pts.setPts(Utils.loadScore())

    while True :
        Draw.clearScreen(screen)
        m.affichageMapFixe(screen)
        p.drawPlayer(screen)
        s.afficheBar(screen)
        Draw.drawBlit(screen, score, pts)
        Draw.drawBlit(screen, t)
        Draw.drawScreenUpdate()
        Draw.quit()
        p.animation()
        if Draw.spaceBarKey():#lance le jeu en mettant une attente de quelques instants 
            ecranNoir(screen)
            jeu(screen, WIDTH, HEIGHT)
            pts.setPts(Utils.loadScore())
        if Draw.escapeKey():
            exit()

def ecranNoir(screen):
    screen.fill(0)
    Draw.drawScreenUpdate()
    Draw.attente(250)

def gameOver(screen, WIDTH, HEIGHT):
    t = affichable((WIDTH *0.21,HEIGHT* 0.21), "Assets/gameOver.png")
    screen.fill(0)
    Draw.drawBlit(screen, t)
    Draw.drawScreenUpdate()
    Draw.attente(1000)

#Lance une partie
def jeu(screen, WIDTH, HEIGHT):
    m = Map.tilemap() 
    p = Player.joueur(WIDTH*0.1, HEIGHT/2)
    pts = Points.Points(10, 10)

    while True :
        Draw.clearScreen(screen)        # nettoie l'écran
        m.afficheMap(screen)            # affichage map
        p.updatePlayerMovement(screen)  # Mouvements du joueur
        p.drawPlayer(screen)            # affichage du joueur
        pts.afficherPoints(screen)      # affichage des points
        Draw.drawScreenUpdate()         # actualisation de l'écran
        Draw.quit()                     # vérification de l'état de la fenêtre (croix)
        if m.updateMap():               # Change la carte au fur et à mesure
            pts.addPoints()             # augmentation des points
        if pts.speedUp():               # augmente la vitesse de la map selon le score
            m.addVitesse()
        if p.collisions(m):             # vérifie les collisions
            gameOver(screen, WIDTH, HEIGHT)
            Utils.saveScore(pts.getPts())
            break

        if Draw.escapeKey():            # le joueur veut revenir au menu
            break