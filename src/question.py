import itertools

class question:
    def __init__(self, question: str, reponse: str, points: int, difficulte: str = ""):
        self.__id = next(itertools.count())
        self.__question = question
        self.__reponse = reponse
        self.__points = points
        self.__difficulte = difficulte
    @property
    def id(self):
        return self.__id
    @property
    def question(self):
        return self.__question
    @property
    def reponse(self):
        return self.__reponse
    @reponse.setter
    def reponse(self, reponse):
        self.__reponse = reponse
    @property
    def difficulte(self):
        return self.__difficulte

    @difficulte.setter
    def difficulte(self, difficulte):
        self.__difficulte = difficulte
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "reponse": self.reponse,
            "points": self.points,
            "difficulte": self.difficulte
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            question=data.get("question"),
            reponse=data.get("reponse"),
            points=data.get("points"),
            difficulte=data.get("difficulte", "")
        )


def CreerQuestion(question_txt,reponse_txt,points,difficulte=""):
    New_question = question(question_txt,reponse_txt,points,difficulte)
    #print(f"{New_question} a ete creer")
    return New_question
