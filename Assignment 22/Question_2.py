class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.Area = (Circle.PI) * (self.Radius * self.Radius)

    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI) * (self.Radius)

    def Display(self):
        print("Radius is: ", self.Radius)
        print("Area is: ", self.Area)
        print("Circumference is: ", self.Circumference)


def main():
    No = 0
    No = int(input("Enter number of circles: "))

    for i in range(No):
        print("Circle", i + 1)

        Obj = Circle()

        Obj.Accept()
        Obj.CalculateArea()
        Obj.CalculateCircumference()
        Obj.Display()

if __name__ == "__main__":
    main()
