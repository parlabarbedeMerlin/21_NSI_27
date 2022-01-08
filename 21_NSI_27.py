
from turtle import *
from math import sqrt
from random import randint
from time import sleep

#Exercice 1 => 00:00

def moyenne(L:list)->float: #on définie la fonction et lui indique le paramètre L ainsi que son type. On indique aussi le type retourné
    """
    renvoie la moyenne d'une liste d'entier
    :param L: liste d'entiers
    :return: float
    """
    total = 0 #on intialise le total
    for i in L: #on parcours tous les éléments de la liste en passant à chaque fois au suivant
        assert not(i is int), "La liste contient un élément qui n'est pas en entier" # vérifie si la liste contient un élément diférent d'un entier
        total = total+i #on ajoute au total l'élément parcourut au moment précis ou l'instruction est exécuté
    return total/len(L) #on renvoie la moyenne

print(moyenne([10,20,30,40,60,110])) #test de la fonction moyenne()


#Exercice 2 => 02:30

#définition du motif
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    '''affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par deux espaces "  "
    :param dessin: liste de liste de caractères
    :return: None (affiche dans la console)
    '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *",end="")
            else:
                print("  ",end="")
        print()


def zoomListe(liste_depart,k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart
    :param liste_depart: liste de caractères
    :param k: entier
    :return: renvoie la liste zoomé par k
    '''
    liste_zoom = [] #la list est vide au départ
    for elt in  liste_depart: #on parcours chaque motif (vide ou remplie de la liste)
        for i in range(k):
            liste_zoom.append(elt) #on l'ajoute fois k
    return liste_zoom #on renvoie la ligne zoomé par k

# 07:30

def zoomDessin(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois
    :param grille: liste de list de caractère
    :param k: entier
    :return: grille zoomé par k
    '''
    grille_zoom=[] #grille zoomé définie comme liste vide
    for elt in grille: #on parcours chaque ligne de la list
        liste_zoom = zoomListe(elt,k) #on stock dans une variable la ligne zoomé par k
        for i in range(k):
            grille_zoom.append(liste_zoom) #on ajoute fois k la liste zoomé
    return grille_zoom #on renvoie la grille (tableau) zoomé

# 10:12

affiche(coeur)

affiche(zoomDessin(coeur,3))

#le code à été fini en 12 minutes et 26 secondes

# le code a été commenté en 29 minutes et 46 secondes


# Bonus

def afficher_couleur(dessin,color = "WHITE"):
    """
    affiche le dessin dans la couleur spécifié
    :param dessin:
    :param couleur:
    :return: None (affiche un dessin dans la console)
    """
    if color == "RED":
        print("\u001b[1;31m")
    elif color == "GREEN":
        print("\u001b[1;32m")
    elif color == "YELLOW":
        print("\u001b[1;33m")
    elif color == "BLUE":
        print("\u001b[1;34m")
    elif color == "MAGENTA":
        print("\u001b[1;35m")
    elif color == "CYAN":
        print("\u001b[1;36m")
    elif color == "WHITE":
        print("\u001b[1;37m")
    else:
        print("\u001b[1;37m")        

    affiche(dessin)

    # on remet la couleur par défaut
    print("\u001b[0m")


def showonwin(dessin):
    """
    créé une fenètre et affiche le motif dans une grille
    """

    # on crée la fenêtre
    setup(width=1.5*sqrt(len(dessin))*100, height=1.5*sqrt(len(dessin))*100)
    title("Motif")
    hideturtle()
    speed(0)
    penup()
    goto(-1.5*sqrt(len(dessin))*100/2, -1.5*sqrt(len(dessin))*100/2)
    pendown()

    # on affiche le motif
    for ligne in dessin:
        for elt in ligne:
            if elt == 1:
                color(randint(0, 255), randint(0, 255), randint(0, 255))
                begin_fill()
                forward(100)
                left(90)
                forward(100)
                left(90)
                forward(100)
                left(90)
                forward(100)
                end_fill()
            else:
                forward(100)
        penup()
        goto(0, 0)
        pendown()
        forward(100)
        penup()
        goto(0, 0)
        pendown()

    # on attend que l'utilisateur ferme la fenêtre
    done()

showonwin(coeur)

