from concurrent.futures import thread
import threading
import time


class LeThread(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            print(self.name,"traitement_long_1",i)


the_lock= threading.Lock()


def traitement_long_1():
    # time.sleep(1)
    


    with the_lock:
        for i in range(5):
            print("traitement_long_1",i)

def traitement_long_2():
    with the_lock:
        for i in range(5):
            print("traitement_long_2",i)


def main():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)

    threads = [th1,th2]
    # [t.start() for t in threads]
    
    # map(lambda t:t.start(),threads)
    
    print("start")
    th1.start()
    print("between")
    th2.start()

    th1.join()
    th2.join()
    # [t.join() for t in threads]

    print("after")
if __name__=='__main__':
    main()
