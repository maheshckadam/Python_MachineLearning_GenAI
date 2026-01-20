# Accept one number and print reverse of that number.
# Input: 123 
# Output: 321

def ReverseNumber(Value1):
    Rev = ""

    for ch in (Value1):
        Rev = ch + Rev  

    return Rev

def main():
    No1 = 0
    Result = 0

    No1 = input("Enter Number: ")   

    Result = ReverseNumber(No1)

    print("Reverse Number is: ", Result)

if __name__ == "__main__":
    main()