# Accept one number and print multiplication table of that number.
# Input: 4 
# Output: 4 8 12 16 20....

def MultiplicationTable(Value1):
    for i in range(1, 11):
        print(Value1 * i)

def main():
    No1 = 0

    No1 = int(input("Enter Number: "))
    MultiplicationTable(No1)

if __name__ == "__main__":
    main()