n, m = map(int, input().split())

a = max(n, m)

ans = 1
for i in range(1, a + 1):
    if n % i == 0 and m % i == 0:
        ans = i

print(ans)