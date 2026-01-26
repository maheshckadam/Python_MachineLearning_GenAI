# Accept N numbers from user and store it into List. Return addition of all prime numbers from that List.

import MarvellousNum

def ListPrime(Elements):
    Sum = 0

    for no in (Elements):
        Ret = MarvellousNum.ChkPrime(no)

        if (Ret == True):
            Sum = Sum + no

    return Sum

def main():
    No = 0
    Data = list()
    Value = 0
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Result = ListPrime(Data)

    print("Addition of prime numbers is:", Result)

if __name__ == "__main__":
    main()
