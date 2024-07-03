n = int(input())

num_list = [int(input()) for _ in range(n)]

ans, cnt = 0 , 0
for i in range(1, n):
    # 곱해서 음수 -> 부호가 다르다는 것
    if num_list[i] * num_list[i - 1] < 0:
        cnt = 1
    else:
        cnt += 1
    
    ans = max(ans, cnt)

print(ans)