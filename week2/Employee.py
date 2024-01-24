class Employee:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years
    
    def show(self):
        print(f'| Name: {self.name} | Salary: {self.salary} | Experience: {self.years} years')


John = Employee('John','2000','1')
John.show()