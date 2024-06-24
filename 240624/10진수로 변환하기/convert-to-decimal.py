target = list(input())

target_len = len(target)

ans = 0
for i in range(target_len):
    if target[i] == '1':
        ans += 2 ** (target_len - i - 1)

print(ans)