# class Employee:
#     class Compeny:
#         def __init__(self,cname,location):
#             self.cname = cname
#             self.location = location

#     def __init__(self,name,salary,cname,location):
#         self.name = name
#         self.salary =salary
#         self.compeny=Employee.Compeny(cname,location)

#     def display_employee(self):
#         print(f"name: {self.name}, Salary: {self.salary},Compeny: {self.compeny.cname} ,Location:{self.compeny.location}")

# emp= Employee("John",50000,"softronics","kozhikkode")
# emp.display_employee()
# emp.compeny.cname="liminar techonology"
# emp.compeny.location="kochi"
# emp.display_employee()



class Employee:
    def __init__(self,cname,location):
        self.cname = cname
        self.location = location

class Compeny:
    def __init__(self,name,salary,cname,location):
        self.name = name
        self.salary =salary
        self.compeny=Employee(cname,location)

    def display_employee(self):
        print(f"name: {self.name}, Salary: {self.salary},Compeny: {self.compeny.cname} ,Location:{self.compeny.location}")

emp =Compeny("John",50000,"softronics","kozhikkode")
emp.display_employee()
        

        


