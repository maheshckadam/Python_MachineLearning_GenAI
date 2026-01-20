# Accept one number and print cube of that number.

def Cube(Value1):
    res = 0
    res = Value1 **3

    return res

def main():
    No1 = 0
    Ans = 0
    
    No1 = int(input("Enter Number: "))
    Ans = Cube(No1)

    print("Cube of number is: ", Ans)


if __name__ == "__main__":
    main()