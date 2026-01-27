import threading

def ChkPrime(No):

    if (No < 2):
        return False

    for i in range(2, No):
        if (No % i == 0):
            return False

    return True

def DisplayPrime(Elements):

    print("Prime numbers are:")
    for no in (Elements):
        if ChkPrime(no):
            print(no)

def DisplayNonPrime(Elements):

    print("Non Prime numbers are:")
    for no in (Elements):
        if not ChkPrime(no):
            print(no)

def main():
    No = 0
    Data = list()
    Value = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements:")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=DisplayPrime, args=[Data])
    t2 = threading.Thread(target=DisplayNonPrime, args=[Data])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()