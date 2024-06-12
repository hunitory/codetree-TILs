n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sub = [[]]

for num in A:
    size = len(A_sub)
    for i in range(size):
        A_sub.append(A_sub[i] + [num])

if B in A_sub:
    print('Yes')
else:
    print('No')