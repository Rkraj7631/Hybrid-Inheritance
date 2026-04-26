class Employee:
    def __init__(self):
        self.name=input("Enter Your Name : ")
        self.salary=int(input("Enter your salary : "))

    def show_Emp(self):
        print(f"Name is : {self.name} ")
        print(f"Salary is : {self.salary}")

class Developers(Employee):
    def __init__(self):
        super().__init__()
        self.language=input("Enter Programming Language Name : ")

    def show_dev(self):
        print(f"Programming Language  : {self.language}")
        
class Managers(Employee):
    def __init__(self):
        super().__init__()
        self.team_size=int(input("How many member in your Team : "))

    def show_manager(self):
        print(f"Team size : {self.team_size}")
        

class TechLead(Developers,Managers):
    def __init__(self):
        super().__init__()

    def show_all(self):
        self.show_Emp()
        self.show_dev()
        self.show_manager()

t=TechLead()
t.show_all()

    
