# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

CheckDivisible = lambda No: (No % 3 == 0 and No % 5 == 0)

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result

def main():
    Data = []
    Result = []

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    Result = filterX(CheckDivisible, Data)
    print("Data after filter is:", Result)

if __name__ == "__main__":
    main()
