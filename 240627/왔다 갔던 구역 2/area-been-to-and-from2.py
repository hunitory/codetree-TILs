n = int(input())

make = 2000
start = make // 2
line = [0] * make

for i in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for j in range(int(a)):
            line[start] += 1
            start += 1

    else:
        for j in range(int(a)):
            start -= 1
            line[start] += 1


count = len(list(filter(lambda x : x > 1, line)))

print(count)