#single Inheritance
class Vehicle:
    def __init__(self):
        print("I'm the Vehicle class constructor")
    @staticmethod
    def Start():
        print("Vehicle is started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the car class constructor")
    @staticmethod
    def Start():
        print("Car is started")
C1=Car()
C1.Start()
