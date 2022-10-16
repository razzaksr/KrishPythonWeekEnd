'''
def __init__ >> cosntructor
    will be called whenever objects get created to the class
    since constructor executed first than other functions we can use it for following purpose
        1. to perform any important task/process before others
        2. to initialize the class members
'''

class Week:
    def __init__(self):
        print("Hi there!!!!!!!!!!!")
    def solo(self):
        print("Solo Skioa")
    def uce(self):
        print("Jimmy & Jay")
    def best(self):
        print("Ministry of darkness")
        

w1=Week()
w1.best()
#w1.solo()
w1.uce()

class Account:
    
    # constrcutor overloading
    def __init__(self,nm="",num=0,bal=0):
        self.__holder=nm
        self.__number=num
        self.__balance=bal
        
    def __str__(self):
        return self.__holder+" "+str(self.__number)+" "+str(self.__balance)+"\n"
    
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
acc2=Account("Krish",12323651211111,4500.34)


acc1.setHolder("Razak Mohamed S")
acc1.setBalance(2560.5)
acc1.setNumber(987654567654)
# print(acc1.getBalance(),acc1.getHolder(),acc1.getNumber())
print(acc2.getBalance(),acc2.getHolder(),acc2.getNumber())

print(acc1)