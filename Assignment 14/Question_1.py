#  Accept one number and return square of that number using lambda function

Square = lambda Value1 : Value1 **2

def main():
    No1 = 0
    Ans = 0
    
    No1 = int(input("Enter Number: "))
    Ans = Square(No1)

    print("Square of number is: ", Ans)


if __name__ == "__main__":
    main()