import math

a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    if i == 1:
        continue
    cnt = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
           cnt += 1

    if cnt == 0 :
         ans += i
        

print(ans)