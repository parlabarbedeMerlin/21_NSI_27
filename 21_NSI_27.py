from tkinter import Tk, Canvas, Frame, BOTH  # import de tkinter pour le bonus


# Exercice 1 => 00:00

# On définit la fonction et lui indique le paramètre L ainsi que son type. On indique aussi le type retourné
def moyenne(liste: list) -> float:
    """
    Renvoie la moyenne d'une liste d'entier
    :param liste: liste d'entiers
    :return: float
    """
    total = 0  # on intialise le total
    for i in liste:  # on parcours tous les éléments de la liste en passant à chaque fois au suivant

        # vérifie si la liste contient un élément diférent d'un entier
        assert not (i is int), "La liste contient un élément qui n'est pas en entier"

        # on ajoute au total l'élément parcourut au moment précis ou l'instruction est exécuté
        total = total + i

    return total / len(liste)  # on renvoie la moyenne


print(moyenne([10, 20, 30, 40, 60, 110]))  # test de la fonction moyenne()

# Exercice 1 fini en 1:45

# Exercice 2 => 02:30

# définition du motif
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    """affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par deux espaces "  "
    :param dessin: liste de liste de caractères
    :return: None (affiche dans la console)
    """
    for ligne in dessin: # on parcours chaques lignes du dessin
        for col in ligne: #on parcours chaque élément de la ligne
            if col == 1: #on regarde si quel est le caractère a afficher
                print(" *", end="")  # on affiche un "*" avec un espace après pour ne pas avoir le dessin étiré
            else:
                print("  ", end="") # sinon on affiche deux espaces pour ne pas déformer le dessin
        print()


def zoomliste(liste_depart, k):
    """renvoie une liste contenant k fois chaque
       élément de liste_depart
    :param liste_depart: liste de caractères
    :param k: entier
    :return: renvoie la liste zoomé par k
    """
    liste_zoom = []  # la list est vide au départ
    for elt in liste_depart:  # on parcours chaque motif (vide ou remplie de la liste)
        for i in range(k): #on executes l'instruction imbriqué k fois
            liste_zoom.append(elt)  # on on ajoute element
    return liste_zoom  # on renvoie la ligne zoomé par k


# au bout de 07:30

def zoomdessin(grille, k):
    """renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois
    :param grille: liste de list de caractère
    :param k: entier
    :return: grille zoomé par k
    """
    grille_zoom = []  # grille zoomé définie comme liste vide
    for elt in grille:  # on parcours chaque ligne de la list
        liste_zoom = zoomliste(elt, k)  # on stock dans une variable la ligne zoomé par k
        for i in range(k): # on répète k fois les instructions
            grille_zoom.append(liste_zoom)  # on ajoute la liste zoomé
    return grille_zoom  # on renvoie la grille (tableau) zoomé


# Au bout de 10:12

affiche(coeur) # test de la fonction affiche()

affiche(zoomdessin(coeur, 3)) # test de la fonction zoomdessin()


# le code à été fini au bout de 12 minutes et 26 secondes

# le code a été fini d'être commenté au bout de 29 minutes et 46 secondes


# Bonus (NECESSITE TKINTER)

def afficher_couleur(dessin, color="WHITE"):
    """
    affiche le dessin dans la couleur spécifié
    :param dessin:
    :param color:
    :return: None (affiche un dessin dans la console)
    """
    if color == "RED": # si la couleur est rouge
        print("\u001b[1;31m") # on met la couleur rouge
    elif color == "GREEN": # si la couleur est verte
        print("\u001b[1;32m") # on met la couleur verte
    elif color == "YELLOW": # si la couleur est jaune
        print("\u001b[1;33m") # on met la couleur jaune
    elif color == "BLUE": # si la couleur est bleue
        print("\u001b[1;34m") # on met la couleur bleue
    elif color == "MAGENTA": # si la couleur est magenta
        print("\u001b[1;35m") # on met la couleur magenta
    elif color == "CYAN": # si la couleur est cyan
        print("\u001b[1;36m") # on met la couleur cyan
    elif color == "WHITE": # si la couleur est blanche
        print("\u001b[1;37m") # on met la couleur blanche
    else: # sinon on met la couleur par défaut
        print("\u001b[1;37m") # on met la couleur blanche

    affiche(dessin)

    #après avoir fini d'afficher le dessin, on remet la couleur par défaut
    print("\u001b[0m")# on remet la couleur par défaut


# Bonus (NECESSITE TKINTER)
root = Tk() # on crée une fenêtre
root.title("Dessin") # on donne un titre à la fenêtre
root.geometry("800x800") # on donne une taille à la fenêtre


def showonwin(dessin, win): # on crée une fonction qui affiche un dessin dans une fenêtre
    """
    print the motif of dessin on grid on window using tkinter
    :param win: window
    :param dessin: list of list of int
    :return: None
    """

    # create a canvas
    canvas = Canvas(win, width=800, height=800) # on crée un canvas de 800x800 pixels
    canvas.pack(fill=BOTH, expand=1) # on met le canvas dans la fenêtre

    # create a frame
    frame = Frame(win) # on crée un cadre
    frame.pack() # on met le cadre dans la fenêtre

    # create a grid
    for i in range(len(dessin)): # on parcours chaque indices des lignes du dessin
        for j in range(len(dessin[i])): # puis chaques caractères
            if dessin[i][j] == 1: # si le caractère est un 1
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="black") # on crée un rectangle noir
            else: # sinon
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white", outline="black") # on crée un rectangle blanc
    win.mainloop() # on affiche la fenêtre


showonwin(coeur, root) # on affiche le dessin coeur dans la fenêtre


# le bonus a été fini au bout de 1h 2 minutes et 23 secondes
