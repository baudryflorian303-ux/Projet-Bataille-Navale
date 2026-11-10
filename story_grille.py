from grille import Grille

# Nom : "Plouf dans l'eau"
# Utilisateur : un joueur
# Story : On veut pouvoir gérer les tirs de l'adversaire
# Actions :
# - créer une grille à 5 lignes et 8 colonnes
# - afficher la grille à l'écran
# - demande à l'utilisateur de rentrer deux coordonnées x et y
# - tirer à l'endroit indiqué sur la grille
# - retour en 2

grille = Grille(5, 8)

print(grille)

while "~" in grille.matrice:
    x = int(input("Coordonnée x : "))
    y = int(input("Coordonnée y : "))

    assert 0 < x and x <= 5 and 0 < y and y <= 8

    grille.tirer(x-1,y-1)

    print(grille)

print("Partie terminée")