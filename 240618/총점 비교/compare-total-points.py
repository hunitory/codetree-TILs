class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


    def __str__(self):
        return f"{self.name} {self.kor} {self.eng} {self.math}"

        
n = int(input())

students = []
for i in range(n):
    name, kor, eng, math = input().split()
    students.append(Student(name, int(kor), int(eng), int(math)))

students.sort(key=lambda x: (x.kor + x.eng + x.math))

for student in students:
    print(student)