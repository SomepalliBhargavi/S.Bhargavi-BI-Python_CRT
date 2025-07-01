class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a graduate now")
#First sub class
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a computer science graduate ")
#Second Sub class
class BioInformatics(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a Bioinformatics graduate")
#Third sub class
class ECE(Graduation):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Graduate():
        print("Congratulations you are a ECE graduate")
Graduation.Graduate()
CSE.Graduate()
BioInformatics.Graduate()
ECE.Graduate()



