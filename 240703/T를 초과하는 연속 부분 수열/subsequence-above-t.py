n, t = map(int, input().split())

num_list = list(map(int, input().split()))

ans,cnt = 0, 0 

for i in range(n):
    if i >= 1 and num_list[i] > t and num_list[i - 1] > t:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

if ans == 0:
    print(0)
else:
    print(ans)