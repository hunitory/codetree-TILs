import math

N = int(input())

mirrors = []

for i in range(N):
    mirrors.append(input())

K = int(input())

maps = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if mirrors[y][x] == "/":
            maps[y][x] = 0
        else:
            maps[y][x] = 1

# 0 : 남, 1 : 서, 2 : 북, 3 : 동
current_direction = math.ceil(K / N) - 1

lazer_location = (K - 1) % N

x, y = 0, 0
if current_direction == 0:
    x, y = lazer_location, 0
elif current_direction == 1:
    x, y = N - 1, lazer_location
elif current_direction == 2:
    x, y = N - 1 - lazer_location, N - 1
else:
    x, y = 0, N - 1 - lazer_location

ans = 0

while 0 <= x < N and 0 <= y < N:
    ans += 1
    if current_direction == 0:
        if maps[y][x]:
            current_direction = 3
            x += 1
        else:
            current_direction = 1
            x -= 1
    
    elif current_direction == 1:
        if maps[y][x]:
            current_direction = 2
            y -= 1
        else:
            current_direction = 0
            y += 1
    elif current_direction == 2:
        if maps[y][x]:
            current_direction = 1
            x -= 1
        else:
            current_direction = 3
            x += 1
    else:
        if maps[y][x]:
            current_direction = 0
            y += 1
        else:
            current_direction = 2
            y -= 1
print(ans)