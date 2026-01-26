# Write one function that accept one number from user and returns true if number is divisible by 5 else return false. 
# Input: 8    
# Output: False 
# Input: 25
# Output: True 

def ChkDivisible(Value):
    if (Value % 5 == 0):
        return True
    else:
        return False
    
def main():
    No = 0
    Ans = False

    No = int(input("Enter number: "))
    Ans = ChkDivisible(No)

    if (Ans == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()