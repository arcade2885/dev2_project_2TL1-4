
import itertools
#from storage import save_data
class SameNameError(Exception):
    pass
class Equipe:
    id = itertools.count(1)
    def __init__(self, nom:str, scoreTotal=0, jokerUtilise=False, equipe_id=None):
        self.id = next(Equipe.id) if equipe_id is None else equipe_id
        #if nom is in SoireeQuiz:
            #raise SameNameError("Ce nom d'équipe exsite déja")
        self.nom = nom
        self.scoreTotal = scoreTotal
        self.jokerUtilise = jokerUtilise
    def ajouterPoints(self, points=1):
        self.scoreTotal += points
    def retirerPoints(self, points=1):
        self.scoreTotal -= points
    def utiliserJoker(self):
        self.jokerUtilise = True
    def __str__(self):
        return f"L'équipe {self.nom} à l'id {self.id} à {self.scoreTotal} points"
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "scoreTotal": self.scoreTotal,
            "jokerUtilise": self.jokerUtilise
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            equipe_id=data.get("id"),
            nom=data.get("nom"),
            scoreTotal=data.get("scoreTotal", 0),
            jokerUtilise=data.get("jokerUtilise", False)
        )

def CreerEquipe():
    a = input("introduit le nom de l'équipe: ")
    New_equipe = Equipe(a)
    print(f"{New_equipe} a ete creer")
    return New_equipe
'''
def main():
    a = Equipe("A")
    b = Equipe("B")
    test = Equipe('test')
    print(a.nom)
    print(a.id)
    print(a.scoreTotal)
    print(a.ajouterPoints(3))
    print(a.ajouterPoints())
    print(a.retirerPoints(2))
    print(a.scoreTotal)
    print(a.jokerUtilise)
    print(b.nom)
    print(b.id)
    print(a)
    CreerEquipe()
    save_data([a,b])

if __name__ == "__main__":
    main()
'''