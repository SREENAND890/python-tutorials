class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Pet:
    def cuddle(self):
        print("Pet loves cuddles")

class Puppy(Dog, Pet):
    def play(self):
        print("Puppy plays")

class TrainedPuppy(Puppy):
    def perform(self):
        print("Trained Puppy performs tricks")

tp = TrainedPuppy()
tp.speak()
tp.bark()
tp.cuddle()
tp.play()
tp.perform()
