# 남 서 북 동
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

n, t = map(int, input().split())

r, c, d = map(str, input().split())

if d == "L": d = 1
if d == "U": d = 2
if d == "D": d = 0
if d == "R": d = 3



x, y = int(c) - 1, int(r) - 1

for time in range(t):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny
    else:
        if d == 1: d = 3
        elif d == 2: d = 0
        elif d == 0: d = 2
        elif d == 3: d = 1

print(y + 1, x + 1)