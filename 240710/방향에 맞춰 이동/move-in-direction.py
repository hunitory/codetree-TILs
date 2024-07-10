N = int(input())

x, y = 0, 0

for _ in range(N):
    Direction, Distance = map(str, input().split())
    if Direction == "N":
        y += int(Distance)
    elif Direction == "S":
        y -= int(Distance)
    elif Direction == "E":
        x += int(Distance)
    elif Direction == "W":
        x -= int(Distance)


print(x, y)