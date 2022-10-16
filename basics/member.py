# member operator: in, not in

#list
twoface=[45,9.2,"Wonder woman",False]

print(5 in twoface)

print(False in twoface)

#set
making={
    12,97,45,78,345,123,48,85,5,23,75,4
}

# ask=int(input("Enter the value to check it is part of set "))

# print(ask in making)

#dict
flash={
    "aqua":78,
    "manhunter":8.9,
    "cyborg":(5.6,9.2,129.45,6.1,78.3,1.9,3.1,0.05)#tuple
}

print("batman" in flash)

print(9.2 not in flash['cyborg'])

print(0.1 not in flash['cyborg'])

corporate="Infosys"

print('a' in corporate)
print('i' not in corporate)

print('ys' in corporate)