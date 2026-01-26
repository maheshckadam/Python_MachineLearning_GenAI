# Accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input: 11, Elements = 13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5
# Output: 3

def Frequency(Arr, Value1):
    Count = 0
    for i in range(len(Arr)):
        if (Arr[i] == Value1):
            Count = Count + 1
    return Count

def main():
    No = 0
    Data = list()
    Value = 0
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Value = int(input("Enter number to search frequency: "))

    Result = Frequency(Data, Value)
    
    print("Frequency of", Value, "is:", Result)


if __name__ == "__main__":
    main()