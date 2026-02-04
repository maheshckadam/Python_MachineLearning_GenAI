def main():
    try:
        FileName = input("Enter the file name: ")

        fobj = open(FileName, "r")
        print("File gets successfully open.")

        Data = fobj.read()

        print("Data from file is: ", Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file.")
    finally:
        print("End Of Application")


if __name__ == "__main__":
    main()
