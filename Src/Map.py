#Module de gestion de la map

import Draw
import Utils
import exampleClass

class tilemap(exampleClass.example):

    #Constructeur
    def __init__(self):
        self.color = (0,0,0)
        self.imgSky = Draw.createImg("Assets/sky.png")
        self.imgPipe = Draw.createImg("Assets/pipe.png")
        self.coords = (0,0)
        self.size = 32
        self.depart = 0
        self.temps = Draw.getTime()
        self.tab = Utils.loadCSV()
        self.addTemps = 400
        self.vitesse = 3

    def addVitesse(self):
        self.vitesse += 1

    def getTab(self):
        return self.tab
    
    def getSize(self):
        return self.size

    #Affichage de la map
    # screen : l'écran sur lequel affiché
    def afficheMap(self, screen):
        if self.depart > -1 * self.size:
            i = self.depart
        else:
            i = 0
            self.depart = 0
        j = 0
    
        for ligne in self.tab:
            for colonne in ligne:
                if colonne == "0":
                    self.img = self.imgSky
                else:
                    self.img = self.imgPipe
                self.coords = (i,j)
                Draw.drawBlit(screen, self)
                i+= self.size
            j+= self.size
            i = self.depart
        self.depart -= self.vitesse

    #Affichage fixe de la map pour le menu
    def affichageMapFixe(self, screen):
        i = 0
        j = 0
    
        for ligne in self.tab:
            for colonne in ligne:
                if colonne == "0":
                    self.img = self.imgSky
                else:
                    self.img = self.imgPipe
                self.coords = (i,j)
                Draw.drawBlit(screen, self)
                i+= self.size
            j+= self.size
            i = 0
            
    #Met la map à jour
    def updateMap(self):
        if self.depart <= (-1 * self.size):
            self.tab = Utils.createNextObstacle(self.tab)
            self.temps = Draw.getTime()