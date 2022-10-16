from array import *

myObj=array('d',[])

myObj.append(3.4)
myObj.append(9.1)

print(myObj)

myObj.append(True)
#myObj.append("Razak")

print(myObj)

myObj.insert(1,0.3)

print(myObj)

# slicing
print(myObj[:])
print(myObj[::-1])
print(myObj[:2])
print(myObj[3:])

# update
myObj[2]/=2;

print(myObj)

# remove
myObj.pop(1)
myObj.remove(4.55)
del myObj[1]
print(myObj)
