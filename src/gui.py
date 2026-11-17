import tkinter as tk
from joker import activer_joker
from classement import afficher_classement


def gui(equipes, question, participations):
    SoireQuiz = tk.Tk()
    SoireQuiz.title("Soiré Quiz")

    txtEquipes = ""
    i = 0
    for e in equipes:
        txtEquipes = txtEquipes + str(i) + " " + e.nom 
        i = i + 1


    tk.Label(SoireQuiz, text=txtEquipes).pack()
    tk.Label(SoireQuiz, text="Entrez le numéro de l'équipe qui souhaite utilisée sont joker : (Si aucune équipe souhaite utilisé sont joker appuyer simple sur continue sans introduire de numéro dans la boite)").pack()
    
    boite = tk.Entry(SoireQuiz)
    boite.pack()

    mess = tk.Label(SoireQuiz, text="")
    mess.pack()

    classement = tk.Label(SoireQuiz, text=afficher_classement(equipes))
    classement.pack()
        
    def bouton_joker():
        try:
            num = int(boite.get())
        except ValueError:
            mess.config(text="Numéro pas valide!!")
            return

        if num < 0 or num >= len(equipes):
            mess.config(text="Numéro pas valide!!")
        else:
                mess.config(text=activer_joker(equipes[num], question, participations[num]))
                classement.config(text=afficher_classement(equipes))

                

    # les 2 boutton pour continuer et passer a la suite du quiz il faut appuyer sur continuer et la suite du quiz continue dans le terminal
    tk.Button(SoireQuiz, text="Activer joker", command=bouton_joker).pack()
    tk.Button(SoireQuiz, text="Continuer", command=SoireQuiz.destroy).pack()

    SoireQuiz.mainloop()
  