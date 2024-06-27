n = int(input())

line_len = 3000000
start = line_len // 2
line = [""] * line_len

for i in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for j in range(int(a)):
            line[start] += "B"
            start += 1

        start -= 1

    else:
        for j in range(int(a)):
            line[start] += "W"
            start -= 1

        start += 1



W, B, G = 0, 0, 0

for k in line:
    if len(k) > 0:
        if len(k) > 3:
            G += 1
        else:
            if k[-1] == "W":
                W += 1
            else:
                B += 1

print(W, B, G)