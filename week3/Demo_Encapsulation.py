from hmac import new


class Employee:
    def __init__(self, name, salary, years):
        self.__name = name
        self.__salary = salary
        self.__years = years
    
    def show(self):
        print(f'| Name: {self.__name} | Salary: {self.__salary} | Experience: {self.__years} years')

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
            return
        self.__name = name

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary < 0:
            print('Salary cannot be negative')
            return
        self.__salary = salary

    def get_year(self):
        return self.__years
    
    def set_year(self, years):
        if years < 0:
            print('Experience year cannot be negative')
            return
        self.__years = years

John = Employee('John',2000,1)
John.show()

John.set_name('Paul')
John.set_salary(500000)
John.set_year(10)

John.show()

John.set_name('')
John.set_salary(-200000)
John.set_year(-5)

John.show()


John.__years = 5 # it is not the same as self.__years
John.show()


class Company:
    def __init__(self, name):
        self.__name = name
        self.__employees = []
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name == '':
            print('Name cannot be empty')
            return
        self.__name = name

    def add_employee(self, employee):
        self.__employees.append(employee)
        print(f'Employee {employee.get_name()} added to the company')

    def remove_employee(self, name):
        for e in self.__employees:
            if e.name == name:
                self.__employees.remove(e)
                print(f'Employee {name} removed from the company')
                return
        print(f'Employee {name} not found in the company')

    def show(self):
        print(f'Company: {self.__name}')
        print('Employee: ')
        for e in self.__employees:
            e.show()

    def raise_salary(self, employee, amount):
        old_salary = employee.get_salary()
        new_salary = old_salary + amount
        employee.set_salary(new_salary)



John = Employee('John', 60000, 5)
Paul = Employee('Paul', 40000, 3)
Mike = Employee('Mike', 50000, 4)
ALice = Employee ('Alice', 20000,1)



apple = Company('Apple')
apple.add_employee(John)
apple.add_employee(Paul)
apple.add_employee(Mike)
apple.add_employee(ALice)

apple.raise_salary(John, 10000)

apple.show()
