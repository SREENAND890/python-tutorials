class Engine:
    def start_engine(self):
        print("Engine Started")

class Wheel:
    def rotate(self):
        print("wheels rotating")

class Car(Engine,Wheel):
    def Drive(self):
        print("car driving")

car = Car()
car.start_engine()
car.rotate()
car.Drive()