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

    def get_points(self):
        return self.__points