import math

a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1 ):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        c = str(i)
        if len(c) > 1:
            if (int(c[0]) + int(c[1])) % 2 == 0:
                ans += 1

print(ans)