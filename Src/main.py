import Draw
from Affichable import affichable
import Map
import Player

WIDTH = 672
HEIGHT = 384

screen = Draw.create_window(WIDTH, HEIGHT, "Flappy bird")
m = Map.tilemap() 
p = Player.joueur(WIDTH*0.1, HEIGHT/2)
#t = affichable((0,0), "Assets/logo_NS.png")

while True :
    Draw.clearScreen(screen)
    m.afficheMap(screen)
    p.updatePlayerMovement(screen)
    p.drawPlayer(screen)
    Draw.drawScreenUpdate()
    p.collisions(m)
    Draw.quit()