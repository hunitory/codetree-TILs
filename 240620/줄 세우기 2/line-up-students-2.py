class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number


N = int(input())

students = []
for i in range(1, N + 1):
    height, weight = map(int, input().split())
    number = i
    students.append(Student(height, weight, i))

students.sort(key=lambda x:(x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.number)