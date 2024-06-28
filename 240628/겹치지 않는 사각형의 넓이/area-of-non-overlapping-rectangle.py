arr = [[0] * 2001 for _ in range(2001)]

for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1+ 1000, y2+ 1000 ):
        for x in range(x1 + 1000, x2 + 1000):
            if i == 2:
                arr[y][x] += 2
            else:
                arr[y][x] += 1

ans = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            ans += 1

print(ans)