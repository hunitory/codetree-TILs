n = int(input())

students= []

for i in range(n):
    name, kor, eng, math = map(str, input().split())
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for student in students:
    print(*student)