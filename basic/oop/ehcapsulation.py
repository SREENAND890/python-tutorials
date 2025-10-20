class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    
    def display(self):
        return f'{self.name},{self.__salary}'
    
    def update_salary(self,update):
        self.__salary =update
    
emp=Employee('john',30000)
print(emp.display())
# print(emp.__salary)
emp.name="alice"
# emp.__salary = 50000
# print(emp.display())

# print(emp.__salary)
# print(emp.display())

emp.update_salary(50000)
print(emp.display())







