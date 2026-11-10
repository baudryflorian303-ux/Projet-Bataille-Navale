from bateau import porte_avion, croiseur, torpilleur, sous_marin

class Grille:
    
    vide = "~"
    touche = "x"

    def __init__(self, nb_lignes, nb_colonnes):
        
        self.matrice = [self.vide] * (nb_lignes * nb_colonnes)
        self.nb_colonnes = nb_colonnes

    def tirer(self, ligne, colonne, touche = "x"):
        self.touche = touche
        self.matrice[ligne * self.nb_colonnes + colonne] = touche

    def __str__(self):
        grille_affichage = []
        for i in range(0, len(self.matrice), self.nb_colonnes):
            ligne = self.matrice[i:i + self.nb_colonnes]
            ligne_affichage = []
            for j in ligne:
                if j == self.vide:
                    ligne_affichage.append(".")
                else:
                    ligne_affichage.append(j)
            grille_affichage.append("".join(ligne_affichage))
                    
        return "\n".join(grille_affichage)

    def ajoute(self, bateau):
        pos_bateau = bateau.positions()
        nb_lignes = len(self.matrice) // self.nb_colonnes

        if isinstance(bateau, porte_avion):
            icone = "🚢"
        elif isinstance(bateau, croiseur):
            icone = "⛴"
        elif isinstance(bateau, torpilleur):
            icone = "🚣"
        elif isinstance(bateau, sous_marin):
            icone = "🐟"
        
        for ligne, colonne in pos_bateau:
            if ligne < 0 or ligne >= nb_lignes or colonne < 0 or colonne >= self.nb_colonnes:
                print("Le bateau sort de la grille !")
                return
            
        for ligne, colonne in pos_bateau:
            self.matrice[ligne * self.nb_colonnes + colonne] = icone