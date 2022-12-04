'''
overriding: run time polymorphsim
    it happens when inheritance performed
    same method name and paramters is part of two classes which involved in inheritance process
'''

class Santa:
    alpha=[34,99,11,66,45,56,43,3,78,7,65]    
    def hai(self):
        print(self.alpha)

class Travis(Santa):
    def __init__(self):
        self.cosmo={
            "boards":['cbsc','state','matric'],
            "school":"Senthil",
            "address":"Jahir ammapalayam",
            "kms":10
        }
    def hai(self):
        print(self.cosmo)
        super().hai()

# san=Santa()
# san.hai()

# tra=Travis()
# tra.hai()

tr=Travis()
tr.hai()