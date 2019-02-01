from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():
    studentRoster = []
    studentRoster.append(Student("Salman", 100))
    studentRoster.append(Student("Rick", 95))
    studentRoster.append(Student("Shivam", 79))
    studentRoster.append(Student("Davian", 88))
    studentRoster.append(Student("Puneet", 67))
    studentRoster.append(Student("Jessica", 46))
    studentRoster.append(Student("Michelle", 93))
    studentRoster.append(Student("Kim", 57))
    studentRoster.append(Student("Tiffany", 91))
    studentRoster.append(Student("Brianna", 64))

    for students in studentRoster:
        students.print_student_info()

    print(f"The average grade of all students in the class is: {average_grade(studentRoster)}")

__main__()
