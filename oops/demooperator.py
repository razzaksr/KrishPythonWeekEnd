# operator overloading

print(12+45)

print("hai"+"hello")

class Alphabetz:
    def __init__(self,a=0,b=0):
        self.donut=a
        self.froyo=b
    
    def __str__(self):
        return str(self.donut)+" "+str(self.froyo)+"\n"
    
    def __add__(self, ref):
        self.donut*=ref.donut
        self.froyo/=ref.froyo
        
    def __lshift__(self,num):
        self.donut+=num
        self.froyo+=num
        
    def __sub__(self,ref):
        tmp=Alphabetz()
        tmp.donut=self.donut^ref.donut
        tmp.froyo=self.froyo&ref.froyo
        return tmp
    

ab1=Alphabetz(78,100)
ab2=Alphabetz(256,32)

ab3=ab1-ab2

print(ab3)

print(ab1,ab2)

ab1+ab2

print(ab1,ab2)

ab2<<5

print(ab2)