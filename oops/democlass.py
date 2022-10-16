from array import *

class Krish:
    hi=array('i',[34,89,12,45,11,9,5,20])
    say=55

    def select(self):
        for hold in range(len(self.hi)):
            for comp in range(hold+1,len(self.hi)):
                if self.hi[hold]>self.hi[comp]:
                    self.hi[hold]^=self.hi[comp]
                    self.hi[comp]^=self.hi[hold]
                    self.hi[hold]^=self.hi[comp]
                    
                    
# syntax: object=Classname()

h=Krish()

print(h.hi,"and say value is",h.say)
h.select()
h.say=10
print(h.hi,"and say value is",h.say)


z=Krish()
print(z.hi,"and say value is",z.say)