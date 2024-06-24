a, b = map(int, input().split())
n = list(input())

n_len = len(n)

n_to_10 = 0
for i in range(n_len):
    if int(n[i]) > 0:
        n_to_10 += (int(n[i])) * (a **(n_len - i - 1))


ans = []

while True:
    if n_to_10 < b:
        ans.append(n_to_10)
        break

    ans.append(n_to_10 % b)
    n_to_10 //= b

ans.reverse()
for j in ans:
    print(j,end="")