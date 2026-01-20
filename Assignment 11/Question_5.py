# Accept one number and check whether it is palindrome or not
# Input: 121
# Output: Palindrome

def CheckPalindrome(Value1):
    Rev = ""

    for ch in (Value1):
        Rev = ch + Rev

    if (Value1 == Rev):
        return True
    else:
        return False

def main():
    No1 = 0
    Result = False

    No1 = input("Enter number: ")
    Result = CheckPalindrome(No1)

    if (Result == True):
        print("Input is Palindrome Number")
    else:
        print("Input is Not Palindrome Number")

if __name__ == "__main__":
    main()

