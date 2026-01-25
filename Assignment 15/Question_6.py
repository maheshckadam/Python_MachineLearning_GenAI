# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element

Minimum = lambda A, B: A if A < B else B

def reduceX(Task, Elements):
    Max = Elements[0]   

    for no in Elements:
        Max = Task(Max, no)

    return Max

def main():
    Data = []
    Result = 0

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    Result = reduceX(Minimum, Data)
    print("Minimum element is:", Result)

if __name__ == "__main__":
    main()
