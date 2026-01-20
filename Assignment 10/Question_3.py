# Accept one number and print factorial of that number.
# Input: 5 
# Output: 120

def Factorial(Value1):
    Fact = 1

    for i in range(1, Value1 + 1):
        Fact = Fact * i

    return Fact

def main():
    No1 = 0
    Result = 0

    No1 = int(input("Enter Number: "))
    Result = Factorial(No1)

    print("Factorial is: ", Result)

if __name__ == "__main__":
    main()