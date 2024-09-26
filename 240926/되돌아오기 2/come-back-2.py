commands = input()
# 상, 우, 하, 좌
direction = [0, 1, 2, 3]

ans = -1
x, y = 0, 0
current_time = 0
current_direction = 0

commands_len = len(commands)

for i in range(commands_len):
    if commands[i] == 'F':
        if current_direction == 0:
            y += 1
        elif current_direction == 2:
            y -= 1
        elif current_direction == 1:
            x -= 1
        else:
            x += 1

    else:
        if commands[i] == 'L':
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4

    current_time += 1
    if x == 0 and y == 0:
        ans = current_time
        break

print(ans)