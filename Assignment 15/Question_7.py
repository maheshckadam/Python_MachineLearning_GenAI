# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5

CheckLength = lambda Str: (len(Str) > 5)

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

    Size = int(input("Enter number of strings: "))

    print("Enter strings:")
    for i in range(Size):
        Data.append(input())

    print("Actual Data is:", Data)

    Result = filterX(CheckLength, Data)
    print("Strings having length greater than 5 are:", Result)

if __name__ == "__main__":
    main()
