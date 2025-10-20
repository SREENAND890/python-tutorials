class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    
    def StudentGrade(self):
        if self.marks >= 90:
            print("A+")
        elif self.marks >= 82 :
            print("A")
        elif self.marks >= 76 :
            print("B+")
        elif self.marks >= 70 :
            print("B")
        elif self.marks >= 64 :
            print("C+")
        elif self.marks >= 56 :
            print("C")
        elif self.marks >= 40 :
            print("D+")
        elif self.marks >= 30 :
            print("D")
        else:
            print("fail")

std1=Student("john",89.0)
std2=Student("alice",77.5)
print(std1.StudentGrade())
print(std2.StudentGrade())
        
