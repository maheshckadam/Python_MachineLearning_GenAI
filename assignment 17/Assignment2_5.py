# Accept one number and check whether it is prime or not.
# Input: 11 
# Output: Prime Number

def CheckPrime(Value1):

    for i in range(2, Value1):
        if (Value1 % i == 0):
            return False
        
    return True

def main():
    No1 = 0

    No1 = int(input("Enter Number: "))
    Result = CheckPrime(No1)

    if (Result == True):
        print("Number is Prime")
    else:
        print("Number is Not Prime")

if __name__ == "__main__":
    main()