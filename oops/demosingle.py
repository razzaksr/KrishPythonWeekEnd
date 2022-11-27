'''
inheritance:
    using an object to access not only own class members but another class members too
    copying one class members to another class
    
    syntax:
        class Derived(BaseClass):
            
'''

class Monitor:
    def __init__(self):
        self.backup=[]
    
    def __rshift__(self,one=[]):
        self.backup=one
    
    def __lshift__(self,ref):
        return self.backup

# single inheritance
class Traverse(Monitor):
    def __str__(self):
        return str(self.backup)
    
    

# mon=Monitor()
# mon>>[45,89,12,90,45,25,7,65]
# print(mon<<mon)

# mon=Traverse()
# mon>>[45,89,12,90,45,25,7,65]
# print(mon)