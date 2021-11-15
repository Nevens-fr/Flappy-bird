import pygame as pg

# Création et set up de la fenetre
def create_window(width, height, title):
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode((width, height))

    pg.display.set_caption(title)

    #pg.display.set_icon(logo)
    return screen

#Nettoie l'écran des images résiduelles
def clearScreen(screen):
    screen.fill(0)

def attente(temps):
    pg.time.wait(temps)
        
#Retourne une image
def createImg(path):
    return pg.image.load(path)
    	
#Retourne un rectangle
def createRect(left, top, width, height):
   	return pg.Rect(left, top, width, height)
   		
#Retourne le temps en millisecondes
def getTime():
   	return pg.time.get_ticks()
        
#Render texte
def rendertexte(font, texte, bool, color):
    return font.render(texte , bool, color)

#Applique tous les changements sur l'écrans
def drawScreenUpdate():
    pg.display.flip()

#Blit les surfaces sur l'écran
def drawBlit(screen, *arg):
    for x in arg:
        screen.blit(x.getImg(), x.getCoords())

#Dessine des rectangles
def drawRect(screen, *arg):
    for x in arg:
        pg.draw.rect(screen, x.getColor(), x.getImg())


########################################################################
########## KEYBOAD #####################################################

#Getter de la liste des touches
def getEvent():
    return pg.key.get_pressed()

#renvoie vrai si la touche espace est utilisée
def spaceBarKey():
    event = getEvent()
    return event[pg.K_SPACE]

#Quitte la fenetre si la croix est utilisée
def quit():
    for events in pg.event.get():
        if events.type == pg.QUIT:
            exit()

def escapeKey():
    event = getEvent()
    return event[pg.K_ESCAPE]