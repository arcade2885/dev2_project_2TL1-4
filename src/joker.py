def activer_joker(equipe, question, participation):
    if equipe.jokerUtilise or question.estAffichee or question.estPariable:
        return "refus du joker"

    equipe.utiliserJoker()
    participation.jokerActif = True
    return "joker accepter et activé"
    
