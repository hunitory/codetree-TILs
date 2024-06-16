n = int(input()) # 그룹 수


num_list = list(map(int, input().split()))

num_list.sort()

min_nums = num_list[:n]
max_nums = num_list[n:]

ans = 0
for i in range(n):
    if min_nums[i] + max_nums[n - i - 1] > ans:
        ans = min_nums[i] + max_nums[n - i - 1]

print(ans)