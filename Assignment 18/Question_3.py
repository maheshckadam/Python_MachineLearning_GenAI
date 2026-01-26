# Accept N numbers from user and store it into List. Return Minimun number from that List.
# Input: 4, Elements = 13 5 45 7
# Output: 5

def Minimum(Arr):

    Min = Arr[0]
    for i in range(1, len(Arr)):
        if (Arr[i] < Min):
            Min = Arr[i]
    return Min

def main():
    No = 0
    Data = list()
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Result = Minimum(Data)

    print("Minimum number is: ", Result)

if __name__ == "__main__":
    main()

