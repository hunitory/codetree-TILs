matrix = 2001
offset = 1000

arr = [[0] * matrix for _ in range(matrix)]

mx1, my1, mx2, my2 = 0, 0, 0, 0

for i in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    if i == 1:
        mx1, my1, mx2, my2 = x1, y1, x2, y2

    for y in range(y1 + offset, y2 + offset + 1):
        for x in range(x1 + offset, x2 + offset + 1):
            arr[y][x] += i

ax, ay = 0, 0

for i in range(my1 + offset, my2 + offset + 1):
    x = 0
    dx = 0
    for j in range(mx1 + offset, mx2 + offset + 1):
        if arr[i][j] == 1:
            x += 1
            if dx > 0 :
                x += dx
                dx = 0
        else:
            dx += 1

    if x > ax:
        ax = x

for i in range(mx1 + offset, mx2 + offset + 1):
    y = 0
    dy = 0
    for j in range(my1 + offset, my2 + offset + 1):
        if arr[j][i] == 1:
            y += 1
            if dy > 0 :
                y += dy
                dy = 0
        else:
            dy += 1

    if y > ay:
        ay = y

print(ax, ay)
if ax == 0 or ay == 0:
    print(0)
else:
    print((ax - 1) * (ay - 1))