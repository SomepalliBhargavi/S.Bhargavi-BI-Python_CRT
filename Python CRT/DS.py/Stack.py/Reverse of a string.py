class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} Element is Appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self,data):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print(f"{data} Element is removed")
    def peek(self):
        Len=len(self.Stack)
        print(f"Peek element is {self.Stack[Len-1]}")
    def Display(self):
        #to print from top to bottom
        self.Stack.reverse()
        Str=[]
        for i in self.Stack:
            Str.append(i)
        Rev_Str="".join(Str)
        print(Rev_Str)

stack=Stack()
stack.push('c')
stack.push('o')
stack.push('d')
stack.push('i')
stack.push('n')
stack.push('g')
stack.Display()