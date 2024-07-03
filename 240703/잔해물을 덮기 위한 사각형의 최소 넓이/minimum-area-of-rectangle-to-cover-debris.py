matrix = 2001
offset = 1000

arr = [[0] * matrix for _ in range(matrix)]

mx1, my1, mx2, my2 = 0, 0, 0, 0

for i in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    if i == 1:
        mx1, my1, mx2, my2 = x1, y1, x2, y2

    for y in range(y1 + offset, y2 + offset):
        for x in range(x1 + offset, x2 + offset):
            arr[y][x] = i

ax, ay = 0, 0

for ii in range(my1 + offset, my2 + offset):
    x = 0
    dx = 0
    for jj in range(mx1 + offset, mx2 + offset):
        if arr[ii][jj] == 1:
            x += 1
            if dx > 0:
                x += dx
                dx = 0
        else:
            if x > 0:
                dx += 1

    if x > ax:
        ax = x

for iii in range(mx1 + offset, mx2 + offset):
    y = 0
    dy = 0
    for jjj in range(my1 + offset, my2 + offset):
        if arr[jjj][iii] == 1:
            y += 1
            if dy > 0:
                y += dy
                dy = 0
        else:
            if y > 0:
                dy += 1

    if y > ay:
        ay = y

if ax == 0 or ay == 0:
    print(0)
else:
    print((ax) * (ay))