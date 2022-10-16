'''
Looping statements:
    repeataion to ignore rewrite same statement multiple times
    series, patterns, real time process
    
    attributes:
        loop control var/obj
            start       initialization
            end         condition
            step up     iteration
    types:
        while
        for>> for in range
           >> for in
'''

# for point in "krish":
#     print(point)

# yet={1200,"Razak",9.2,679.4,False}
# for p in yet:
#     print(p)

tup=(1200,4500.3,"Razak","Zealous",True)
# for q in tup:print(q)
# pos=0
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=2
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1

# pos=0
# while pos<len(tup)-2:
#     print(tup[pos])
#     pos+=1

# for index in range(len(tup)):
#     print(tup[index])

# for index in range(len(tup)-2):
#     print(tup[index])

# for index in range(2,len(tup)-1):
#     print(tup[index])

for index in range(len(tup)-1,-1,-1):
    print(tup[index])

# for var in range(start,condition,iter):
    # loop ends before condition step
    # default iteration is +1
    # default initialization is 0
# for hai in range(1,101,+1):
#     print(hai)

# for hai in range(1,101):
#     print(hai)

# for hai in range(1,101,+2):
#     print(hai)

# for hai in range(100,2,-1):
#     print(hai)

# for hai in range(101):
#     print(hai)

# fibonacci series: 0 1 1 2 3 5 8 13 21 34 55 
# end=int(input("tell us how many digits you want in the series "))#10
# num1,num2=0,1
# if end>=2:
#     print(num1)
#     print(num2)
#     for steps in range(3,end+1):
#         sum=num1+num2
#         print(sum)
#         num1=num2
#         num2=sum
# else:
#     print("fibonacci wouldn't come")


# sale
#stock=30
# for stock in range(5,0,-1):
#     amt=int(input("enter the amount to purchase "))
#     if amt>=10000:
#         print("stock quantity one has purchased")
#         stock-=1
#     else:
#         print("insufficient amount to purchase")

# stock=5
# while stock>0:
#     amt=int(input("enter the amount to purchase "))
#     if amt>=10000:
#         print("stock quantity one has purchased")
#         stock-=1
#     else:
#         print("insufficient amount to purchase")


# # 1,2,3,4,...100

# num=1# init
# while num<=100:# cond
#     print(num)
#     num+=1# iter

# # 1,3,5,...99

# num=1# init
# while num<=100:# cond
#     print(num)
#     num+=2# iter

# # 2,4,...100

# num=2# init
# while num<=100:# cond
#     print(num)
#     num+=2# iter

# odd/even through condition: series
# current=1
# while current <= 200:
#     if current%2==0:
#         print(current)
#     current+=1

# # prime series within user given range
# stand=int(input("Tell us start point to find prime "))
# end=int(input("tell us end point "))
# while stand<=end:
#     if stand==2 or stand==3 or stand==5 or stand==7 or stand%2!=0 and stand%3!=0 and stand%5!=0 and stand%7!=0:
#         print(stand)
#     stand+=1

# cash withdrawls
# availableCash=46000
# withdrawls=0
# while availableCash>0:
#     requiredCash=int(input("tell us required amount "))
#     if requiredCash<=availableCash:
#         availableCash-=requiredCash
#         withdrawls+=1
#     else:
#         print("available is",availableCash)
# else:
#     print("totally",withdrawls,"happened")