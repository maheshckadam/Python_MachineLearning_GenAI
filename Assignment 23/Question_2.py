class BankAccount:

    ROI = 10.5 

    def __init__(self, Name, Amount):

        self.Name = Name
        self.Amount = Amount

    def Display(self):

        print("Account Holder Name: ", self.Name)
        print("Current Balance: ", self.Amount)

    def Deposit(self):

        DepAmt = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + DepAmt
        print("Amount deposited successfully")

    def Withdraw(self):

        WithAmt = float(input("Enter amount to withdraw: "))

        if (WithAmt <= self.Amount):
            self.Amount = self.Amount - WithAmt
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):

        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():

    Obj1 = BankAccount("Mahesh", 5000)
    Obj2 = BankAccount("Umesh", 10000)

    print("Account 1 Details: ")
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    Interest = Obj1.CalculateInterest()
    print("Interest is: ", Interest)
    print()

    print("Account 2 Details: ")
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Interest = Obj2.CalculateInterest()
    print("Interest is: ", Interest)

if __name__ == "__main__":
    main()
