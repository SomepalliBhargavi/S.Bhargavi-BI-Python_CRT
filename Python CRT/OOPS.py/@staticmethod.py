'''static-single copy for entire class'''
class Mobile:
    def __init__(self):
        print("Object is created")
    @staticmethod
    def Display():
        print("I'm a class method")
        print("I will work irrespective of object creation")
Mobile.Display()
