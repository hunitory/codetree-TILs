N = list(input())

N_len = len(N)

ans = 0
for i in range(N_len):
    if N[i] == "1":
        ans += 2 ** (N_len - 1 - i)

ans *= 17

ans_digits = []
while True:
    if ans < 2:
        ans_digits.append(ans)
        break
    
    ans_digits.append(ans % 2)
    ans //= 2

ans_digits.reverse()
for i in ans_digits:
    print(i, end="")