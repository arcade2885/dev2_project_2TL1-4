
def activer_joker(equipe, question, participation):
    if equipe.jokerUtilise:
        return "refus du joker. joker déjà utiliser"
    if question.estAffichee:
         return "refus du joker. question déjà afficher"
    if  question.estPariable:
         return "refus du joker. question est pariable"

    equipe.utiliserJoker()
    participation.jokerActif = True
    return "joker accepter et activé"
    

def utiliser_joker(equipes, question, participations):
    choix = input("activé le joker pour une equipé ? oui/non : ")

    while choix == "oui":
        nb = 0
        for e in equipes:
            print(nb, e.nom)
            nb = nb + 1

        choixNumeroEquipe = int(input("Choisiser l'equipe qui veut utiliser son joker : "))
        
        if choixNumeroEquipe < 0 or choixNumeroEquipe >= len(equipes):
            print("Numéro invalide veuillez entrer un numéro valide!")

        else:

            equipe = equipes[choixNumeroEquipe]
            participation = participations[choixNumeroEquipe]
            message = activer_joker(equipe, question, participation)
            print(message)

        choix = input("Une autre equipe souhaite utilisé son joker ? oui/non : ")