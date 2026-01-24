#  Accept one number and return True if number is odd otherwise False using lambda function

CheckOdd = lambda Value: True if (Value % 2 != 0) else False

def main():
    No1 = 0
    Result = False

    No1 = int(input("Enter Number: "))

    Result = CheckOdd(No1)

    print(Result)

if __name__ == "__main__":
    main()