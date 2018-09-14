# -*- coding: utf-8 -*-

"""exercice4.py

Consignes :
  Demander une année à l'utilisateur et calculer les 10 prochaines années bissextiles à partir de cette date à l'aide d'une **boucle**.

Usage :
  python exercice4.py

Code :
"""

print("== Exercice 4 ==")
annee = int(input("Entrez une année : "))

trouver = 0
while trouver < 10:
    if ((annee % 4 == 0) and (annee % 100 != 0)) or annee % 400 == 0:
        print(annee)
        trouver += 1

    annee += 1
