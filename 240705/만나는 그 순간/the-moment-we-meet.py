N, M = map(int, input().split())

A_command = [0]
B_command = [0]

total_time = 0
A_time = 0
A_location = 0

for i in range(N):
    d, t = map(str, input().split())
    t = int(t)
    total_time += t
    if d == "R":
        for j in range(t):
            A_location += 1
            A_command.append(A_location)
    else:
        for j in range(t):
            A_location -= 1
            A_command.append(A_location)

B_location = 0

for i in range(M):
    Bd, Bt = map(str, input().split())
    Bt = int(Bt)
    if Bd == "R":
        for j in range(Bt):
            B_location += 1
            B_command.append(B_location)
    else:
        for j in range(Bt):
            B_location -= 1
            B_command.append(B_location)

for k in range(1, total_time):
    if A_command[k] == B_command[k]:
        print(k)
        break