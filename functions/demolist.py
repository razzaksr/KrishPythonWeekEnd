# list : functions

quick=[89,23,545,34,677,65,53,4,6,78,6]

# adding

quick.append(56)


print(quick[:])
print(quick[::-1])
print(quick[4:10])

quick.insert(3,922)
print(quick)

quick[4]=1200

print(quick)

print(quick.pop(5))

print(quick)

del quick[10]

print(quick[10])

quick.remove(545)

print(quick)

#quick.sort()

print(quick)

quick.reverse()
print(quick)

print(quick.count(65))

print(quick.index(1200))
