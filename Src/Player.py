#Module du joueur

import exampleClass
import Draw

#Classe permettant de gérer le joueur
class joueur(exampleClass.example):

    def __init__(self, coordX, coordY):
        self.color = (0,0,0)
        self.img = Draw.createRect(coordX, coordY, 32, 32)