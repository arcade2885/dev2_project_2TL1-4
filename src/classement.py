def afficher_classement(equipes):
    classement = "\nClassement : "
    nb = 1
    for equipe in sorted(equipes, key=lambda equipe: equipe.scoreTotal, reverse=True):

        classement = classement + "\n" + str(nb) + ": " + equipe.nom + " " +str(equipe.scoreTotal) + " points"
        nb = nb + 1
    return classement