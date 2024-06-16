n, k, T = map(str, input().split())

words = [input() for _ in range(int(n))]

words.sort()

T_len = len(T)
ans = ''
cnt = 0
for word in words:
    try:
        if word[:T_len] == T:
            cnt += 1
        if cnt == int(k):
            ans = word
            break
    except:
        continue

print(ans)