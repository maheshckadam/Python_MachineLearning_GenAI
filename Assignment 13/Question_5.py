# Accepts marks and displays grade.

def DisplayGrade(Marks):
    if (Marks >= 75):
        return "Distinction"
    elif (Marks >= 60):
        return "First Class"
    elif (Marks >= 50):
        return "Second Class"
    else:
        return "Fail"

def main():
    mar = 0
    Result = ""

    mar = int(input("Enter marks: "))
    Result = DisplayGrade(mar)

    print("Grade is: ", Result)

if __name__ == "__main__":
    main()
