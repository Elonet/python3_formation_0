# -*- coding: utf-8 -*-

"""exercice2.py

Consignes :
  Réaliser une calculatrice avec les opérateurs `+`, `-`, `*`, `/`

  1. Le programme demande à l’utilisateur l’opération à réaliser via un menu
  2. Le programme demande 2 nombres à l’utilisateur
  3. Le programme fait le calcul et retourne le résultat

Usage :
  python exercice2.py

Code :
"""

print("== Exercice 2 ==\nMenu :")
print("\t1 - Addition\n\t2 - Soustraction\n\t3 - Division\n\t4 - Multiplication\n\t9 - Quitter")

possible = [1, 2, 3, 4, 9]
choix = int(input("Votre choix : "))

if choix not in possible:
    print("Mauvais choix")
    quit(-1)

total = 0
if choix == 1:
    print("\n== Addition ==")
    nb1 = float(input("Entrez le nombre 1 : "))
    nb2 = float(input("Entrez le nombre 2 : "))
    total = nb1 + nb2
    print("\n" + str(nb1) + " + " + str(nb2) + " = " + str(total))

elif choix == 2:
    print("\n== Soustraction ==")
    nb1 = float(input("Entrez le nombre 1 : "))
    nb2 = float(input("Entrez le nombre 2 : "))
    total = nb1 - nb2
    print("\n" + str(nb1) + " - " + str(nb2) + " = " + str(total))

elif choix == 3:
    print("\n== Division ==")
    nb1 = float(input("Entrez le nombre 1 : "))
    nb2 = float(input("Entrez le nombre 2 : "))

    if nb2 == 0:
        print("<!> Division par zéro impossible")
        quit(-1)

    total = nb1 / nb2
    print("\n" + str(nb1) + " / " + str(nb2) + " = " + str(total))

elif choix == 4:
    print("\n== Multiplication ==")
    nb1 = float(input("Entrez le nombre 1 : "))
    nb2 = float(input("Entrez le nombre 2 : "))

    total = nb1 * nb2
    print("\n" + str(nb1) + " * " + str(nb2) + " = " + str(total))

else:
    print("Vous avez choisi de quitter")