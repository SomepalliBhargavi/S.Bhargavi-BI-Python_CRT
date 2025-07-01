#Multilevel inheritance
class GrandFather():
    def __init__(self):
        pass
    #method overriding-Providing the specific method implementation for the inherited methods from super class to subclass.
                # (within the differnt class having same method and same parameters but differnt implementation).
    @staticmethod
    def Properties():
        print("100 Acres of Land")
class Father(GrandFather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("50 Acres of Land")
class Yourself(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("A Btech Degree")
GrandFather.Properties()
Yourself.Properties()

    