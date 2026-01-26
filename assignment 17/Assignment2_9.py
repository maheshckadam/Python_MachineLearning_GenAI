# Accept one number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

def CountDigits(No):
    DigitCount = 0

    DigitCount = len(str(No))

    return DigitCount

def main():
    No = 0
    Ret = 0

    No = int(input("Enter number: "))

    Ret = CountDigits(No)

    print("Number of digits are:", Ret)

if __name__ == "__main__":
    main()


