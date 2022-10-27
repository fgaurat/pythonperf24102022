
from collections import deque
from typing import List


# def hello(**kwargs):
def hello(*, name, firstname):
    # print(kwargs)
    # print("Hello", kwargs['name'], kwargs['firstname'])
    print("Hello", name, firstname)

# def add(params:List[int])->int:


def add(*params) -> int:
    """
    return the sum of all elements of l
    """

    print(params)
    r = 0
    for i in params:
        r += i

    return r


def returnValue(i):
    return i


if __name__ == "__main__":
    l = [10, 20, 30, 40]
    a, b, *c = l
    print(a, b, c)
    # c = add(l) # 100
    # c = add(10,20,30,40) # 100
    c = add(*l)  # 100
    # print(c)
    print("toto", "tutu", "tata", sep=" ", end="\n")
    a = [2, 4]
    print(*l)  # [2,4,2,4]
    print(l)
    print(50*'-')
    # hello("GAURAT", "Fred")
    hello(name="GAURAT", firstname="Fred")
    hello(firstname="Fred", name="GAURAT")
    d = {
        "name": "GAURAT",
        "firstname": "Fred"
    }
    print("le 3eme")
    hello(**d)

    print(50*'-')

    l = [10, 20, 30, 40]

    l.append(50)
    print(l)
    l.insert(0, 0)
    print(l)
    i = l.pop()
    print(i)
    print(l)
    i = l.pop(0)
    print(i)
    print(l)

    d = deque(l)

    d.appendleft(0)
    print(d)

    print(50*"-")

    l = []
    for i in range(0, 100, 10):
        l.append(i)

    print(l)

    # l = list(map(lambda e: e, range(0, 100, 10)))
    # print(l)
    l = [i for i in range(10) if i%2 ==0]
    print(l)

    print(50*"-")

    keys = ['key1','key2','key3']
    values = ['value1','value2','value3']
    
    # lt = [('key1',"value1"),('key2',"value2"),('key3',"value3"),]
    lt = list(zip(keys,values))
    d = dict(lt)
    print(lt)
    print(d)

    
