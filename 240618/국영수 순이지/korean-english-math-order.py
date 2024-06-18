# 클래스 선언
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


# 변수 선언 및 입력
n = int(input())
students = []
for _ in range(n):
    name, korean, english, math = tuple(input().split())
    students.append(Student(name, int(korean), int(english), int(math)))

# Custom Comparator를 활용한 정렬
students.sort(key = lambda x: (-x.korean, -x.english, -x.math))

# 출력
for student in students:
    print(student.name, student.korean, student.english, student.math)