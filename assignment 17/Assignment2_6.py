# Accept one number and dsiplay below pattern
# Input: 3
# Output:   * * *
#           * * 
#           * 

def main():
    No = 0

    No = int(input("Enter Number: "))

    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    main()