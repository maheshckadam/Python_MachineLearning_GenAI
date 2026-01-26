# Accept one number and dsiplay below pattern
# Input: 3
# Output:   1 2 3
#           1 2 3   
#           1 2 3

def main():
    No = 0

    No = int(input("Enter Number: "))

    for i in range(No):
        for j in range(1, No + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    main()