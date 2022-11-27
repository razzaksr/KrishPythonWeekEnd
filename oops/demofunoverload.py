
class WareHouse:
    def __init__(self):
        self.__store=[12,56,7,35,87,16,80,33,12]
    def __str__(self):
        return str(self.__store)+"\n"
    
    def filter(self,user=0):
        max1,max2=self.__store[0],self.__store[0]
        for x in self.__store:
            if x>max1 and x>user:
                max2=max1
                max1=x
            elif x>max2 and x!=max1 and x>user:
                max2=x
        
        print("max value one is",max1,"and max value 2 is",max2)


war1=WareHouse()
war1.filter()
war1.filter(56)
war1.filter(100)