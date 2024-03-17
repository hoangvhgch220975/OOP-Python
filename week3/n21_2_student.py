from pyclbr import Class


class Student:
    def __init__(self, id, name , gpa):
        self.__id = id
        self.__name = name
        self.__gpa = gpa
    
    def show(self):
        print(f'| Student ID: {self.__id} | Name: {self.__name} | GPA: {self.__gpa} ')

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        if gpa == '':
            print('GPA cannot be empty')
            return
        self.__gpa = gpa
        print(f'{self.__name} GPA has change to {gpa}')

John = Student('1','John','4')
John.show()

John.set_gpa(1.1)
John.show()


class Classroom:
    def __init__(self,name):
        self.__name = name
        self.__students = []

    def get_name(self):
        return self.__name
    
    def add_student(self, student):
        self.__students.append(student)
        print(f'Student {student.get_name()} added to the classroom')

    def remove_student(self, id):
        for e in self.__students:
            if e.id == id:
                self.__students.remove(e)
                print(f'Student {e.get_name()} removed from the classroom')
                return
        print(f'Student {e.get_name()} not found in the clasroom')

    def best_student(self):
        if not self.__students:
            print('No student in class')
            return
        best_student = self.__students[0]
        for student in self.__students:
            if student.get_gpa() > best_student.get_gpa():
                best_student = student
        print(f'The best student is {best_student.get_name()} with GPA {best_student.get_gpa()}')
        return best_student
    def avg_gpa(self):
        if len(self.__students) == 0:
            print('No student in the class')
            return
        sum_gpa = 0
        for s in self.__students:
            sum_gpa += float(s.get_gpa())
        
        return sum_gpa/ len(self.__students)
    
    def show(self):
        print(f'Classroom: {self.__name}')
        print('Student: ')
        for e in self.__students:
            e.show()
        print(f'Averager GPA: {self.avg_gpa()}')
        
John = Student('1','John','4')
Paul = Student('2','Paul','3')
Mike = Student('3','Mike','3.5')
ALice = Student ('4','Alice','3.8')



apple = Classroom('Apple')
apple.add_student(John)
apple.add_student(Paul)
apple.add_student(Mike)
apple.add_student(ALice)


apple.show()
apple.best_student()
