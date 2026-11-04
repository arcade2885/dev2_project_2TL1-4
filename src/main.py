from equipe import Equipe, CreerEquipe, SameNameError
from storage import load_data, save_data

def main():
    mes_equipes = load_data()
    
    while True:
        print(mes_equipes)
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

    choix1=0

    while choix1 < 1 or choix1 > 3:
        print("Entrer 1, 2 ou 3 :")
        choix1 = int(input())

        if choix1 < 1 or choix1 > 3:
            print("Choix invalide, recommencez.")

    print(listeQuestion[choix1-1])

    return choix1

def afficherReponse(choix1):

    choix2=""

    while choix2 !="oui":
        print("Voulez-vous affiché la réponse ? oui/non/quitter")

        choix2 = str(input())

        if choix2 == "oui":
            print("Réponse :",listeReponse[choix1-1])
        elif choix2 == "quitter":
            break
        else:
            print("Et maintenant ?.")

choix = afficherQuestion()
afficherReponse(choix)