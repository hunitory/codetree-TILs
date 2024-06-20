a, b, c, d = map(int, input().split())

h, m = 0, 0

h = c - a
if b <= d:
    m = b - d
else:
    m = d + 60 - b
    h -= 1

print(h * 60 + m)