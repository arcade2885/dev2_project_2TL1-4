import itertools
class Equipe:
    id = itertools.count(1)
    def __init__(self, nom, scoreTotal=0, jokerUtilise=False):
        self.id = next(Equipe.id)
        self.nom = nom
        self.scoreTotal = scoreTotal
        self.jokerUtilise = jokerUtilise
    def ajouterPoints(self):
        self.scoreTotal += 1
    def retirerPoints(self):
        self.scoreTotal -= 1
    def utiliserJoker(self):
        self.jokerUtilise = True
    def __str__(self):
        return f"L'équipe {self.nom} à l'id {self.id} a {self.scoreTotal} points"

def main():
    a = Equipe("A")
    b = Equipe("B")
    c = Equipe("C")
    print(a.nom)
    print(a.id)
    print(a.scoreTotal)
    print(a.ajouterPoints())
    print(a.scoreTotal)
    print(a.jokerUtilise)
    print(b.nom)
    print(b.id)
    print(a)

if __name__ == "__main__":
    main()
