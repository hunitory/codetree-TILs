N, M = map(int, input().split())

N_distance = [0]
M_distance = [0]

total_time = 0

N_location = 0
M_location = 0


for n in range(N):
    Nv, Nt = map(int, input().split())
    total_time += Nt
    for vt in range(Nt):
        N_location += Nv
        N_distance.append(N_location)

for m in range(M):
    Mv, Mt = map(int, input().split())
    for mt in range(Mt):
        M_location += Mv
        M_distance.append(M_location)

cnt = 0
flag = ""
for k in range(1, total_time):
    if not flag:
        if N_distance[k] > M_distance[k]:
            flag = "N"
        elif N_distance[k] < M_distance[k]:
            flag = "M"

    else:
        if flag == "N" and N_distance[k] < M_distance[k]:
            cnt += 1
            flag = "M"

        elif flag == "M" and N_distance[k] > M_distance[k]:
            cnt += 1
            flag = "N"

print(cnt)