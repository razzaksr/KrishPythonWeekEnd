# hierarchy inheritance : single base class is parent to two or more derived class

from demosingle import Traverse
from demomultilevel import Finding

class Order(Traverse):
    # OrderObj|1
    def __or__(self,data):
        for pos in range(len(self.backup)-1):
            for choose in range(len(self.backup)-pos-1):
                if data==1:
                    if self.backup[choose]>self.backup[choose+1]:
                        self.backup[choose],self.backup[choose+1]=self.backup[choose+1],self.backup[choose]
                elif data==-1:
                    if self.backup[choose]<self.backup[choose+1]:
                        self.backup[choose],self.backup[choose+1]=self.backup[choose+1],self.backup[choose]


ord1=Order()
ord1>>[87,50,2,54,9.9,0,1,20,6,79.4]
print(ord1)
users=int(input("Tell us order of sorting 1 or -1"))
ord1|users
print(ord1)

fn=Finding()
fn>>[87,50,2,54,9.9,0,1,20,6,79.4]
print(fn)
print(fn*9.9)
