


from Rectangle import Rectangle


class Carre(Rectangle):

    def __init__(self, cote):
        super().__init__(cote, cote)
        self._cote = cote
        print(f"def __init__(self, {cote})")

    def __str__(self):
        return f'{self.__class__.__name__} cote:{self._cote}'