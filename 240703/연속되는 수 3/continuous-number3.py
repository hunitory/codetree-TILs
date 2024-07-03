n = int(input())

num_list = [int(input()) for _ in range(n)]

ans, cnt = 0 , 1
for i in range(n):
    # 곱해서 음수 -> 부호가 다르다는 것
    if i >= 1 and num_list[i] * num_list[i - 1] < 0:
        cnt = 1
    else:
        cnt += 1
    
    ans = max(ans, cnt)

print(ans)