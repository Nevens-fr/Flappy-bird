import exampleClass
import Draw


#Classe qui permet de display les points du joueur
class Points(exampleClass.example):

    #Constructeur
    def __init__(self, coordX, coordY):
        self.pts = 0
        self.img = None
        self.color = (0,0,0)
        self.coords = (coordX,coordY)
        self.font = Draw.creerFont()

    #Getter des points
    def getPts(self):
        return self.pts

    #Affichage des points
    def afficherPoints(self, screen):
        self.img = Draw.rendertexte(self.font, str(self.pts), False, self.color)
        Draw.drawBlit(screen, self)

    #Ajoute un point
    def addPoints(self):
        self.pts += 1
