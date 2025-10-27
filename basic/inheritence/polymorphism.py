class Animal:
    def speak(self):
        return "The animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

animals = [Dog(), Cat()]

for a in animals:
    make_animal_speak(a)
