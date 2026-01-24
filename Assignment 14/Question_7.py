#  Accept one number and return True if number is divisible by 5 otherwise False using lambda function

CheckDivisible = lambda Value: True if (Value % 5 == 0) else False

def main():
    No1 = 0
    Result = False

    No1 = int(input("Enter Number: "))

    Result = CheckDivisible(No1)

    print(Result)

if __name__ == "__main__":
    main()