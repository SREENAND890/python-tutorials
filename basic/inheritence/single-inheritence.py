class Dog:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f'{self.name} make a sound!...')
        
class Animal(Dog):
    def speak(self):
        print(f"{self.name} woof!...")

dog=Dog("Bob")
