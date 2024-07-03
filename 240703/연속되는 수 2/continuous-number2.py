n = int(input())

num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

ans = 0
cnt = 0

for i in range(n - 1):
    if num_list[i] == num_list[i + 1]:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
            cnt = 0

print(ans + 1)