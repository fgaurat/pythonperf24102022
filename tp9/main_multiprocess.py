from multiprocessing import Pool,cpu_count
import time
def f(x,y):
    return x*y

def main():

   
    print(cpu_count())
   
    with Pool(5) as p:
        # print(p.map(f, [1, 2, 3]))
        print(p.starmap(f,[(1,2),(3,4)]))

if __name__=='__main__':
    main()
