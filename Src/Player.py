#Module du joueur

import exampleClass
import Draw

#Classe permettant de gérer le joueur
class joueur(exampleClass.example):

    #constructeur
    def __init__(self, coordX, coordY):
        self.img = Draw.createImg("Assets/piaf.png")
        self.h = 29
        self.w = 41
        self.rect = Draw.createRect(0, 0, self.w, self.h)
        self.temps = Draw.getTime()
        self.coords = (coordX, coordY)
        self.coordX = coordX
        self.coordY = coordY
        self.addTemps = 10
        self.addMove = 3
        self.yBase = coordY
        self.direction = 0

    def getRect(self):
        return self.rect

    #affichage du joueur
    def drawPlayer(self, screen):
        Draw.drawBlitRect(screen, self)

    #Fait chuter le joueur au fur et à mesure
    def updatePlayerChute(self):
        self.coordY +=1
        self.coords = (self.coordX, self.coordY)
        self.rect.x = 0

    #Fait monter le joueur si la touche espace est activée
    def updatePlayerMovement(self, screen):
        if Draw.spaceBarKey() and self.temps + self.addTemps <= Draw.getTime():
            self.coordY -= self.addMove
            self.temps = Draw.getTime()
            self.coords = (self.coordX, self.coordY)
            self.rect.x = self.w
            self.drawPlayer(screen)
        elif self.temps + self.addTemps <= Draw.getTime():
            self.temps = Draw.getTime()
            self.updatePlayerChute()
            self.drawPlayer(screen)

    #ajoute une animation pour le menu principal
    def animation(self):
        if self.temps + self.addTemps <= Draw.getTime():
            if self.direction == 0 and self.coordY >= self.yBase - 20:
                self.coordY -= 1
                self.rect.x = self.w
            elif self.direction == 0 and self.coordY < self.yBase - 20:
                self.direction = 1
            elif self.direction == 1 and self.coordY <= self.yBase + 20:
                self.coordY += 1
                self.rect.x = 0
            elif self.direction == 1 and self.coordY > self.yBase + 20:
                self.direction = 0

            self.coords = (self.coordX, self.coordY)
            self.temps = Draw.getTime()


    #Collisions
    def collisions(self, tilemap):
        size = tilemap.getSize()
        tab = tilemap.getTab()

        i = int(self.coordX / size)# collision haut gauche
        j = int(self.coordY / size)

        i1 = int((self.coordX + size) /size)#collission haut droite
        j1 = int(self.coordY / size)

        i2 = int(self.coordX / self.h)    #collision bas gauche
        j2 = int((self.coordY + size) /size)

        i2 = int((self.coordX + self.h) / size)    #collision bas droite
        j2 = int((self.coordY + self.h  - 2) /size)

        try:
            if tab[j][i] == "0" and tab[j1][i1] == "0" and tab[j2][i2] == "0":
                return False
            else:
                Draw.attente(500)
                return True
        except IndexError:
            return 0