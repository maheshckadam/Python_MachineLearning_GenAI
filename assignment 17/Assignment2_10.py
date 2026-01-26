# Accept one number and print sum of digits.
# Input: 5187934 
# Output: 37

def SumOfDigits(Value1):
    Sum = 0

    for i in range(0, len(Value1)):
        Sum = Sum + int(Value1[i])

    return Sum

def main():
    No1 = 0
    Result = 0

    No1 = input("Enter Number: ")   

    Result = SumOfDigits(No1)

    print("Sum Of Digits is: ", Result)

if __name__ == "__main__":
    main()