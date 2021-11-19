import Draw
from Affichable import affichable
import Menu

WIDTH = 672
HEIGHT = 384

screen = Draw.create_window(WIDTH, HEIGHT, "Flappy bird", Draw.createImg("Assets/piaf2.png"))
t = affichable((WIDTH *0.15,HEIGHT* 0.1), "Assets/logo_NS.png")
Draw.drawBlit(screen, t)
Draw.drawScreenUpdate()
Draw.attente(1500)

Menu.menu(screen, WIDTH, HEIGHT)