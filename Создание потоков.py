import threading
import time

def potok():
    for pot in range(1, 11):
        print(pot)
        time.sleep(1)

def potok2():
    for pot2 in "abcdfghij":
        print(pot2)
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=potok)
    t2 = threading.Thread(target=potok2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Done")