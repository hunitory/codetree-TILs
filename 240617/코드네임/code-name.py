class student:
    def __init__(self, codeName, score):
        self.codeName = codeName
        self.score = score
        
students = []
for i in range(5):
    input_info = input().split()
    students.append(student(input_info[0], int(input_info[1])))

ans = min(students, key=lambda x:x.score)
print(ans.codeName, ans.score)