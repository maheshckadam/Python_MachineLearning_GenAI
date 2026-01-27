class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number: "))
        self.Value2 = int(input("Enter Second Number: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if (self.Value2 == 0):
            return "Error : Division by zero"
        else:
            return self.Value1 / self.Value2

    def Display(self):
        print("Addition is:", self.Addition())
        print("Subtraction is:", self.Subtraction())
        print("Multiplication is:", self.Multiplication())
        print("Division is:", self.Division())


def main():
    No = 0
    No = int(input("Enter number of objects: "))

    for i in range(No):
        print("Object", i + 1)

        Obj = Arithmetic()

        Obj.Accept()
        Obj.Display()

if __name__ == "__main__":
    main()
