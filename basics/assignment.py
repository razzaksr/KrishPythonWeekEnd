# assignment/ shorthand: += -= *= /= //= %=

# eg: data1=data1+data2 >> data1+=data2

# eg: data2=data1+data2 >> can't use shorthand

# atm deposite

# account={
#     "number":8765678945,
#     "holder":"krish",
#     "balance":34000.56,
# }

# userIn=int(input("tell us amount to deposite "))

# account['balance']+=userIn

# print(userIn,"has deposited,so available is",account['balance'])

# theatre ticket counter

# count=int(input("Tell us no of tickets you required "))

# payable=count*120;

# print(payable,"amount to be payable for",count,"tickets")


donut,eclairs=3.4,8.1
print("donut has",donut,",eclairs has",eclairs)

# #swap using third variable
# krish=donut
# donut=eclairs
# eclairs=krish

# swap using + -
# donut+=eclairs
# eclairs=donut-eclairs
# donut-=eclairs

# swap  using * /
# donut*=eclairs
# eclairs=donut/eclairs
# donut/=eclairs

donut,eclairs=eclairs,donut


print("donut has",donut,",eclairs has",eclairs)