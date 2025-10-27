class Animal:
    def animel(self):
        print(f"{self} make a sound")
class Dog(Animal):
    def dog(self):
        print(f"{self} make large sound")

class Cat(Dog):
    def cat(self):
        print(f"{self} crying")

ADC = Cat()
ADC.animel()
ADC.dog()
ADC.cat()