'''write a python program to create an Employee class and declare the states
and create 5 objects using different constructors'''
class Employee:
    #constructor overloading
    def __init__(self,*arg):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        self.Dept=Dept
        print("Hey..!I'm a Six Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job,Salary,Location):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        print("Hey..!I'm a Five Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job,Salary):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        print("Hey..!I'm a Four Parameterized Constructor")
    def __init__(self,EmpName,EmpID,Job):
        self.EmpName=EmpName
        self.EmpID=EmpID
        self.Job=Job
        print("Hey..!I'm a three Parameterized Constructor")
    def __init__(self,EmpName,EmpID):
        self.EmpName=EmpName
        self.EmpID=EmpID
        print("Hey..!I'm a Two Parameterized Constructor")
    def __init__(self,EmpName):
        self.EmpName=EmpName
        print("Hey..!I'm a One Parameterized Constructor")
    def __init__(self):
        print("Hey..!I'm No Parameterized Constructor")
Emp1=Employee()
Emp2=Employee("Scott")
Emp3=Employee("Rose",101)
Emp4=Employee("Jack",102,'HR')
Emp5=Employee("Snow",103,'Data Analyst',25000)
Emp6=Employee("Arya",104,'Developer',30000,'Bengaluru')


    