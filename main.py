# decouverte_python.py

def pause():
    input("\nAppuyez sur Entrée pour continuer...")

def introduction():
    print("\n=== Bienvenue dans la découverte de Python ===")
    print("Ce programme vous permet d'apprendre Python en interagissant.")
    pause()

def lecon_variables():
    print("\n=== LES VARIABLES ===")
    nom = input("Quel est votre prénom ? ")

    print(f"Bonjour {nom} !")

    age = int(input("Quel âge as-tu ? "))
    print(f"Dans un an tu auras {age + 1} ans.")

    pause()

def lecon_calcul():
    print("\n=== LES CALCULS ===")

    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))

    print(f"Addition : {a + b}")
    print(f"Soustraction : {a - b}")
    print(f"Multiplication : {a * b}")

    if b != 0:
        print(f"Division : {a / b}")
    else:
        print("Impossible de diviser par zéro.")

    pause()

def lecon_conditions():
    print("\n=== LES CONDITIONS ===")

    note = int(input("Entre une note sur 20 : "))

    if note >= 16:
        print("Très bien !")
    elif note >= 10:
        print("Admis.")
    else:
        print("À améliorer.")

    pause()

def lecon_boucles():
    print("\n=== LES BOUCLES ===")

    nombre = int(input("Choisis un nombre : "))

    print("\nTable de multiplication :")
    for i in range(1, 11):
        print(f"{nombre} x {i} = {nombre * i}")

    pause()

def quiz():
    print("\n=== QUIZ ===")

    score = 0

    reponse = input("Quelle fonction affiche du texte ? ").lower()

    if reponse == "print":
        score += 1

    reponse = input("Quel symbole permet l'addition ? ")

    if reponse == "+":
        score += 1

    reponse = input("Une boucle qui compte de 0 à 9 utilise : ").lower()

    if "range" in reponse:
        score += 1

    print(f"\nScore : {score}/3")

    if score == 3:
        print("Excellent !")
    elif score >= 2:
        print("Bon travail !")
    else:
        print("Continue à apprendre !")

    pause()

def menu():
    while True:
        print("\n")
        print("========== MENU ==========")
        print("1 - Variables")
        print("2 - Calculs")
        print("3 - Conditions")
        print("4 - Boucles")
        print("5 - Quiz")
        print("0 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            lecon_variables()

        elif choix == "2":
            lecon_calcul()

        elif choix == "3":
            lecon_conditions()

        elif choix == "4":
            lecon_boucles()

        elif choix == "5":
            quiz()

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

introduction()
menu()
