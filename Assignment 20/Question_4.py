import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if (ch.islower()):
            Count = Count + 1

    print("Small letters count is:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def Capital(Str):
    Count = 0

    for ch in Str:
        if (ch.isupper()):
            Count = Count + 1

    print("Capital letters count is:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def Digits(Str):
    Count = 0

    for ch in Str:
        if (ch.isdigit()):
            Count = Count + 1

    print("Digits count is:", Count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)

def main():

    Str = input("Enter string: ")

    t1 = threading.Thread(target=Small, args=[Str])
    t2 = threading.Thread(target=Capital, args=[Str])
    t3 = threading.Thread(target=Digits, args=[Str])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
