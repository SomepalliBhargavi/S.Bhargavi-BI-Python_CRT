'''classmethod-which act upon the class variables'''
class Mobile:
    def __init__(self):
        print("Object is created")
    @classmethod
    def Display(Class):
        print("I'm a class method")
        print("I will work irrespective of object creation")
Mobile.Display()
M1=Mobile()
M1.Display()