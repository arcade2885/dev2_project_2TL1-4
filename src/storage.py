import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "data.json"

def load_data() : 
    if not DATA_FILE.exists():
        return {"equipes":[]}

    try:
        with open(DATA_FILE, "r",encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("ERROR")
        return {"equipes":[]}

def save_data(data: dict):
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)


#save_data({"equipes":[1,2,3,4]})
#print(load_data())