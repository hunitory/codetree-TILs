n, m = map(int, input().split())

# 우, 하, 좌, 상
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

arr = [[0] * m for _ in range(n)]
x, y = 0, 0
arr[y][x] = 1
direction = 0

for i in range(2, n * m + 1):
    nx, ny = x + dx[direction], y + dy[direction]

    if not 0 <= nx < m or not 0 <= ny < n:
        direction = (direction + 1) % 4
    
    x, y = x + dx[direction], y + dy[direction]
    arr[y][x] = i

for ar in arr:
    print(*ar)