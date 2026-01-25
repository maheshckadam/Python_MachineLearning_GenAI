# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element

Maximum = lambda A, B: A if A > B else B

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

    Result = reduceX(Maximum, Data)
    print("Maximum element is:", Result)

if __name__ == "__main__":
    main()
