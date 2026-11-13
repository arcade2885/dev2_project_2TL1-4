import json
import itertools
from pathlib import Path
from equipe import Equipe


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "data.json"

def load_data() : 
    """Charge les équipes enregistrées dans le fichier JSON.

    Préconditions : aucune ; le fichier peut ne pas encore exister. S'il existe,
    il doit contenir un objet JSON avec une clé ``equipes`` dont la valeur est
    une liste de dictionnaires compatibles avec ``Equipe.from_dict``.
    Postconditions : renvoie une liste d'objets ``Equipe``. Si le fichier est
    absent, illisible ou contient un JSON invalide, renvoie une liste vide.
    """
    if not DATA_FILE.exists():
        print('no data')
        return []

#   try:
#        with open(DATA_FILE, "r",encoding="utf-8") as file:
#            return json.load(file)

    try:
         with open(DATA_FILE, "r", encoding="utf-8") as file:
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

def save_data(listEquipes: list):
    """Enregistre la liste d'équipes dans le fichier JSON.

    Préconditions : ``listEquipes`` est une liste d'objets ``Equipe`` dont
    ``to_dict()`` renvoie des valeurs sérialisables en JSON.
    Postconditions : le dossier de données existe et le fichier contient un
    objet JSON avec une clé ``equipes`` correspondant à cette liste.
    Une erreur d'accès au fichier ou de sérialisation est propagée à l'appelant.
    """
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    data ={"equipes": [eq.to_dict() for eq in listEquipes]}
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)


#save_data({"equipes":[1,2,3,4]})
#print(load_data())