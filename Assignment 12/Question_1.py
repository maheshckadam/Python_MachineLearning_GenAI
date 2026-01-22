# Accept one character and check whether it is vowel or consonant.
# Input: a
# Output: Vowel

def CheckVowel(ch):
    if (ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
        return True
    else:
        return False

def main():
    Char = ""
    Result = False

    Char = input("Enter Character: ")

    Result = CheckVowel(Char)

    if (Result == True):
        print("Input is Vowel")
    else:
        print("Input is Consonant")

if __name__ == "__main__":
    main()
