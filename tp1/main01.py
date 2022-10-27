from sys import getrefcount
import copy

# HelloWorld => UpperCamelCase
# helloWorld => camelCase
# hello_world => snake
# hello-world => kebab



def main():

    print(getrefcount(1))
    a = 1
    print(getrefcount(1))
    b = 1
    print(getrefcount(1))
    print(hex(id(a)))
    print(hex(id(b)))
    # a=2
    # print(a)
    # print(hex(id(a)))

    path = r"c:\natation\tennis"
    print(path)

    s = f"valeur de a : {a}"
    s = "valeur de a : {0}".format(a)
    print(s)
    print(50*"-")
    ma_liste = ["value 1", "value 2", "value 3", "value 4", "value 5"]
    # ma_liste_1 = ma_liste[:]
    ma_liste_1 = ma_liste
    # l = ma_liste[-1]
    # print(l)

    ma_liste[0] = "Toto"
    print(ma_liste)
    print(ma_liste_1)

    e1 = [10, 20]
    e2 = [30, 40]
    e3 = [50, 60]
    l = [e1, e2, e3]
    # l1=l[:] shallow
    l1 = copy.deepcopy(l)  # [:] shallow
    l[1][1] = 1000
    print(l)
    print(l1)


if __name__ == '__main__':
    main()
