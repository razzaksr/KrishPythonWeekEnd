
class Account:
    def setHolder(self,nm=""):self.__holder=nm
    def getHolder(self):return self.__holder
    def setNumber(self,num=0):self.__number=num
    def getNumber(self):return self.__number
    def setBalance(self,bal=0.0):self.__balance=bal
    def getBalance(self):return self.__balance
    
    def deposite(self,amt=0):
        self.__balance+=amt
        print(amt,"has deposited in",self.__number,"by",self.__holder)


acc1=Account()
acc1.setHolder("Razak Mohamed S")
acc1.setBalance(2560.5)
acc1.setNumber(987654567654)
# acc1.holder="Razak Mohamed S"
# acc1.balance=2560.4
# acc1.number=98765678765

acc1.deposite(500)
#print(acc1.__balance)
#print(hasattr(acc1,"__balance"))
print(acc1.getBalance())


acc2=Account()
acc2.setHolder("Krish")
acc2.setBalance(10453.9)
acc2.setNumber(8765456755645)
# acc2.holder="Krish"
# acc2.number=876545678678
# acc2.balance=8740.1

acc2.deposite(10000)