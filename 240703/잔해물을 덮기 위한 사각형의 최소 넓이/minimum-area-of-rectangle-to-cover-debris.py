N = 2
matrix = 2001

arr = [[0] * matrix for _ in range(matrix)]

ans = 0

for i in range(1, N + 1):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1 + 1000, y2 + 1000 + 1):
        for x in range(x1 + 1000, x2 + 1000 + 1):
            if i == 1:
                ans += 1
                arr[y][x] += 1
            else:
                if arr[y][x] == 1:
                    ans -= 1


print(ans)