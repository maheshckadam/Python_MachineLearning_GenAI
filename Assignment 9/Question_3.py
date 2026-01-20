# Accept one number and print square of that number.
# Input: 5 
# Output: 25

def Square(Value1):
    res = 0
    res = Value1 **2

    return res

def main():
    No1 = 0
    Ans = 0
    
    No1 = int(input("Enter Number: "))
    Ans = Square(No1)

    print("Square of number is: ", Ans)


if __name__ == "__main__":
    main()