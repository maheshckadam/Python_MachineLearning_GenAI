# Display first 10 even numbers on screen.
# Output: 2 4 6 8 10 12 14 16 18 20

def EvenNumbers():
    No = 1
    Count = 0

    while (Count < 10):
        if (No % 2 == 0):
            print(No, end=" ")
            Count = Count + 1
        No = No + 1

def main():
    EvenNumbers()

if __name__ == "__main__":
    main()


