# Accept one number and check whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def CheckPerfect(Value):
    Sum = 0

    for i in range(1, Value):
        if (Value % i == 0):
            Sum = Sum + i

    if (Sum == Value):
        return True
    else:
        return False

def main():
    No = 0
    Result = False

    No = int(input("Enter number: "))
    Result = CheckPerfect(No)

    if (Result == True):
        print("Entered number is Perfect Number")
    else:
        print("Entered number is Not Perfect Number")

if __name__ == "__main__":
    main()
