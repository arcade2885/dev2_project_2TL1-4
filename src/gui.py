import tkinter as tk
from joker import activer_joker
from classement import afficher_classement
from tkinter import ttk

def gui(equipes, question, participations, mes_questions):
    SoireQuiz = tk.Tk()
    SoireQuiz.title("Soiré Quiz")
    SoireQuiz.geometry("700x400")
    SoireQuiz.resizable(False, False)

    def vider_fenetre():
        for widget in SoireQuiz.winfo_children():
            widget.destroy()

    def afficher_questions():
        vider_fenetre()

        tk.Label(SoireQuiz, text="Choisissez une question").pack(pady=10)

        liste = [q.question for q in mes_questions]

        choix = ttk.Combobox(SoireQuiz, values=liste, state="readonly",width=80)
        choix.current(0)
        choix.pack(pady=10)

        def confirmer():
            afficher_question(choix.current())

        tk.Button(
            SoireQuiz,
            text="Confirmer",
            command=confirmer
        ).pack(pady=10)

    def afficher_question(i):
        vider_fenetre()

        tk.Label(
            SoireQuiz,
            text=mes_questions[i].question
        ).pack()

        tk.Button(
            SoireQuiz,
            text="Afficher la réponse",
            command=lambda: afficher_reponse(i)
        ).pack()
        tk.Button(
            SoireQuiz,
            text="Retour",
            command=afficher_questions
        ).pack()

    def afficher_reponse(i):
        vider_fenetre()

        tk.Label(
            SoireQuiz,
            text="Réponse : " + mes_questions[i].reponse
        ).pack(pady=20)

        tk.Button(
            SoireQuiz,
            text="Retour au terminal",
            command=SoireQuiz.destroy
        ).pack()

    txtEquipes = ""
    i = 0
    for e in equipes:
        txtEquipes = txtEquipes + str(e.id) + " " + e.nom + "\n"
        i = i + 1


    tk.Label(SoireQuiz, text="Equipe : " + txtEquipes).pack()
    tk.Label(SoireQuiz, text="Entrez le numéro de l'équipe qui souhaite utilisée sont joker : \n(Si aucune équipe souhaite utilisé sont joker appuyer simple sur continue sans introduire de numéro dans la boite)").pack()
    
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

        for e in equipes:
            if e.id == num:
                mess.config(text=activer_joker(e, question, participations[e.id]))
                classement.config(text=afficher_classement(equipes))
                return

        mess.config(text="Numéro pas valide!!")




    # les 2 boutton pour continuer et passer a la suite du quiz il faut appuyer sur continuer et la suite du quiz continue dans le terminal
    tk.Button(SoireQuiz, text="Activer joker", command=bouton_joker).pack()
    tk.Button(SoireQuiz, text="Continuer", command=afficher_questions).pack()

    SoireQuiz.mainloop()
