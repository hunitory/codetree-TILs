n = int(input())

num_list = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        print(num_list[i // 2], end=" ")