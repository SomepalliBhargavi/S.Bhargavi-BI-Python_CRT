#constructor without parameter
class Mobile:
    def __init__(self):
        print("Mobile Constructor Called")
realme=Mobile()

class Mobile:
    #constructor without parameter
    def __init__(self):
        self.model='RealMe X'
    def show_model(self):
        print("Model:",self.model)
    def show_version(self):
        print("Version:" ,self.model)
realme=Mobile()
realme.show_model()
realme.show_version()