#Module utilitaire regroupant diverses fonctions

import random

#Retourne une liste de liste contenant la map de départ
def loadCSV():
    path = "Assets/map.csv"

    t = []

    f = open(path, "r")

    while True:
        line = f.readline()

        if len(line) > 0:
            n = []
            for e in line:
                if e != ";" and e != "\n":
                    n.append(e)
            t.append(n)
        else:
            break
    f.close()
    return t

#recherche un "1" dans la colonne, si pas présent on renvoi -1, sinon l'indice 
# map : la map à modifier
# numCol : numéro de la colonne à vérifier
def searchObstacleInLine(numCol, map):
    j = 0
    while j < len(map):
        if map[j][numCol] == "1":
            return j
        j+=1

    return -1

#Recherche un 0 dans une colonne
# map : la map à modifier
# numCol : numéro de la colonne à vérifier
def searchFirst0InLine(numCol, map):
    i = 0
    while i < len(map):
        if map[i][numCol] == "0":
            return i
        i+=1
    print("Error, no 0 found searcgFirst0InLine")
    return -1

#supprime la première colonne et insère des 0 à la fin
# map : la map à modifier
def new0Colonne(map):
    i = 0

    while i < len(map):
        del map[i][0]
        map[i].append("0")
        i+=1
    return map

#copie la dernière ligne car elle n'est présente qu'en un exemplaire
# map : la map à modifier
def copieDerniereColonne(map):
    i = 0

    while i < len(map):
        del map[i][0]
        map[i].append(map[i][len(map[i])-1])
        i+=1
    return map

#créé un nouvel obstacle en fonction du précédent, un peu plus haut, un peu plus bas en fonction
# map : la map à modifier
# colonne : le numéro de la colonne à modifier
# blankSpaceLine : le nombre de blanc entre deux obstacles 
def createNewObstacle(map, colonne, blankSpaceLine):
    random.seed()
    if colonne > 1 and colonne < len(map[0]) -3:
        colonne += random.randint(-2, 1)
    elif colonne > 0:
        colonne += random.randint(-2, 0)
    else:
        colonne += random.randint(0, 2)

    i = 0

    while i < len(map):
        del map[i][0]
        if i < colonne:
            map[i].append("1")
        elif i <= (colonne + blankSpaceLine) -1:
            map[i].append("0")
        else:
            map[i].append("1")
        i+=1
    return map

#Prépare un nouvel obstacle par rapport à l'emplacement du précédent
# map : la map à modifier
def createNextObstacle(map):
    i = len(map[0]) - 1
    blankSpace = 2
    blankSpaceLine = 3

    while searchObstacleInLine(i, map) == -1:
        i = i - 1
    indice = searchFirst0InLine(i, map)

    if i == len(map[0]) -1 and searchObstacleInLine(i-1, map) != -1:
        return new0Colonne(map)                               # Nouvelle colonne vide
    elif i == len(map[0]) -1:
        return copieDerniereColonne(map)                      # Rajoute une colonne identique à la précédente
    elif i == (len(map[0]) -1) -(blankSpace -1):
        return new0Colonne(map)                               # Nouvelle colonne vide
    else:
        return createNewObstacle(map, indice, blankSpaceLine) # Création nouvel obstacle

#Compare le score avec le score précédent. Sauvegarde le meilleur des deux
def saveScore(score):
    try:
        f = open("Assets/score.txt", "r")

        pred = int(f.readline())

        f.close()
    except:
        f = open("Assets/score.txt", "w")
        pred = 0
        f.close()

    f = open("Assets/score.txt", "w")

    if pred < score:
        f.write(str(score))
    else:
        f.write(str(pred))
    f.close

#Charge le meilleur score
def loadScore():
    try:
        f = open("Assets/score.txt", "r")
        tmp = f.readline()
        f.close()
        return int(tmp)
    except:
        return 0
