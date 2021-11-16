import Draw
import exampleClass

#Classe permettant d'afficher une barre espace animée sur le menu
class spaceBarKey(exampleClass.example):
    #constructeur
    def __init__(self, coordX, coordY):
        self.imgClicked = Draw.createImg("Assets/clicked_spacebar.png")
        self.imgNClicked = Draw.createImg("Assets/spacebar.png")
        self.coords = (coordX,coordY)
        self.coordX = coordX
        self.coordY= coordY
        self.interval = 250
        self.temps = Draw.getTime()
        self.img = self.imgNClicked
        self.clicked = False
        self.substracX = 41
        self.substracy = 45
    
    #Affichage de la bar
    def afficheBar(self, screen):
        if self.temps + self.interval <= Draw.getTime():
            if self.clicked :
                self.clicked = False
                self.img = self.imgNClicked
                self.coords = (self.coordX, self.coordY)
            else:
                self.clicked = True
                self.img = self.imgClicked
                self.coords = (self.coordX - self.substracX /2 , self.coordY - self.substracy/2)
            self.temps = Draw.getTime()
        Draw.drawBlit(screen, self)
