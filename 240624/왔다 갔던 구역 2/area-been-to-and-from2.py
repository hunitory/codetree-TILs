n = int(input())

line = [0] * 2001

start = 1000

for i in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for j in range(int(a) + 1):
            start += j
            line[start] += 1
    else:
        for j in range(int(a) + 1):
            start -= j
            line[start] += 1

ans = 0
for li in line:
    if li > 1:
        ans += 1 

print(ans)