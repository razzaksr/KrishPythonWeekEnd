'''
Nested loop

loop1:
    body of loop1
    loop2:
        body of loop2

'''

chart=""

for rows in range(1,4):
    for seat in range(1,5):
        amount=int(input("enter the amount to book ticket "))
        if amount>=450:
            print("Happy journey @ seat number",seat,"@ row",rows)
            chart+="$"
        else:
            print("insufficient to travel")
            chart+="@"
        if seat==2:chart+=" "
    chart+="\n"

print(chart)

# for cabin in range(1,4):
#     print("cabin number",cabin)
#     seat=1
#     while seat<=4:
#         age=int(input("tell us age "))
#         if age>=18 and age<=60:
#             print("enjoy the ride")
#             seat+=1
#         else:
#             print("we regret not to let you")

# for cabin in range(1,4):
#     print("cabin number",cabin)
#     for seat in range(1,5):
#         age=int(input("tell us age "))
#         if age>=18 and age<=60:
#             print("enjoy the ride")
#         else:
#             print("we regret not to let you")

# for tab in range(1,11):
#     print("Table",tab)
#     for num in range(1,11):
#         print(num,"X",tab,"=",(tab*num))