import Draw
from Affichable import affichable

screen = Draw.create_window(704, 416, "Flappy bird")
t = affichable((0,0), "Assets/logo_NS.png")
while 1 :
    Draw.drawBlit(screen,t)
    Draw.drawScreenUpdate()
    Draw.attente(2500)
    exit()