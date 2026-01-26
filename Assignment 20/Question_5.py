import threading

def DisplayForward():
    for i in range(1, 51):
        print(i)

def DisplayReverse():
    for i in range(50, 0, -1):
        print(i)

def main():

    t1 = threading.Thread(target=DisplayForward)
    t2 = threading.Thread(target=DisplayReverse)

    t1.start()
    t1.join()    

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
