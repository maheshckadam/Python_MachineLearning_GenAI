# Accept one number and print all even numbers till that number.
# Input: 10 
# Output: 2 4 6 8 10

def EvenNumber(Value1):
    
    for i in range(1, Value1 + 1):
        if (i % 2 == 0):
            print(i)    

def main():
    No1 = 0
    Result = 0

    No1 = int(input("Enter Number: "))
    Result = EvenNumber(No1)

if __name__ == "__main__":
    main()

