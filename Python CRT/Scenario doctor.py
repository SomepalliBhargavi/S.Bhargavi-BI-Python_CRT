'''1.Create a 'Person' class that serves as a base class for both doctors and 
pateints.This class should contain:
-Name
-Age
-Gender
-A method to return formatted personal details
2.Create  a 'Pateint' class** that inherits from 'person' and includes:
-Disease information
-A method to return full pateint details
3.Create a 'Doctor' class that inherits from person and includes:
-Methods to assign a pateint,retrieve details and list assigned
'''

class Person:
    def __init__(self,name,age,gender):
        self.Name=name
        self.Age=age
        self.Gender=gender
        print("Super Class Constructor")
    def Details(self):
        print(f"Person's Name :{self.Name}")
        print(f"Person's Age :{self.Age}")
        print(f"Person's Gender :{self.Gender}")
class Patient(Person):
    def __init__(self, name, age, gender,disease):
        super().__init__(name, age, gender)
        self.Disease=disease
    def Details(self):
        print(f"Patient's Name :{self.Name}")
        print(f"Patient's Age :{self.Age}")
        print(f"Patient's Gender :{self.Gender}")
        print(f"Disease Description :{self.Disease}")
class Doctor(Person):
    def __init__(self, name, age, gender,specialization):
        super().__init__(name, age, gender) 
        self.Specialization=specialization
        self._patients=[]
    def assign_patient(self,patient):
        self._patients.append(patient)
    def get_doctor_details(self):
        return f"{self.get_details()},specialization:{self.Specialization}"
    def get_assigned_patients(self):
        if not self._patients:
            return "No patients assigned."
        result=""
        for p in self._patients:
            result+=f"-{p.name} ({p.disease})\n"
        return result.strip()
doctors=[]
patients=[]
def find_doctor_by_name(name):
    for doc in doctors:
        if doc.name.lower() == name.lower():
            return doc
    return None
def find_patient_by_name(name):
    for pat in patients:
        if pat.name.lower() == name.lower():
            return doc
    return None
def main():
    while True:
        print("\n---Hospital Management System---")
        print("1.Register Doctor")
        print("2.Register Patient")
        print("3.Assign Patient to Doctor")
        print("4.View Doctor and Assigned Patients")
        print("5.View Patient Details")
        print("6.Exit")
        choice=input("Enter your choice (1-6): ")

        if choice=='1':
            name=input("Doctor Name: ")
            age=int(input("Doctor Age :"))
            gender=input("Doctor Gender: ")
            specialization=input("Specialization: ")
            doc=Doctor(name,age,gender,specialization)
            doctors.append(doc)
            print("Doctor registered successfully.")

        elif choice=='2':


       
        

        