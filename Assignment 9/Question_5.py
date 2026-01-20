# Accept one number and check whether it is divisible by 3 and 5
# Input: 15 
# Output: Divisible by 3 and 5

def CheckDivision(Value1):
    if (Value1 % 3 == 0) and (Value1 % 5 == 0):
        return True
    else:
        return False

def main():
    No1 = 0
    Ans = False
    
    No1 = int(input("Enter Number: "))
    Ans = CheckDivision(No1)

    if (Ans == True):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")


if __name__ == "__main__":
    main()