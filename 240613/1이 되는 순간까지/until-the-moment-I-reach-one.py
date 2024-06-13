N = int(input())

cnt = 0
def go_1(N):
    global cnt

    if N == 1:
        return

    cnt += 1
    if N % 2 ==0:
        go_1(N // 2)
    else:
        go_1(N // 3)

go_1(N)
print(cnt)