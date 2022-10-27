# import lib as l

# from lib import add as ad
# from libmath import lib
import libmath.lib
# from libmath.lib import add



def add(a,b):
    print("local",a,b)

def main():

    c = libmath.lib.add(1,2)
    print(c)

if __name__=='__main__':
    main()
