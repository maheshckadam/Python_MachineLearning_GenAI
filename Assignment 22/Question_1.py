class Demo:
    Value = 0 

    def __init__(self, No1, No2):
        self.No1 = No1 
        self.No2 = No2 

    def Fun(self):
        print("Fun Method - No1: ", self.No1, "No2: ", self.No2)

    def Gun(self):
        print("Gun Method - No1: ", self.No1, "No2: ", self.No2)

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()