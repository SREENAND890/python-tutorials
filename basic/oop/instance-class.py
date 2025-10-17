class Employee:

    company="Softronics"

    def __init__(self,name,position):
        self.name = name
        self.position = position


emp1=Employee("John","Teacher")
emp2=Employee("Alice","Student")

print(emp1.company)
print(emp2.company)
        