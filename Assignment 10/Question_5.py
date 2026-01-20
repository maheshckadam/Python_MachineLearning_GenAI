# Accept one number and print all odd numbers till that number.
# Input: 10 
# Output: 1 3 5 7 9

def OddNumber(Value1):
    
    for i in range(1, Value1 + 1):
        if (i % 2 != 0):
            print(i)    

def main():
    No1 = 0    

    No1 = int(input("Enter Number: "))
    OddNumber(No1)

if __name__ == "__main__":
    main()