# Accept one number and return addition of its factors.
# Input: 12 
# Output: 16

def FactorsSum(Value1):
    Sum = 0
    for i in range(1, Value1):
        if (Value1 % i == 0):
            Sum = Sum + i

    return Sum

def main():
    No1 = 0
    Result = 0

    No1 = int(input("Enter Number: "))
    Result = FactorsSum(No1)

    print("Addition of factors is: ", Result)

if __name__ == "__main__":
    main()