n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_len = len(A)
A_sub = []

for i in range(A_len):
    start = [A[i]]
    A_sub.append(start.copy())  # 리스트의 복사본 추가
    cnt = 0
    for j in range(i + 1, A_len):
        cnt += 1
        start.append(A[j])
        A_sub.append(start.copy())  # 리스트의 복사본 추가


if B in A_sub:
    print('Yes')
else:
    print('No')