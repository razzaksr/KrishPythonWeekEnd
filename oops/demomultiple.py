# multiple : one derived may have more than one parent/base class

class Subject:
    def __init__(self):
        self.name=""
        self.units=0
        self.marks=0
        self.scored=0
    def __str__(self):
        return "Name of the subject "+self.name+"\nUnits in the subject "+str(self.units)+"\nTotal marks "+str(self.marks)+"\nScored mark "+str(self.scored)+"\n"
        
        
class Student:
    def __init__(self):
        self.portion=[]
    def __str__(self):
        for x in self.portion:
            print(x)
        return ""
            
class Exam(Student,Subject):
    def __lshift__(self,obj):
        self.portion.append(obj)
        print(obj.name+" has added in the syllabus")
    def addMarks(self):
        for x in range(len(self.portion)):
            mk=int(input("Enter the score for "+self.portion[x].name))
            self.portion[x].scored=mk


sb1=Subject()
sb1.name="Maths"
sb1.marks=100
sb1.units=9

sb2=Subject()
sb2.name="Physics"
sb2.marks=100
sb2.units=4


sb3=Subject()
sb3.name="Chemistry"
sb3.marks=100
sb3.units=5


sb4=Subject()
sb4.name="Biology"
sb4.marks=100
sb4.units=4


ex1=Exam()

ex1<<sb1
ex1<<sb2
ex1<<sb3
ex1<<sb4

print(ex1)

ex1.addMarks()

print(ex1)