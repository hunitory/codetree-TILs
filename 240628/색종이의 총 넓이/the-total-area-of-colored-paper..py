N = int(input())

matrix = 201

arr = [[0] * matrix for _ in range(matrix)]

for i in range(N):
    sx, sy = map(int, input().split())
    for y in range(8):
        for x in range(8):
            arr[sy + y][sx + x] += 1

ans = 0

for i in range(matrix):
    for j in range(matrix):
        if arr[i][j] > 0:
            ans += 1

print(ans)