# -*- coding: utf-8 -*-

"""chaud froid.py

Consignes :
  Petit jeu 2 joueur, le but du jeu est de trouver le nombre de notre adversaire en un minimum de coups.

  - Le joueur 1 entre un nombre compris entre 0 et 100
  - Le programme demande le nombre mystère au joueur 2 tant que celui-ci n'a pas entré la bonne valeur.

  On appelle **diff** la valeur absolue de la différence entre le nombre mystère et la proposition du joueur 2

  - Si diff est supérieur à 20, le programme affichera **glacé**
  - Si diff est supérieur à 10 et inférieur à 20, le programme affichera **froid**
  - Si diff est supérieur à 5 et inférieur à 10, le programme affichera **chaud**
  - Si diff est inférieur à 5 et supérieur à 0, le programme affichera **bouillant**
  - Si diff est égal à zéro c'est que nous avons trouvé le nombre mystère, le programme affichera **Gagné en X coups** et s’arrêtera.

Usage :
  python chaud_froid.py

Code :
"""

mystere = input("Entrez le nombre mystère : ")
mystere = int(mystere)

if mystere < 0 or mystere > 100:
  print("Le nombre doit être compris entre 0 et 100")
  quit(-1)  # On force le programme à quitter en indiquant une erreur, -1 est souvent associé à une erreur quand 0 est associé à "tout va bien"

compteur = 0
proposition = -1 # On fixe délibérement une proposition qui ne peut pas fonctionner
while proposition != mystere:
    proposition = int(input("Entrez un nombre : "))

    diff = abs(mystere - proposition)

    if diff > 20:
        print("Glacé")
    elif diff > 10:
        print("Froid")
    elif diff > 5:
        print("Chaud")
    elif diff > 0:
        print("Bouillant")
    else:
        print("Trouvé")

    compteur += 1

print("Gagné en " + str(compteur) + " coups")
