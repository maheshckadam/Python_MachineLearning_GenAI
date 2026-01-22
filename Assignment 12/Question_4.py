# Accept one number and print that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def Numbers(Value):
    for i in range(1, Value + 1):
        print(i)

def main():
    No = 0

    No = int(input("Enter number: "))
    Numbers(No)

if __name__ == "__main__":
    main()
