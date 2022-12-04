'''
abstraction:
    a function without logic/body/definition
    rather it contains keyword "pass"
    abstract function logic/body/definition will be wriiten in the derived class
    override mandate when you inherite a class which contains abstract function
    abc module will let us to create abstract class which allow us to write abstract function
    cannot create object to abstract class
'''

from abc import *

class Falcon(ABC):
    def __init__(self):
        self.mine={78,33,10,40,923,42,56,5,75,477,3,56}
    #abstract function        
    def heyThere(self):
        pass
    

class Winter(Falcon):
    def heyThere(self):
        print(self.mine)


win=Winter()
win.heyThere()