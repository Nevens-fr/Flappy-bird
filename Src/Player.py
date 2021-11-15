#Module du joueur

import exampleClass
import Draw

#Classe permettant de gérer le joueur
class joueur(exampleClass.example):

    #constructeur
    def __init__(self, coordX, coordY):
        self.img = Draw.createImg("Assets/piaf.png")
        self.temps = Draw.getTime()
        self.coords = (coordX, coordY)
        self.coordX = coordX
        self.coordY = coordY
        self.addTemps = 10
        self.addMove = 5
        self.yBase = coordY
        self.direction = 0

    #affichage du joueur
    def drawPlayer(self, screen):
        Draw.drawBlit(screen, self)

    #Fait chuter le joueur au fur et à mesure
    def updatePlayerChute(self):
        self.coordY +=1
        self.coords = (self.coordX, self.coordY)

    #Fait monter le joueur si la touche espace est activée
    def updatePlayerMovement(self, screen):
        if Draw.spaceBarKey() and self.temps + self.addTemps <= Draw.getTime():
            self.coordY -= self.addMove
            self.temps = Draw.getTime()
            self.coords = (self.coordX, self.coordY)
            self.drawPlayer(screen)
        elif self.temps + self.addTemps <= Draw.getTime():
            self.temps = Draw.getTime()
            self.updatePlayerChute()
            self.drawPlayer(screen)

    #ajoute une animation pour le menu principal
    def animation(self):
        if self.temps + self.addTemps <= Draw.getTime():
            if self.direction == 0 and self.coordY >= self.yBase - 20:
                self.coordY -= 2
            elif self.direction == 0 and self.coordY < self.yBase - 20:
                self.direction = 1
            elif self.direction == 1 and self.coordY <= self.yBase + 20:
                self.coordY += 2
            elif self.direction == 1 and self.coordY > self.yBase + 20:
                self.direction = 0

            self.coords = (self.coordX, self.coordY)
            self.temps = Draw.getTime()


    #Collisions
    def collisions(self, tilemap):
        size = tilemap.getSize()
        tab = tilemap.getTab()

        i = int(self.coordX / size)
        j = int(self.coordY / size)

        try:
            if tab[j][i] == "0":
                return False
            else:
                return True
        except IndexError:
            return 0