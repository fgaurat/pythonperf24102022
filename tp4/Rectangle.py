

from ICalcGeo import ICalcGeo
from IMetaCalcGeo import IMetaCalcGeo


# class Rectangle(ICalcGeo):
class Rectangle(IMetaCalcGeo):

    def __init__(self,longueur,largeur):
        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self,longueur):
        self._longueur = longueur

    def set_largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._largeur*self._longueur

    def __eq__(self, o) -> bool:
        return self._longueur == o._longueur and self._largeur == o._largeur

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self._longueur=}, largeur={self._largeur}'

    def __del__(self):
        print("def __del__(self)")