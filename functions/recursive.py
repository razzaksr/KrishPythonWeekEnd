'''

Recursive function:
    like other's it should call once by caller
    
    once caller has called the function it will keep on calling itself 
    again and again from the function body itself
    until some condition get matches
    
    

'''

def hiThere():
    print("Hi there!!!!!!!!")
    hiThere() # recursive
    
def meetNEat(limit=10):
    if limit>0:
        print("Calling attendance",limit)
        limit-=1
        meetNEat(limit)
        
hai=[23,67,343,89,87,35,677,45]
        
def display(start=0,end=len(hai)):
    print("Printing values from",start,"to",end)
    for pos in range(start,end):
        print(hai[pos],end=" ")
    print()

def iterate(start=0,end=len(hai)):
    if start<end:
        print(hai[start])
        start+=1
        iterate(start,end)
    
# display(1,5)
#iterate()
#iterate(2,5)
iterate(end=8,start=3)

#caller called once
# hiThere()
# meetNEat()
# meetNEat(50)

