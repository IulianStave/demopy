class Account:
    def __init__(self, FilePath):
        self.filePath = FilePath
        with open(self.filePath,"r") as file:
            self.balance = int(file.read())
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def checkBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def commit (self):
        with open(self.filePath,"w") as file:
            file.write(str(self.balance))

    def __del__(self):
        pass


myac = Account("iulian.txt")
print (myac.checkBalance())
myac.deposit(20)
myac.deposit(40)
myac.withdraw(7)
myac.withdraw(10)
myac.commit()

print(myac.checkBalance())
lst = []
while (current := input("Write something: ")) != "quit":
    lst.append(current)






        

