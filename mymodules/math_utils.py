from mymodules import models

def average_grade(studentRoster):
    averageClassScore = 0
    for students in studentRoster:
        averageClassScore = averageClassScore + students.get_grade()

    return averageClassScore/len(studentRoster)
