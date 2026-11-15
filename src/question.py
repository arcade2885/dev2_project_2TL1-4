import itertools

class question:
    def __init__(self, question: str, reponse: str, points: int, difficulte: str = ""):
        self.__id = next(itertools.count())
        self.__question = question
        self.__reponse = reponse
        self.__points = points
        self.__difficulte = difficulte

    def get_id(self):
        return self.__id

    def get_question(self):
        return self.__question
    
    def get_reponse(self):
        return self.__reponse
    @property
    def set_reponse(self, reponse):
        self.__reponse = reponse

    def get_difficulte(self):
        return self.__difficulte

    @property
    def set_difficulte(self, difficulte):
        self.__difficulte = difficulte

    def get_points(self):
        return self.__points

    @property
    def set_points(self, points):
        self.__points = points

    @classmethod
    def to_dict(self):
        return {
            "id": self.__id,
            "question": self.__question,
            "reponse": self.__reponse,
            "points": self.__points,
            "difficulte": self.__difficulte
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