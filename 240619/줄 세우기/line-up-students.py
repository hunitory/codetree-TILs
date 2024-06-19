n = int(input())

students = []
for i in range(1, n + 1):
    number = i
    high, weight = map(int, input().split())
    students.append((high, weight, number))

students.sort(key=lambda x:(-x[0], -x[1], -x[2]))

for student in students:
    print(*student)