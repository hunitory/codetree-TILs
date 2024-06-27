n = int(input())

line = [0] * 2001

start = 1000
for i in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for j in range(int(a) + 1):
            if line[start] == 0:
                line[start] += 1
                start += 1
                continue

            if line[start + 1] > 0:
                line[start] += 1
                start += 1

    else:
        start -= int(a) + 1
        for j in range(int(a) + 1):
            if line[start] == 0:
                line[start] += 1
                start += 1
                continue

            if line[start + 1] > 0:
                line[start] += 1
                start += 1

count = len(list(filter(lambda x: x > 1, line)))

print(count)