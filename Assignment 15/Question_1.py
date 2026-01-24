# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

Square = lambda Value: Value **2

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def main():
    Data = []
    Result = []

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    Result = mapX(Square, Data)
    print("Data after map is:", Result)

if __name__ == "__main__":
    main()