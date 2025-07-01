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
    def Display(self):
        #to print from top to bottom
        self.Stack.reverse()
        Str=[]
        for i in self.Stack:
            Str.append(i)
        Rev_Str="".join(Str)
        print(Rev_Str)
    def Check_Balence(self):
        if '([{' in self.Stack:
            if self.stack[3:]=='{[(':
                print("Balanced Paranthesis")
        elif '({['== self.Stack:
            if self.stack[3:]==']})':
                print("Balenced Paranthesis")
    


stack=Stack()
stack.push('([{}])')
stack.push('({[]})')
stack.push('{[()]}')
stack.push('{}')
