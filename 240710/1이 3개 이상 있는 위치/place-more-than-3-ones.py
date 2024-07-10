# 남 서 북 동
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for y in range(n):
    for x in range(n):
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 1:
                cnt += 1
        
        if cnt >= 3:
            ans += 1

print(ans)