# Accept one number and print sum of first N natural numbers.
# Input: 5 
# Output: 15

def SumOfNumbers(Value1):
    Sum = 0
    for i in range(Value1 + 1):
        Sum = Sum + i

    return Sum

def main():
    No1 = 0
    Result = 0

    No1 = int(input("Enter Number: "))
    Result = SumOfNumbers(No1)

    print("Sum of Natural number is: ", Result)

if __name__ == "__main__":
    main()