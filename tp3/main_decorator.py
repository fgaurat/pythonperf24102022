
def do_log(params):
    print(params)
    def wrapper0(func):
        def wrapper(*args):
            print(func.__name__,"args",args)
            r = func(*args)
            print(func.__name__,"return",r)
            return r
        return wrapper
    return wrapper0



@do_log('toto')
def say_hello(name):
    return f"Bonjour {name}"

def main():
    s = say_hello("Fred")
    print(s)


if __name__=='__main__':
    main()
