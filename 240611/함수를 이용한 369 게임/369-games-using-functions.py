a, b = map(int, input().split())

check = ["3", "6", "9"]

cnt = 0 
for i in range(a, b + 1):
    if str(i)[0] in check or str(i)[1] in check:
        cnt += 1
        continue
    if i % 3 == 0:
        cnt += 1

print(cnt)