# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

CheckEven = lambda No: (No % 2 == 0)

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result

def main():
    Data = []
    FData = []
    Count = 0

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    FData = filterX(CheckEven, Data)
    Count = len(FData)

    print("Count of even numbers is:", Count)

if __name__ == "__main__":
    main()
