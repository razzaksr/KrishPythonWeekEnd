# set : functionalities

alpha={120,"Razak",5,2.3,False,98.5,True}

# slicing: not allowed here
# no index based operations in set: read, slicing, loop

print(alpha)

alpha.add("Zealous")

print(alpha)

alpha.pop()

print(alpha)

alpha.remove(120)

hi=tuple(alpha)
for x in hi:print(x,end="")

