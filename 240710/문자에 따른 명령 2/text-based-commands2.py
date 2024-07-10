command = input()

command_len = len(command)

# 남 서 북 동
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]


face = 2
x, y = 0, 0
for i in range(command_len):
    if command[i] == "L":
        if face == 0:
            face = 3
        elif face == 1:
            face = 0
        elif face == 2:
            face = 1
        else:
            face = 2

    elif command[i] == "R":
        if face == 0:
            face = 1
        elif face == 1:
            face = 2
        elif face == 2:
            face = 3
        else:
            face = 0   
    else:
        x += dx[face]
        y += dy[face]

print(x, y)