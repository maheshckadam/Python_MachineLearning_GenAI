# Accept three numbers and return largest number using lambda function

Largest = lambda Value1, Value2, Value3: Value1 if (Value1 >= Value2 and Value1 >= Value3) else (Value2 if Value2 >= Value3 else Value3)

def main():
    No1 = 0
    No2 = 0
    No3 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))
    No3 = int(input("Enter Third Number: "))

    Result = Largest(No1, No2, No3)

    print(Result, "is largest")

if __name__ == "__main__":
    main()
