import itertools
class SameNameError(Exception):
    pass
class Equipe:
    id = itertools.count(1)
    def __init__(self, nom:str, scoreTotal=0, jokerUtilise=False):
        self.id = next(Equipe.id)
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

def CreerEquipe():
    a = input("introduit le nom de l'équipe: ")
    truc = Equipe(a)
    print(f"{truc} a ete creer")

def main():
    a = Equipe("A")
    b = Equipe("B")
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

if __name__ == "__main__":
    main()
