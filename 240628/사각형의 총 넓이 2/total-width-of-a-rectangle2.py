N = int(input())

arr = [[0] * 201 for _ in range(201)]

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1+ 100, y2+ 100 ):
        for x in range(x1 + 100, x2 + 100):
            arr[y][x] += 1

ans = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] > 0:
            ans += 1

print(ans)