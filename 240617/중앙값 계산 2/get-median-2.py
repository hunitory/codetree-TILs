n = int(input())

num_list = list(map(int, input().split()))

ans_list = []
for i in range(n):
    ans_list.append(num_list[i])
    ans_list.sort()
    if i % 2 == 0:
        print(ans_list[i // 2], end=" ")