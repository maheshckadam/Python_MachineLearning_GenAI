# Accept one number from user and check whether that number is positive or negative or zero. 
# Input: 11    
# Output: Positive Number 
# Input: -8  
# Output: Negative Number  
# Input: 0       
# Output: Zero 

def ChkNum(Value):
    if (Value > 0):
        return "Positive Number"
    elif (Value < 0):
        return "Negative Number"
    else:
        return "Zero"
    
def main():
    No = 0
    Ans = ""

    No = int(input("Enter number: "))
    Ans = ChkNum(No)

    print(Ans)

if __name__ == "__main__":
    main()
