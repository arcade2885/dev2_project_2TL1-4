from equipe import Equipe, CreerEquipe, SameNameError
from storage import load_data, save_data
from joker import utiliser_joker
from classement import afficher_classement


# class tempo a changer plus tard 
class Question:
    pass

class Participation:
    pass


mes_equipes = load_data()


def main():
    mes_equipes = load_data()
    jocker_active = False

    while True:
        mes_equipes = load_data()
        print("\nMenu principal :")
        print("1. Créer une nouvelle équipe")
        print("2. Afficher les équipes existantes")
        print("3. Question")
        print("4. Quitter le jeu")
        input_choice = input("Choisissez une option (1-4) : ")
        if input_choice == "1":
            new_team()
        elif input_choice == "2":
            if not mes_equipes:
                print("Aucune équipe n'existe.")
            else:
                print("Équipes existantes :")
                for equipe in mes_equipes:
                    print(equipe)
        elif input_choice == "3":
            while True:
                question = Question()
                question.estAffichee = False # a changer plus tard 
                question.estPariable = False # a changer plus tard 

                participations = []
                for e in mes_equipes:
                    p = Participation()
                    p.jokerActif = False # a changer plus tard
                    participations = participations + [p]

                utiliser_joker(mes_equipes, question, participations)

                choix = afficherQuestion()
                afficherReponse(choix)
                add_points(jocker_active)
                print(afficher_classement(mes_equipes))
                print("1. Continuer avec une autre question")
                print("2. Retour au menu principal")
                sub_choice = input("Choisissez une option (1-2) : ")
                if sub_choice == "1":
                    continue
                elif sub_choice == "2":
                    break
        elif input_choice == "4":
            end_game()
            break
            
                    

def add_points(jocker):
    for i in range(len(mes_equipes)):
        print(f"Équipe {mes_equipes[i].nom}")
    print('quelle equipe a reçu les points ?')
    input_choice = input("Entrez le nom de l'équipe : ")
    for equipe in mes_equipes:
        if equipe.nom == input_choice:
            points = 1
            if jocker:
                points *= 2
            equipe.ajouterPoints(points)
            print(f"{points} points ajoutés à l'équipe {equipe.nom}.")
            save_data(mes_equipes)
            return
    print('test points', jocker)

def show_scores():
    print("test show scores")


q1="Quel est la capitale du Congo ?"
q2="Quel est la capitale de Chine ?"
q3="Quel est la capitale de la Colombie ?"

listeQuestion=[q1,q2,q3]

r1="Brazzaville"
r2="Pékin"
r3="Bogota"

listeReponse=[r1,r2,r3]

d1 = "Facile"
d2 = "Facile"
d3 = "Moyenne"

listeDifficulte = [d1, d2, d3]

def afficherQuestion():
    """
    Pre: listeQuestion à au moins 1 question
    Post: un numéro est choisi, la question est affiché et le numéro choisi est retourné
    """
    choix1=0

    while choix1 < 1 or choix1 > 3:
        print("Entrer 1, 2 ou 3 :")
        choix1 = int(input())

        if choix1 < 1 or choix1 > 3:
            print("Choix invalide, recommencez.")

    print(listeQuestion[choix1-1])

    return choix1

def afficherReponse(choix1):
    """
    Pre: choix1 est une valeur correct et listeReponse contient autant de réponse que ListeQuestion de question
    Post: si oui est sélèctionner monter la réponse et si quitter l'est arreter la fonction
    """
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

#choix = afficherQuestion()
#afficherReponse(choix)


def new_team():
    try:
        new_team = CreerEquipe()
        mes_equipes.append(new_team)
        save_data(mes_equipes)
    except SameNameError as e:
        print(e)

def end_game():
    print("Merci d'avoir joué !")
    save_data(mes_equipes)
    



if __name__ == "__main__":
    main()
