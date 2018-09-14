# -*- coding: utf-8 -*-

"""exercice5.py

Consignes :
  Demander à l'utilisateur un nombre d'étoiles à afficher et les afficher sur une seule ligne à l'aide d'une **boucle**

Usage :
  python exercice5.py

Code :
"""

print("== Exercice 5 ==")
nb = int(input("Entrez une entier positif : "))

if nb < 0:
    print("Le nombre n'est pas un entier positif")
    quit(-1)

compteur = 0

while compteur < nb:
    print("*", end="")
    compteur += 1
