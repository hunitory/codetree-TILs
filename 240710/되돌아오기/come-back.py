# 우, 하, 좌, 상
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


N = int(input())

ans = 0
x, y = 0, 0


for n in range(N):
    Direction, Time = map(str, input().split())
    Time = int(Time)

    if Direction == 'W': Direction = 0
    elif Direction == 'S': Direction = 1
    elif Direction == 'N': Direction = 3
    else: Direction = 2

    for time in range(Time):
        ans += 1
        x, y = x + dx[Direction], y + dy[Direction]
        if x == 0 and y == 0:
            break
    
    if x == 0 and y == 0:
        print(ans)
        break

else:
    print(-1)