# Accepts length and width of rectangle and prints area.

def AreaOfRectangle(Length, Width):
    Area = Length * Width
    return Area

def main():
    Len = 0
    Wid = 0
    Result = 0

    Len = int(input("Enter Length: "))
    Wid = int(input("Enter Width: "))

    Result = AreaOfRectangle(Len, Wid)

    print("Area of rectangle is:", Result)

if __name__ == "__main__":
    main()
