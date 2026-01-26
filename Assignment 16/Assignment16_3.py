# Accept two number and add them.
# Input: 11 5
# Output: 16

def Add(Value1, Value2):
   
   Result = Value1 + Value2

   return Result

def main():
    No1 = 0
    No2 = 0
    Ans = 0
    
    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))
    Ans = Add(No1, No2)

    print("Addition is: ", Ans)


if __name__ == "__main__":
    main()