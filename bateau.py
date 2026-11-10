class Bateau:

    def __init__(self, ligne, colonne, longueur = 1, vertical = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        liste_pos = []
        l = self.ligne
        c = self.colonne
        liste_pos.append((l, c))
        if self.vertical:
            for i in range(1, self.longueur):
                l += 1
                liste_pos.append((l, c))
        else:
            for j in range(1, self.longueur):
                c += 1
                liste_pos.append((l, c))

        return liste_pos

    def coulé(self, grille):

        compteur_touche = 0
        for ligne, colonne in self.positions():
            if grille.matrice[ligne * grille.nb_colonnes + colonne] == grille.touche:
                compteur_touche += 1

        if compteur_touche == self.longueur:

            return True

        else:

            return False


class porte_avion(Bateau):

    def __init__(self, ligne, colonne, longueur=4, vertical=False):
        super().__init__(ligne, colonne, longueur, vertical)

class croiseur(Bateau):

    def __init__(self, ligne, colonne, longueur=3, vertical=False):
        super().__init__(ligne, colonne, longueur, vertical)

class torpilleur(Bateau):

    def __init__(self, ligne, colonne, longueur=2, vertical=False):
        super().__init__(ligne, colonne, longueur, vertical)

class sous_marin(Bateau):

    def __init__(self, ligne, colonne, longueur=2, vertical=False):
        super().__init__(ligne, colonne, longueur, vertical)