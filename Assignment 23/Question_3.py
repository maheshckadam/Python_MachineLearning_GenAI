class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if (self.Value < 2):
            return False

        for i in range(2, self.Value):
            if (self.Value % i == 0):
                return False

        return True

    def Factors(self):
        print("Factors of", self.Value, "are: ")

        for i in range(1, self.Value + 1):
            if (self.Value % i == 0):
                print(i, end=" ")


    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value):
            if (self.Value % i == 0):
                Sum = Sum + i

        return Sum

    def ChkPerfect(self):
        if (self.SumFactors() == self.Value):
            return True
        else:
            return False


def main():
    No = 0
    No = int(input("Enter number of objects: "))

    for i in range(No):
        Value = int(input("Enter number: "))

        Obj = Numbers(Value)

        print("Prime:", Obj.ChkPrime())
        print("Perfect:", Obj.ChkPerfect())
        Obj.Factors()

        print()

if __name__ == "__main__":
    main()
