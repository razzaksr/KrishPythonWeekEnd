'''

User defined functions:
    def fun_name(parameters):
        function_body
        reusable code 
        return data


search operations:
    linear>> visiting every index value til end to match with user given value
    binary>> unlike linear it will search dynamic range, not always search from 0 to end, since
                it will search only on sorted list

'''

hai=[23,67,343,89,87,35,677,45]

def linear(data):
    for x in range(len(hai)):
        if hai[x]==data:
            return x
    else:
        return -1

def selection():
    for hold in range(len(hai)):
        for comp in range(hold+1,len(hai)):
            if hai[hold]<hai[comp]:
                hai[hold]^=hai[comp]
                hai[comp]^=hai[hold]
                hai[hold]^=hai[comp]

# inbuilt search function
# print(hai.index(343))

# print(linear(11))
# print(linear(23))
# print(linear(45))
# print(linear(677))

# print(hai)
# selection()
# print(hai)

def display(start=0,end=len(hai)):
    print("Printing values from",start,"to",end)
    for pos in range(start,end):
        print(hai[pos],end=" ")
    print()
    
display()
display(3,7)
display(4) #start
display(end=5)
display(end=6,start=3)