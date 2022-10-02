# tuple: inbuilt functions
# fixed size: can't increase or decrease the size

wind=('razak',45,5.6,False,"Zealous",45,False,5)

print(type(wind))

print(wind)

print(wind[1])

#del wind[1]

#wind.append(34)

# slicing: extraction elements between specified positions
# obj[start:end:forward/backward]

# extract all
print(wind[:])

# extract in reverese
print(wind[::-1])

# exactraqct specified positions
print(wind[2:4])

# index, count

# searching the object for position
print(wind.index(45))

#count of occurance
print(wind.count(False))
print(wind.count(5.6))
print(wind.count(45))