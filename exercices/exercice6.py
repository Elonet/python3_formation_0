# -*- coding: utf-8 -*-

"""exercice6.py

Consignes :
  Demander à l'utilisateur une largeur et une longueur pour afficher un pavé d'étoiles à l'aide d'une boucle dans une boucle

Usage :
  python exercice6.py

Code :
"""

print("== Exercice 6 ==")
largeur = int(input("Entrez une largeur : "))
longueur = int(input("Entrez une longueur : "))

if largeur < 0:
    print("La largeur doit être positive")
    quit(-1)

if longueur < 0:
    print("La longueur doit être positive")
    quit(-1)


cpt_largeur = 0
while cpt_largeur < largeur:
    cpt_longueur = 0
    while cpt_longueur < longueur:
        print("*", end="")
        cpt_longueur += 1
    print()
    cpt_largeur += 1
