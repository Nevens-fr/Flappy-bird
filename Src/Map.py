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
        self.tab = Utils.loadCSV()

    #Affichage de la map
    # screen : l'écran sur lequel affiché
    def afficheMap(self, screen):
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

    def updateMap(self):
        self.tab = Utils.createNextObstacle(self.tab)