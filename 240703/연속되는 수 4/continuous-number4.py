n = int(input())

num_list = [int(input()) for _ in range(n)]

ans, cnt = 0 , 0
for i in range(n - 1):
    if num_list[i] < num_list[i + 1]:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)