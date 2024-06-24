n = int(input())

block = [0] * (201)

for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1 + 100, x2 + 100):
        if block[j] > 0 and block[j + 1] > 0:
            block[j] += 1

        if block[j] == 0:
            block[j] += 1

print(max(block))