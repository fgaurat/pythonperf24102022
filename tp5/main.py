from typing import Any
from Rectangle import Rectangle


class Truc:

    def __call__(self, *args, **kwds):
        print('call')
    
    def __new__(cls):
        print('new')
        return cls
    
    def __init__(self) -> None:
        print('init')
def main():
    r1 = Rectangle(1,2)
    r2 = Rectangle(12,34)
    print("r1",r1)
    print("r2",r2)
    print(id(r1))
    print(id(r2))
    print(50*'-')
    t = Truc()
    


if __name__=='__main__':
    main()
