# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

Multiply = lambda A, B: A * B

def reduceX(Task, Elements):
    Product = 1

    for no in Elements:
        Product = Task(Product, no)

    return Product

def main():
    Data = []
    Result = 1

    Size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    print("Actual Data is:", Data)

    Result = reduceX(Multiply, Data)
    print("Product of all elements is:", Result)

if __name__ == "__main__":
    main()
