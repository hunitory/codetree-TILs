n = int(input())

num_list = [int(input()) for _ in range(n)]

ans, cnt = 0 , 0
for i in range(n):
    if i >= 1 and num_list[i] < num_list[i - 1]:
        cnt = 0
    else:
        cnt += 1
    
    ans = max(ans, cnt)

print(ans)