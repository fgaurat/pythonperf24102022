
class RectangleDec:
    _cpt=0
    def __init__(self,longueur,largeur):
        self._longueur=longueur
        self._largeur=largeur
        RectangleDec._cpt+=1
    
    @classmethod
    def build_from_str(cls,value):
        a,b = [int(i) for i in value.split(',')]
        a,b = map(int,value.split(','))
        return cls(a,b)
    
    @staticmethod
    def get_cpt():
        return RectangleDec._cpt

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    def get_surface(self):
        return self._largeur*self._longueur



    def __del__(self):
        print("def __del__(self)")
        RectangleDec._cpt-=1