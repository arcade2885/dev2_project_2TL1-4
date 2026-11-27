import json
import itertools
from pathlib import Path
from equipe import Equipe
from question import CreerQuestion, question

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE_EQUIPE = DATA_DIR / "equipe.json"
DATA_FILE_QUESTION = DATA_DIR / "question.json"

def load_data_equipe(data_equipe = DATA_FILE_EQUIPE) : 
    """Charge les équipes enregistrées dans le fichier JSON.

    Pre : aucune ; le fichier peut ne pas encore exister. S'il existe,
    il doit contenir un objet JSON avec une clé equipes dont la valeur est
    une liste de dictionnaires compatibles avec Equipe.from_dict.
    Post : renvoie une liste d'objets Equipe. Si le fichier est
    absent, illisible ou contient un JSON invalide, renvoie une liste vide.
    """
    if not data_equipe.exists():
        print('no data')
        return []

#   try:
#        with open(DATA_FILE, "r",encoding="utf-8") as file:
#            return json.load(file)

    try:
         with open(data_equipe, "r", encoding="utf-8") as file:
            data = json.load(file)
            equipes_data = data.get("equipes", [])
            equipes = [Equipe.from_dict(eq) for eq in equipes_data]
            if equipes:
                max_id = max(eq.id for eq in equipes)
                Equipe.id = itertools.count(max_id + 1)
            return equipes
    except (json.JSONDecodeError, OSError):
        print("ERROR")
        return []

def load_data_question(data_question = DATA_FILE_QUESTION) :
    """if not data_question.exists():
        print('no data')
        return []

    try:
         with open(data_question, "r", encoding="utf-8") as file:
            data = json.load(file)
            questions_data = data.get("questions", [])
            questions = [question.from_dict(q) for q in questions_data]
            if questions:
                max_id = max(q.id for q in questions)
                question.id = itertools.count(max_id + 1)
            return questions
    except (json.JSONDecodeError, OSError):
        print("ERROR")
        return []"""
    load_data_equipe(data_question)
#save_data({"equipes":[1,2,3,4]})
#print(load_data())

def save_data_equipe(listEquipes: list, data_equipe =DATA_FILE_EQUIPE):
    """Enregistre la liste d'équipes dans le fichier JSON.

    Pre : listEquipes est une liste d'objets Equipe dont
    to_dict() renvoie des valeurs sérialisables en JSON.
    Post : le dossier de données existe et le fichier contient un
    objet JSON avec une clé "equipes" correspondant à cette liste.
    Une erreur d'accès au fichier ou de sérialisation est propagée à l'appelant.
    """
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    data ={"equipes": [eq.to_dict() for eq in listEquipes]}
    with open(data_equipe, "w", encoding="utf-8") as file:
        json.dump(data, file)

def save_data_question(listQuestions: list,data_question =DATA_FILE_QUESTION ):
    '''DATA_DIR.mkdir(parents=True,exist_ok=True)
    data ={"questions": [q.to_dict() for q in listQuestions]}
    with open(data_question, "w", encoding="utf-8") as file:
        json.dump(data, file)'''
    save_data_equipe(listQuestions,data_question)




"""

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
listeQuestion = []
listeQuestion.append(CreerQuestion(q1, r1,1, d1))
listeQuestion.append(CreerQuestion(q2, r2,1, d2))
listeQuestion.append(CreerQuestion(q3, r3,2, d3))
save_data_question(listeQuestion)

"""
