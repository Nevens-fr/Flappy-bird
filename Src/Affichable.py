import Draw

#Classe abstraite qui permet de définir des comportemens par défaut 
#à toutes les classes en héritant
class affichable:
    #constructeur
    #coords : tuple des coordonnées ou placer l'élément à l'écran
    #path : chemin relatif vers l'image à afficher
    def __init__(self, coords, path):
        self.img = Draw.createImg(path)
        self.coords = coords
    def getImg(self):
        return self.img
    def getCoords(self):
        return self.coords