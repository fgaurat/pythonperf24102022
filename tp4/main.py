from typing import Protocol
from Rectangle import Rectangle
from Carre import Carre
from RectangleDec import RectangleDec
from RectangleDC import RectangleDC
from ICalcGeo import ICalcGeo
from Cercle import Cercle
from IMetaCalcGeo import IMetaCalcGeo


    
def main01():
    r = Rectangle(2,3)
    r1 = Rectangle(longueur=2,largeur=3)
    # print(r.longueur)# erreur !
    print(r.get_longueur())# 2
    # r.set_longueur(3)
    print(r.get_longueur())# 3

    print(r)
    print(r1)

    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")


    r2 = RectangleDec(3,4)
    r2.longueur = 12
    print(r2.longueur)
    r2.largeur = 12
    print(r2.largeur)


    r3 = RectangleDC()
    r4 = RectangleDC(4)

    print(r3.largeur)
    print(r3)
    print(r4.surface)



def show_surface(o:ICalcGeo):
    print("show_surface")
    print(o.get_surface())



def main02():
    r = RectangleDec(3,4)
    r1 = RectangleDec(3,4)
    r2 = RectangleDec(3,4)
    r3 = RectangleDec.build_from_str("3,4")
    print(RectangleDec.get_cpt())
    print(r.get_cpt())
    print("r3",r3)
    print(f"r3.longueur:{r3.longueur}")
    c = Carre(3)
    print("Carre",c)
    print(c.get_surface())

    show_surface(r3)
    show_surface(c)
    # show_surface(2)

    ce = Cercle(2)    
    # print(ce.get_surface())

def main():
    # i =IMetaCalcGeo()
    r = Rectangle(2,5)
    print(type(int))
    print(type(str))
    print(type(Cercle))
    print(type(type))


if __name__=='__main__':
    main()
