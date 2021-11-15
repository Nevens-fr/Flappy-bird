import Draw
from Affichable import affichable
import Map
import Player

screen = Draw.create_window(672, 384, "Flappy bird")
m = Map.tilemap()
p = Player.joueur(672*0.1, 382/2)
#t = affichable((0,0), "Assets/logo_NS.png")
i = 0
while i < 1 :
    m.afficheMap(screen)
    Draw.drawRect(screen, p)
    Draw.drawScreenUpdate()
    Draw.attente(2500)
    i+=1
    m.updateMap()