import threading

def Maximum(Arr):

    Max = Arr[0]
    for i in range(1, len(Arr)):
        if (Arr[i] > Max):
            Max = Arr[i]

    print("Maximum number is:", Max)

def Minimum(Arr):

    Min = Arr[0]
    for i in range(1, len(Arr)):
        if (Arr[i] < Min):
            Min = Arr[i]
            
    print("Minimum number is:", Min)

def main():
    No = 0
    Data = list()
    Value = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Maximum, args=[Data])
    t2 = threading.Thread(target=Minimum, args=[Data])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()