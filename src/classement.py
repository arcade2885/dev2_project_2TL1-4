def afficher_classement(equipes):
    classement = "Classement : "
    nb = 1
    equipes.sort(key=lambda equipe: equipe.scoreTotal, reverse=True)

    for equipe in equipes:
        classement = classement + "\n" + str(nb) + ": " + equipe.nom + " " +str(equipe.scoreTotal) + " points"
        nb = nb + 1
    return classement