
from n21_2_student import Student, Classroom 

class ClassManager:
    def __init__(self):
        name = input('Enter the name of the class: ')
        self.__room = Classroom(name)

    def run(self):
        while True:
            self.print_menu()
            choice = int(input('Enter your option: '))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.remove_student()
            elif choice == 3:
                self.show_student()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print('Quit')
                break
            else: 
                print('Invalid choice, try again! ')
    
    def print_menu(self):
        print(f' Class Manager for {self.__room.get_name}')
        print('1. Add Student')
        print('2. Remove Student')
        print('3. Show Students')
        print('4. Show Scores')
        print('5. Quit')

    def add_student(self):
        id = int(input('ID: '))
        name= input('Name: ')
        gpa = float(input('GPA: '))
        s = Student(id, name, gpa)
        self.__room.add_student(s)

    def remove_student(self):
        id = int(input('ID'))
        self.__room.remove_student(id)

    def show_student(self):
        self.__room.show()

    def show_score(self):
        pass

program = ClassManager()
program.run()