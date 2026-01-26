import threading

def EvenList(Data):
    Sum = 0
    print("Even elements are:")

    for no in Data:
        if (no % 2 == 0):
            print(no, end=" ")
            Sum = Sum + no

    print("Sum of even elements is:", Sum)

def OddList(Data):
    Sum = 0
    print("Odd elements are:")

    for no in Data:
        if (no % 2 != 0):
            print(no, end=" ")
            Sum = Sum + no

    print("Sum of odd elements is:", Sum)

def main():

    Data = list()
    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenList, args=[Data])
    t2 = threading.Thread(target=OddList, args=[Data])

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
