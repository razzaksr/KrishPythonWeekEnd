# single inheritance happens next steps in chain

from demosingle import Traverse

class Finding(Traverse):
    def __mul__(self,data):
        for x in range(len(self.backup)):
            if self.backup[x] == data:
                return x
        return -1
    

# fn=Finding()
# fn>>[87,50,2,54,9.9,0,1,20,6,79.4]
# print(fn)
# print(fn*9.9)