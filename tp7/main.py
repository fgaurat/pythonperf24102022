import traceback

from DivBy12Error import DivBy12Error




def div(a,b):
    if b ==12:
        err = DivBy12Error()
        raise err

    r = a/b
    return r

def call_div(a,b):
    r=0
    try:
        print('ouverture fichier')
        r = div(a,b)
    finally:    
        print('fermeture fichier')
    return r


def main():
    try:
        b=2
        c=int(input("Valeur de c:"))
        a=call_div(b,c)
        print("résultat :",a)
    # except (ZeroDivisionError , TypeError) as e:
    except ZeroDivisionError as e:
        traceback.print_exc()
        print("ZeroDivisionError erreur",e)
    except TypeError as e:
        traceback.print_exc()
        print("TypeError erreur",e)
    except ValueError as e:
        traceback.print_exc()
        print("ValueError erreur",e)
    except DivBy12Error as e:
        traceback.print_exc()
        print("DivBy12Error erreur",e)
    except Exception as e:
        traceback.print_exc()
        print("erreur",e)
    else:
        print("else")
    finally:
        print("finally")
    print("fin du script")




if __name__=='__main__':
    main()
