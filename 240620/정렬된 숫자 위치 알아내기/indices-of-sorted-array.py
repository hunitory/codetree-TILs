n = int(input())

num_list = list(map(int, input().split()))

# 3 1 6 2 7 30 1
# 1 1 2 3 6 7 30

num_list2 = num_list.copy()
num_list2.sort()

for i in range(n):
    for j in range(n):
        if num_list[i] == num_list2[j]:
            num_list[i] = j + 1
            num_list2[j] = 0
            break

print(*num_list)