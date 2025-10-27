# class Cat:
#     def quack(self):
#         print("cat!")

# class Dog(Cat):
#     def quack(self):
#         print("dog!")

# class Duck:
#     def quack(self):
#         print("Quack!")

# def make_it_quack(thing):
#     thing.quack()


# make_it_quack(Dog())
# make_it_quack(Cat())
# make_it_quack(Duck()) 


class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"{self.name} says woof!")

class Human:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"{self.name} says 'I'm pretending to be a duck!'")

def make_it_quack(creature):
    creature.quack()

donald = Duck("Donald")
john = Human("John")
                  
make_it_quack(donald)
make_it_quack(john)

