# Accept one number and print its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def Factors(Value1):
    for i in range(1, Value1 + 1):
        if (Value1 % i == 0):
            print(i)

def main():
    No1 = 0

    No1 = int(input("Enter number: "))
    Factors(No1)

if __name__ == "__main__":
    main()
