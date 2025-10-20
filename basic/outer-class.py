class Engine:
    def __init__(self,ename,cc):
        self.ename=ename
        self.cc=cc

class Car:
    def __init__(self,cname,price,year,ename,cc):
        self.cname=cname
        self.price=price
        self.year=year
        self.engine=Engine(ename,cc)

    def cars(self):
        print(f"name: {self.cname},price: {self.price},year: {self.year},engine-name: {self.engine.ename},engine-cc {self.engine.cc}")

car=Car()