matrix = 201
offset = 100

arr = [[0] * matrix for _ in range(matrix)]

n = int(input())

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # 빨간색
    if i % 2 == 0:
        for y in range(y1 + offset, y2 + offset):
            for x in range(x1 + offset, x2 + offset):
                arr[y][x] = 1

    # 파란색
    else:
        for y in range(y1 + offset, y2 + offset):
            for x in range(x1 + offset, x2 + offset):
                arr[y][x] = 2

ans = 0
for i in range(matrix):
    for j in range(matrix):
        if arr[i][j] == 2:
            ans += 1

print(ans)