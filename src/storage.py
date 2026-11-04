import json
import itertools
from pathlib import Path
from equipe import Equipe


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "data.json"

def load_data() : 
    if not DATA_FILE.exists():
        print('no data')
        return {[]}

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
        return {[]}

def save_data(listEquipes: list):
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    data ={"equipes": [eq.to_dict() for eq in listEquipes]}
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)


#save_data({"equipes":[1,2,3,4]})
#print(load_data())