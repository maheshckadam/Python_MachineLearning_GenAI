import threading

def EvenFactor(No):
    Sum = 0
    print("Even factors are: ")

    for i in range(1, No + 1):
        if (No % i == 0) and (i % 2 == 0):
            print(i, end=" ")
            Sum = Sum + i

    print("Sum of even factors is: ", Sum)

def OddFactor(No):
    Sum = 0
    print("Odd factors are: ")

    for i in range(1, No + 1):
        if (No % i == 0) and (i % 2 != 0):
            print(i, end=" ")
            Sum = Sum + i

    print("Sum of odd factors is: ", Sum)

def main():

    No = int(input("Enter number: "))

    t1 = threading.Thread(target=EvenFactor, args=[No])
    t2 = threading.Thread(target=OddFactor, args=[No])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
