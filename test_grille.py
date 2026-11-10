from grille import Grille
from bateau import Bateau, porte_avion, torpilleur, croiseur, sous_marin

def test_init():
    grille = Grille(3, 4)
    
    assert isinstance(grille, Grille)
    assert Grille(3,4).nb_colonnes == 4

def test_tirer():
    grille = Grille(3, 4)
    grille.tirer(1, 2)

    assert grille.matrice[1 * grille.nb_colonnes + 2] == "x"

def test_str():
    grille = Grille(3, 4)
    grille.tirer(1, 2)

    assert str(grille) == "....\n..x.\n...."

def test_ajoute():
    grille = Grille(2, 3)
    grille.ajoute(torpilleur(1, 0))

    assert grille.matrice == ["~", "~", "~", "🚣", "🚣", "~"]

    grille = Grille(2, 3)
    grille.ajoute(porte_avion(1, 0, vertical=True))

    assert grille.matrice == ["~", "~", "~", "~", "~", "~"]

    grille.ajoute(croiseur(1, 0, vertical=True))

    assert grille.matrice == ["~", "~", "~", "~", "~", "~"]


def test_ajoute_type():
    grille = Grille(4, 4)
    grille.ajoute(porte_avion(0, 0))
    grille.ajoute(croiseur(1, 0))
    grille.ajoute(torpilleur(2, 0))
    grille.ajoute(sous_marin(3, 0))

    assert grille.matrice == ["🚢", "🚢", "🚢", "🚢","⛴", "⛴", "⛴", "~",
                              "🚣", "🚣", "~", "~", "🐟", "🐟", "~", "~",]