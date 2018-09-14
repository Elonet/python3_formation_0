# -*- coding: utf-8 -*-

"""exercice7.py

Consignes :
  Réaliser un petit jeu de question réponse.

  1. Le programme pioche une question
  2. Le programme affiche les choix possibles et attend la réponse de l'utilisateur
  3. Le programme indique si l'utilisateur à bien répondu

Usage :
  python exercice7.py

Code :
"""

from random import randint

questions = [
    {
        "question": "Votre question",
        "reponses": [
            "Reponse A",
            "Reponse B",
            "Reponse C"
        ],
        "correct": "Reponse A"
    },
{
        "question": "Votre question",
        "reponses": [
            "Reponse A",
            "Reponse B",
            "Reponse C"
        ],
        "correct": "Reponse B"
    }
]

print("== Exercice 7 ==")

hasard = randint(0, len(questions) - 1)
question = questions[hasard]

print("Question #" + str(hasard + 1) + " " + question["question"])

compteur = 0
while compteur < len(question["reponses"]):
    print(str(compteur) + " : " + question["reponses"][compteur])
    compteur += 1

choix = int(input("Votre choix : "))

if choix < 0 or choix >= len(question["reponses"]):
    print("Mauvais choix")
    quit(-1)

if question["reponses"][choix] != question["correct"]:
    print("Mauvaise réponse, dommage")
else:
    print("Bonne réponse !")