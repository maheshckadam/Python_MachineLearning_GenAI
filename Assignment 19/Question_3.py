
Range = lambda No: (No >= 70 and No <= 90)
Increment = lambda No: No + 10
Multiplication = lambda A, B: A * B

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if (Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Mult = 1

    for no in Elements:
        Mult = Task(Mult, no)

    return Mult

def main():
    Data = list()
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Actual Data is:", Data)

    FData = list(filterX(Range, Data))
    print("Data after filter is: ", FData)

    MData = list(mapX(Increment,FData))
    print("Data after map is: ", MData)

    RData = reduceX(Multiplication, MData)
    print("Data after reduce is: ", RData)

if __name__ == "__main__":
    main()