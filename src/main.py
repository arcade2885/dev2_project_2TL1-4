

def main():
    pass


if __name__ == "__main__":
    main()


q1="Quel est la capitale du Congo ?"
q2="Quel est la capitale de Chine ?"
q3="Quel est la capitale de la Colombie ?"

listeQuestion=[q1,q2,q3]

r1="Brazzaville"
r2="Pékin"
r3="Bogota"

listeReponse=[r1,r2,r3]

def afficherQuestion():

    print("Entrer 1, 2 ou 3 :")
    choix1 = int(input())

    print(listeQuestion[choix1-1])

    return choix1

def afficherReponse(choix1):
    print("Voulez-vous affiché la réponse ? oui/non")

    choix2 = str(input())

    if choix2 == "oui":
        print("Réponse :",listeReponse[choix1-1])
    else:
        print("La réponse reste masqué")

choix = afficherQuestion()
afficherReponse(choix)