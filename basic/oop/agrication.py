    # loose cuppling:
class Company:
    def __init__(self,location,cname):
        self.cname = cname
        self.location = location

class Employee:
    def __init__(self,name,age,company):
        self.name = name
        self.age = age
        self.company = company

    def display_employee(self):
        return f'My Name Is {self.name},I am {self.age}years old,working in {self.company.cname} at {self.company.location}'

c1 = Company("abc","pmna")
emp=Employee("john",30,c1)
print(emp.display_employee())