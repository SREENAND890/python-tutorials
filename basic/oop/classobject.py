class Car:
    def __int__(self,make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        return f'{self.year} {self.make} {self.model} -${self.price}'

car1 = Car("toyota","camery","2017","540000")
print(car1.display_info())
car2 = Car("ford","endeavour","2019","12000")
print(car2.display_info())

