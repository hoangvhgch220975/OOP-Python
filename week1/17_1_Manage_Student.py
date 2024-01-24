ids = []
names =[]
grades = []


def main():
    running = True
    while running:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student(ids, names, grades)
        elif choice == 2:
            edit_student(ids, names, grades)
        elif choice == 3:
            delete_student(ids, names, grades)
        elif choice == 4:
            seach_student(ids, names, grades)
        elif choice == 5: 
            show_all(ids, names, grades)
        elif choice == 6:
            print('Thanks you!')
            running = False
        else:
            print("Invalid choice. Try again. ")


def menu():
    print('1. Add student')
    print('2. Edit stident')
    print('3. Delete student')
    print('4. Seach student by name')
    print('5. Show all student ')
    print('6. Quit')


def add_student(ids, names, grades):
    id = int(input('Enter student ID: '))
    name = input('Enter student name: ')
    grade = float(input('Enter student grade: '))

    ids.append(id)
    names.append(name)
    grades.append(grade)

    print(f'Student {name} successfully')

def edit_student(ids, names, grades):
    id = int(input('Enter student ID: '))
    new_name = input('Enter new name: ')
    new_grade = float(input("Enter new grade: "))

    for i in range(len(ids)):
        if ids[i] == id:
            names[i] = new_name
            grades[i] = new_grade
            print(f'Student {id} has been editted')
            return
        print(f'Student {id} not found')

def delete_student(ids, names, grades):
    id = int(input('Enter student ID: '))
    for i in range(len[ids]):
        if ids[i] == id:
            ids.pop(i)
            names.pop(i)
            grades.pop(i)
            print(f'Student {id} has been deleted')
            return
        print(f'Student {id} not found')

def seach_student(ids, names, grades):
    student = []
    name = input("Enter student name: ")
    for stdname in names:
        if name.lower() in stdname.lower():
            student.append(stdname)
    if seach_student: 
        return print("Các học sinh có tên chứa '{}' là: {}".format(name, seach_student))
    else: 
        return print("Không có học sinh nào có tên chứa '{}'.".format(name))
    
            
        

def show_all(ids, names, grades):
    for i in range(len(ids)):
        print(f'ID: {ids[i]}| Name: {names[i]}| Grade: {grades[i]}|')

main()
    