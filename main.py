import random

from grille import Grille
from bateau import porte_avion, torpilleur, croiseur, sous_marin

grille_jeu = Grille(8, 10)


liste_bateaux =  [porte_avion(0, 0), croiseur(5,0,vertical=True), torpilleur(3,1), sous_marin(5,3)]


def positions_possibles(bateau, grille):
    nb_lignes = len(grille.matrice) // grille.nb_colonnes
    positions_disponibles = []
    ligne_initiale = bateau.ligne
    colonne_initiale = bateau.colonne
    vertical_initial = bateau.vertical

    for orientation in (False, True):
        for ligne in range(nb_lignes):
            for colonne in range(grille.nb_colonnes):

                bateau.ligne, bateau.colonne, bateau.vertical = ligne, colonne, orientation
                cases = bateau.positions()

                bateau.ligne = ligne_initiale
                bateau.colonne = colonne_initiale
                bateau.vertical = vertical_initial

                placement_valide = True
                for ligne_case, colonne_case in cases:
                    if not (0 <= ligne_case < nb_lignes and 0 <= colonne_case < grille.nb_colonnes
                        and grille.matrice[ligne_case * grille.nb_colonnes + colonne_case] == grille.vide):
                        placement_valide = False
                        break

                if placement_valide:
                    positions_disponibles.append((ligne, colonne, orientation))

    return positions_disponibles


def ajout_aléatoire(bateau, grille):
    positions = positions_possibles(bateau, grille)
    if not positions:
        print("Aucun placement disponible")
        return False

    bateau.ligne, bateau.colonne, bateau.vertical = random.choice(positions)
    grille.ajoute(bateau)
    return True

for bateau in liste_bateaux:
    if not ajout_aléatoire(bateau, grille_jeu):
        print(f"Aucun placement possible pour le bateau {bateau}")

grille_visible = Grille(8, 10)
bateaux_restants = list(liste_bateaux)
nb_tirs = 0


while bateaux_restants:
    # print(grille_jeu)
    # print("_______________")

    print(grille_visible)
    print("\n🤠 Veuillez renseigner les coordonnées du tir")
    
    try:
        ligne = int(input("Numéro de ligne : "))
        colonne = int(input("Numéro de colonne : "))
        assert 0 < ligne <= 8 and 0 < colonne <= 10

    except AssertionError:
        print("​​\n​​⚠️​ La grille est de taille 8x10 ! Réessayez")
        continue
    except ValueError:
        print("​​\n​​⚠️​ Veuillez entrer un nombre !")
        continue

    ligne -= 1
    colonne -= 1

    if grille_visible.matrice[ligne * grille_visible.nb_colonnes + colonne] != grille_visible.vide:
        print("🫤​ Vous avez déjà tiré ici !")
        continue

    nb_tirs += 1

    bateau_touche = False
    for bateau in bateaux_restants:
        if (ligne, colonne) in bateau.positions():
            bateau_touche = bateau

    print("_______________\n")
    
    if bateau_touche is False:
        grille_visible.tirer(ligne, colonne)
        print("​💦​ Tir dans l'eau")
    else:
        grille_jeu.tirer(ligne, colonne, "💣")
        grille_visible.tirer(ligne, colonne, "💣")

        if bateau_touche.coulé(grille_jeu):
            grille_visible.ajoute(bateau_touche)
            bateaux_restants.remove(bateau_touche)

            if isinstance(bateau_touche, porte_avion):
                print("​🔥​ Le porte-avions ne porte plus d'avions !")
            elif isinstance(bateau_touche, croiseur):
                print("​🔥​ Le croiseur est coulé !")
            elif isinstance(bateau_touche, torpilleur):
                print("​🔥​ Le torpilleur torpillé !")
            elif isinstance(bateau_touche, sous_marin):
                print("​🔥​ Le sous-marin repose au fond de l'océan !")
        else:
            print("💥 Touché ! 💥")

print(grille_visible)
print(f"Bravo, tous les bateaux sont coulés en {nb_tirs} coups !")