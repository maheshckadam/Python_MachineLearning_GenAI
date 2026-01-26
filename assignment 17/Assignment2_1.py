import Arithmetic

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Result = Arithmetic.Add(No1, No2)
    print("Addition:", Result)

    Result = Arithmetic.Sub(No1, No2)
    print("Subtraction:", Result)

    Result = Arithmetic.Mult(No1, No2)
    print("Multiplication:", Result)

    Result = Arithmetic.Div(No1, No2)
    print("Division:", Result)

if __name__ == "__main__":
    main()