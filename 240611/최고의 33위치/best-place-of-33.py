N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans= 0

for y in range(1, N - 1):
    for x in range(1, N - 1):
        cnt = 0
        for yy in range(3):
            for xx in range(3):
                if arr[y + yy - 1][x + xx - 1] == 1:
                    cnt += 1

        if cnt > ans:
            ans = cnt


print(ans)