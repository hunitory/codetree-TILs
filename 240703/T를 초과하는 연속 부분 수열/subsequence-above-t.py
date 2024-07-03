n, t = map(int, input().split())

num_list = list(map(int, input().split()))

ans,cnt = 0, 0 

for i in range(n):
    if i >= 1 and num_list[i] > t and num_list[i - 1] > t:
        if num_list[i] > num_list[i - 1]:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)