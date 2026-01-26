
CheckEven = lambda No : (No % 2 == 0)
Square = lambda No : No ** 2
Add = lambda A, B : A + B

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result

def  mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def  reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum,no)

    return Sum



def main():
    Data = list()
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filterX(CheckEven, Data))
    print("Data after filter is: ", FData)

    MData = list(mapX(Square,FData))
    print("Data after map is: ", MData)

    RData = reduceX(Add, MData)
    print("Data after reduce is: ", RData)

if __name__ == "__main__":
    main()