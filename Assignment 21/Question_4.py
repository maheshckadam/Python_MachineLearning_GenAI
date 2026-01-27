import threading

Sum = 0
Multiplication = 1

def SumList(Data):
    global Sum

    for no in (Data):
        Sum = Sum + no

def ProductList(Data):
    global Multiplication

    for no in (Data):
        Multiplication = Multiplication * no

def main():
    
    global Sum
    global Multiplication
    No = 0
    Data = list()
    Value = 0

    No = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=SumList, args=[Data])
    t2 = threading.Thread(target=ProductList, args=[Data])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is:", Sum)
    print("Product of elements is:", Multiplication)

if __name__ == "__main__":
    main()
