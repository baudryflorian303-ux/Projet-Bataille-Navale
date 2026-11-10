from bateau import Bateau
from grille import Grille


def test_init():
	bateau = Bateau(2, 3)

	assert bateau.ligne == 2
	assert bateau.colonne == 3
	assert bateau.longueur == 1
	assert bateau.vertical == False

def test_position():
	assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
	assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]


def test_coule():
	bateau = Bateau(0, 0, longueur=2)
	grille = Grille(1, 2)
	grille.tirer(0, 0)
	grille.tirer(0, 1)

	assert bateau.coulé(grille) == True