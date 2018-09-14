# -*- coding: utf-8 -*-

"""exercice1.py

Consignes :
  Demander à un utilisateur son prénom et sa date de naissance afin de lui dire "Bonjour `nom` vous avez `age` ans"

Usage :
  python exercice1.py

Code :
"""
from datetime import datetime

print("== Exercice 1 ==")

prenom = input("Entrez votre prénom : ")
annee_naissance = int(input("Entrez votre année de naissance : "))
annee = datetime.now().year
diff = annee - annee_naissance

print("Bonjour " + prenom + " vous avez " + str(diff) + " ans")
