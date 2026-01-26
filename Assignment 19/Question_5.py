
CheckPrime = lambda No: all(No % i != 0 for i in range(2, No)) if No > 1 else False
Multiply = lambda No: No * 2
Maximum = lambda A, B: A if A > B else B

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
    Max = Elements[0]

    for no in Elements:
        Max = Task(Max, no)

    return Max

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

    FData = filterX(CheckPrime, Data)
    print("Data after filter is:", FData)

    MData = mapX(Multiply, FData)
    print("Data after map is:", MData)

    RData = reduceX(Maximum, MData)
    print("Data after reduce is:", RData)

if __name__ == "__main__":
    main()
