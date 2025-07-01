#single Inheritance
class Father:
    def __init__(self):
        pass
    @staticmethod
    def work():
        print("Hardworking Father")
class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def work():
        print("Enjoying son")
Father.work()
Son.work()