import exampleClass
import Draw
import Affichable


#Classe qui permet de display les points du joueur
class Points(exampleClass.example):

    #Constructeur
    def __init__(self, coordX, coordY):
        self.pts = 0
        self.color = (255,255,255)
        self.coords = (coordX,coordY)
        self.font = Draw.creerFont()
        self.lim = 20
        self.mult = 1
        self.fond = Affichable.affichable((0,0), "Assets/fond.png")
        self.img = Draw.rendertexte(self.font, str(self.pts), False, self.color)
    
    # Change les points
    def setPts(self, pts):
        self.pts = pts
        self.img = Draw.rendertexte(self.font, str(self.pts), False, self.color)
    
    # Autorise le jeu a accelerer le défilement selon les points acquis
    def speedUp(self):
        if self.pts >= self.lim * self.mult:
            self.mult += 1
            return True
        return False

    #Getter des points
    def getPts(self):
        return self.pts

    #Affichage des points
    def afficherPoints(self, screen):
        self.img = Draw.rendertexte(self.font, str(self.pts), False, self.color)
        Draw.drawBlit(screen, self.fond)
        Draw.drawBlit(screen, self)

    #Ajoute un point
    def addPoints(self):
        self.pts += 1
