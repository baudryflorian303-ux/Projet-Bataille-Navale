from bateau import Bateau

# Nom : "chevauchement"
# Utilisateur : un joueur
# Story : Positionner des bateaux sans chevauchement
# Actions :
# - créer un bateau b1
# - créer un bateau b2
# - vérifier si les deux bateaux se chevauchent


# Bateaux qui se chevauchent

b1_a = Bateau(1, 2, 2)
b1_b = Bateau(0, 2, 3, True)

chevauche_1 = any(element in b1_a.positions() for element in b1_b.positions())

if chevauche_1:
    print("Les bateaux se chevauchent !")
if not chevauche_1:
    print("Les bateaux se chevauchent pas.")


# Bateaux qui ne se chevauchent pas

b2_a = Bateau(1, 2, 2)
b2_b = Bateau(0, 0)

chevauche_2 = any(element in b2_a.positions() for element in b2_b.positions())

if chevauche_2:
    print("Les bateaux se chevauchent !")
if not chevauche_2:
    print("Les bateaux se chevauchent pas.")