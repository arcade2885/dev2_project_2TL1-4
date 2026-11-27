from gui import gui 
from equipe import Equipe, CreerEquipe, SameNameError, list_equipes, supp_toutes_equipes, supp_equipe, renommer_equipe
from storage import load_data_equipe, save_data_equipe, save_data_question, load_data_question
from joker import utiliser_joker
from classement import afficher_classement
from question import question,CreerQuestion


class Participation:
    pass
def load_data():
    return load_data_equipe()
def save_data(listEquipes: list):
    save_data_equipe(listEquipes)

mes_equipes = load_data()


def main():
    # mes_equipes = load_data()
    jocker_active = False
    mes_questions = load_data_question()
    while True:
        # mes_equipes = load_data()
        print("\nMenu principal :")
        print("1. gérer les équipes")
        print("2. Afficher les équipes existantes")
        print("3. Question")
        print("4. Quitter le jeu")
        
        input_choice = input("Choisissez une option (1-6) : ")
        if input_choice == "1":
            gerer_equipes()
            
        elif input_choice == "2":
            list_equipes(mes_equipes)
                    
        elif input_choice == "3":
            while True:
                #question = question()
                question.estAffichee = False # a changer plus tard 
                question.estPariable = False # a changer plus tard 

                participations = []
                for e in mes_equipes:
                    p = Participation()
                    p.jokerActif = False # a changer plus tard
                    participations = participations + [p]

                gui(mes_equipes, question, participations, mes_questions)
                add_points(jocker_active)
                print(afficher_classement(mes_equipes))
                print("\n1. Continuer avec une autre question")
                print("2. Retour au menu principal")
                sub_choice = input("Choisissez une option (1-2) : ")
                if sub_choice == "1":
                    continue
                elif sub_choice == "2":
                    break

        elif input_choice == "4":
            end_game()
            break
            
def gerer_equipes():
    while True:
        print("\nGestion des équipes :")
        print("1. Créer une équipe")
        print("2. Rennomer une equipe")
        print("3. réinitialiser les scores")
        print("4. Supprimer une équipe")
        print("5. supprimer toute les equipes")
        print("6. Retour au menu principal")
        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            new_team()

        elif choix == "2":
            renommer_equipe(mes_equipes)
            save_data(mes_equipes)
            
        elif choix == "3":
            reset_scores()

        elif choix == "4":
            if not mes_equipes:
                print("Aucune équipe n'existe.")
                continue
            print("\n")
            for equipe in mes_equipes:
                print(equipe)

            try:
                id_equipe = int(input("Entrez l'ID de l'équipe à supprimer : "))
            except ValueError:
                print("Veuillez entrer un identifiant numérique.")
                continue

            supp_equipe(mes_equipes, id_equipe)
            save_data(mes_equipes)
            
        elif choix == "5":
            supp_toutes_equipes(mes_equipes)
            save_data(mes_equipes)
        elif choix == "6":
            break
        else:
            print("Option invalide.")
            

def add_points(jocker):
    """
    Pre:mes_equipes contient des objets équipe avec un identifiant et
    une méthode ajouterPoints(). Pour garantir l'ajout de points,l'utilisateur saisit un identifiant numérique correspondant à une équipe 
    Post: Si l'identifiant correspond à une équipe, son score augmente de 1 point,
    ou de 2 points si jocker est vrai, puis les équipes sont sauvegardées. Si aucun identifiant ne correspond, aucun score n'est modifié.
    .
    """
    for i in range(len(mes_equipes)):
        print(f"Équipe {mes_equipes[i].nom} ID: {mes_equipes[i].id}")
    print('\n quelle equipe a reçu les points ?')
    input_choice = input("Entrez le ID de l'équipe : ")
    for equipe in mes_equipes:
        if equipe.id == int(input_choice):
            points = 1
            if jocker:
                points *= 2
            equipe.ajouterPoints(points)
            print(f"\n{points} points ajoutés à l'équipe {equipe.nom}.")
            save_data(mes_equipes)
            return
    print('test points', jocker)

def reset_scores():
    for equipe in mes_equipes:
        equipe.scoreTotal = 0
    save_data(mes_equipes)
    print("Scores réinitialisés pour toutes les équipes.")


def afficherQuestion(listeQuestion):
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

    print(listeQuestion[choix1-1].question)

    return choix1

def afficherReponse(choix1,listeQuestion):
    """
    Pre: choix1 est une valeur correct et listeReponse contient autant de réponse que ListeQuestion de question
    Post: si oui est sélèctionner monter la réponse et si quitter l'est arreter la fonction
    """
    choix2=""

    while choix2 !="oui":
        print("Voulez-vous affiché la réponse ? oui/non/quitter")

        choix2 = str(input())

        if choix2 == "oui":
            print("Réponse :",listeQuestion[choix1-1].reponse)
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
