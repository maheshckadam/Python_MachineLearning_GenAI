# Check Input Number is Even or Odd.
# Input: 11    
# Output: Odd Number

def ChkNum(Value1):
    if (Value1 % 2 == 0):
        return True
    else:
        return False

def main():
    No1 = 0
    Ans = False
    
    No1 = int(input("Enter Number: "))
    Ans = ChkNum(No1)

    if (Ans == True):
        print("Even Number")
    else:
        print("Odd Number")


if __name__ == "__main__":
    main()