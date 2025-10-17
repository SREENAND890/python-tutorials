class Icar:
    def __int__(self,make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f'Releasd year {self.year}.the brand is {self.make} and model name {self.model} .current price -${self.price}'
    
CC=Icar("englend","ford","1994","540000")
print(type(CC))
    