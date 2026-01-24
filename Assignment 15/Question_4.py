# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements

Add = lambda A, B: A + B

def reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum, no)

    return Sum

def main():
    Data = []
    Result = 0

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    Result = reduceX(Add, Data)
    print("Addition of all elements is:", Result)

if __name__ == "__main__":
    main()
