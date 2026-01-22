# Accept one number and prints its binary equivalent.

def main():
    No = 0

    No = int(input("Enter number: "))

    print("Binary Equivalent is: ", bin(No)[2:])

if __name__ == "__main__":
    main()
