# Accept N numbers from user and store it into List. Return Maximum number from that List.
# Input: 7, Elements = 13 5 45 7 4 56 34
# Output: 56

def Maximum(Arr):

    Max = Arr[0]
    for i in range(1, len(Arr)):
        if (Arr[i] > Max):
            Max = Arr[i]
    return Max

def main():
    No = 0
    Data = list()
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Result = Maximum(Data)

    print("Maximum number is: ", Result)

if __name__ == "__main__":
    main()

