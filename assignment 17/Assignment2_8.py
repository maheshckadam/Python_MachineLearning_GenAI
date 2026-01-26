# Accept one number and dsiplay below pattern
# Input: 3
# Output:   1 
#           1 2   
#           1 2 3

def DisplayPattern(Value1):
    for i in range(1, Value1 + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print() 

def main():
    No = 0

    No = int(input("Enter Number: "))
    DisplayPattern(No)

if __name__ == "__main__":
    main()  