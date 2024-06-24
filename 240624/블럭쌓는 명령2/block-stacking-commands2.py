n, k = map(int, input().split())

blocks = [0] * n

for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        blocks[j] += 1

print(max(blocks))