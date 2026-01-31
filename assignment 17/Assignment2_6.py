# Accept one number and dsiplay below pattern
# Input: 3
# Output:   * * *
#           * * 
#           * 

def DisplayPattern(Value1):
    for i in range(Value1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    No = 0

    No = int(input("Enter Number: "))
    DisplayPattern(No)

if __name__ == "__main__":
    main()