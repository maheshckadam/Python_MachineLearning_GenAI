#  Accept one number and return cube of that number using lambda function

Cube = lambda Value1 : Value1 **3

def main():
    No1 = 0
    Ans = 0
    
    No1 = int(input("Enter Number: "))
    Ans = Cube(No1)

    print("Cube of number is: ", Ans)


if __name__ == "__main__":
    main()