# odd  or even

# number=int(input("Enter the number "))

# print("Is entered number is even",(number%2==0))
# print("Is entered number is odd",(number%2!=0))

# prime number: 2, 3, 5, 7

userIn=int(input("Tell us number to find prime "))

print("Is entered number",userIn,"is prime?",
      (userIn==2 or userIn==3 or userIn==5 or userIn==7
       or userIn%2!=0 and userIn%3!=0 and userIn%5!=0 and userIn%7!=0))
