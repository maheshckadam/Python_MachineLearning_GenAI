#  Accept two numbers and return multiplication using lambda function.

Multiplication = lambda Value1, Value2: Value1 * Value2

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Result = Multiplication(No1, No2)

    print("Multiplication is: ", Result)

if __name__ == "__main__":
    main()

