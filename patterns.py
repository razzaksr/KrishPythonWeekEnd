'''
#####
#####
#####
#####
#####

'''

# for row in range(1,6):
#     for col in range(1,6):
#         print("#",end="")
#     print()


'''
left upper floyd
#
##
###
####
#####
'''    

# for row in range(1,6):
#     for col in range(1,row+1):
#         print("#",end="")
#     print()

'''
left lower floyd
#####
####
###
##
#
'''

# for row in range(5,0,-1):
#     for col in range(1,row+1):
#         print("#",end="")
#     print()

'''
right upper floyd
    #
   ##
  ###
 ####
#####
'''
# for row in range(1,6):
#     for space in range(4,row-1,-1):
#         print(" ",end="")
#     for data in range(1,row+1):
#         print("#",end="")
#     print()

'''
right lower floyd
#####
 ####
  ###
   ##
    #
'''

# for row in range(5,0,-1):
#     for space in range(4,row-1,-1):
#         print(" ",end="")
#     for data in range(1,row+1):
#         print("#",end="")
#     print()

'''
pascal triangle
    #
   # #
  # # #
 # # # #
# # # # #
'''

# for row in range(1,6):
#     for space in range(4,row-1,-1):
#         print(" ",end="")
#     for data in range(1,row+1):
#         print("# ",end="")
#     print()
    
'''
pascal lower triangle
# # # # #
 # # # #
  # # #
   # #
    #
'''

# for row in range(5,0,-1):
#     for space in range(4,row-1,-1):
#         print(" ",end="")
#     for data in range(1,row+1):
#         print("# ",end="")
#     print()

'''
pyramid triangle
  #
 ###
#####
'''

# limit=1

# for row in range(1,6):
#     for space in range(4,row-1,-1):
#         print(" ",end="")
#     for data in range(1,limit+1):
#         print("#",end="")
#     print()
#     limit+=2
    
'''
lower pyramid
#########
 #######
  #####
   ###
    #
'''

limit=9

for row in range(5,0,-1):
    for space in range(4,row-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("#",end="")
    print()
    limit-=2