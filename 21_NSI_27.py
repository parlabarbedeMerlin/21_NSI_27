from tkinter import Tk, Canvas, Frame, BOTH


# Exercice 1 => 00:00

# on définie la fonction et lui indique le paramètre L ainsi que son type. On indique aussi le type retourné
def moyenne(liste: list) -> float:
    """
    renvoie la moyenne d'une liste d'entier
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
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
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
        for i in range(k):
            liste_zoom.append(elt)  # on l'ajoute fois k
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
        for i in range(k):
            grille_zoom.append(liste_zoom)  # on ajoute fois k la liste zoomé
    return grille_zoom  # on renvoie la grille (tableau) zoomé


# Au bout de 10:12

affiche(coeur)

affiche(zoomdessin(coeur, 3))


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


# create a window
root = Tk()
root.title("Dessin")
root.geometry("800x800")


def showonwin(dessin, root):
    """
    print the motif of dessin on grid on window using tkinter
    :param dessin: list of list of int
    :return: None
    """

    # create a canvas
    canvas = Canvas(root, width=800, height=800)
    canvas.pack(fill=BOTH, expand=1)

    # create a frame
    frame = Frame(root)
    frame.pack()

    # create a grid
    for i in range(len(dessin)):
        for j in range(len(dessin[i])):
            if dessin[i][j] == 1:
                # create a rectangle
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="black")
            else:
                # create a rectangle
                canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="white", outline="black")

    # show window
    root.mainloop()


showonwin(zoomdessin(coeur, 3), root)


# le bonus a été fini au bout de 1h 2 minutes et 23 secondes

# closewin func
def closewin(win):
    """
    close the window
    :return: None
    """
    win.destroy()
    win.quit()


