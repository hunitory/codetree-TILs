a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        continue
    
    a = str(i)
    a_len = len(a)
    if a[a_len - 1] == '5':
        continue
    
    if i % 3 == 0 and i % 9 != 0:
        continue
    
    ans += 1
    

print(ans)