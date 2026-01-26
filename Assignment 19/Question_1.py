# Accept number from user and return its power of two using lambda function.
# Input: 6
# Output: 64

PowerOfTwo = lambda No: 2 ** No

def main():
    No = int(input("Enter number: "))
    Result = PowerOfTwo(No)

    print("Power of two is: ", Result)

if __name__ == "__main__":
    main()