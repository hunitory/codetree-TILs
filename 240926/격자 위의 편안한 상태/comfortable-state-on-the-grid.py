dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_comport_state(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if maps[ny][nx]:
                cnt += 1
    
    if cnt == 3:
        return True

    return False
    

N, M = map(int, input().split())

paintings = []

for i in range(M):
    x, y = map(int, input().split())
    paintings.append((x - 1, y -1 ))

maps = [[0] * N for i in range(N)]

for x, y in paintings:
    maps[y][x] = 1
    if check_comport_state(x, y):
        print(1)
        continue
    print(0)