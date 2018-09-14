# -*- coding: utf-8 -*-

"""exercice3.py

Consignes :
  Demander une année à un utilisateur et lui indiquer si l'année est bissextile ou non.

  Une année est bissextile si :
    1. Elle est divisible par 4 **et** non divisible par 100, **ou**
    2. Si elle est divisible par 400

Usage :
  python exercice3.py

Code :
"""

print("== Exercice 3 ==")
annee = int(input("Entrez une année : "))

if ((annee % 4 == 0) and (annee % 100 != 0)) or annee % 400 == 0:
    print("Année bissextile")
else:
    print("Année normale")
