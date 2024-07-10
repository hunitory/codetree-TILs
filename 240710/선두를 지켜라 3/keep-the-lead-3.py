N, M = map(int, input().split())

N_move = [0]
M_move = [0]

total_time = 1

for n in range(N):
    v, t = map(int, input().split())
    total_time += t
    for nt in range(t):
        N_move.append(N_move[-1] + (v))


for m in range(M):
    v, t = map(int, input().split())
    for mt in range(t):
        M_move.append(M_move[-1] + (v))


honor = "NM"
cnt = 0
for time in range(total_time):
    if honor == "NM":
        if N_move[time] > M_move[time]:
            honor = "N"
            cnt += 1
        elif N_move[time] < M_move[time]:
            honor = "M"
            cnt += 1
        

    elif honor == "N":
        if N_move[time] == M_move[time]:
            honor = "NM"
            cnt += 1
        elif N_move[time] < M_move[time]:
            honor = "M"
            cnt += 1

    elif honor == "M":
        if N_move[time] > M_move[time]:
            honor = "N"
            cnt += 1
        elif N_move[time] == M_move[time]:
            honor = "NM"
            cnt += 1

print(cnt)