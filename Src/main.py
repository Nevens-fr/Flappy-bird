import Draw
from Affichable import affichable
import Menu

WIDTH = 672
HEIGHT = 384

screen = Draw.create_window(WIDTH, HEIGHT, "Flappy bird")
t = affichable((WIDTH *0.1,HEIGHT* 0.1), "Assets/logo_NS.png")
Draw.drawBlit(screen, t)
Draw.drawScreenUpdate()
Draw.attente(2500)

Menu.menu(screen, WIDTH, HEIGHT)