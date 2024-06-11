N = int(input())

start = 1
for i in range(N):
    for i in range(N):
        print(start, end=' ')
        start += 1
        if start == 10:
            start = 1
    print()