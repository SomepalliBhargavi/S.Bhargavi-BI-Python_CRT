class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is created")
        self.EmpName=empname
        self.EmpID=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
def Display_Details(self):
    print("Details of Employee :")
    print(f"Employee Name : {self.EmpName}")
    print(f"Employee ID : {self.EmpID}")
    print(f"Employees's designation :{self.Designation}")
    print(f"Employees's salary : {self.Salary}")
    print(f"Employee's DeptName : {self.DeptName}")
E1=Employee("Scott",'EMP101','Data Analyst',25000,'DeploymentTeam')
Display_Details(E1)