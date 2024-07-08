N, K, P, T = map(int, input().split())

Developer = [0] * (N + 1)
Developer[P] = K + 1
diary = []

for t in range(T):
    diary_handshaking = tuple(map(int, input().split()))
    diary.append(diary_handshaking)

diary.sort(key=lambda x: x[0])

for time, person1, person2 in diary:
    # 감염시킬 수 있는 사람인 지 확인
    if Developer[person1] > 1:
        if Developer[person2] > 1:
            Developer[person1] -= 1
            Developer[person2] -= 1
        elif Developer[person2] == 1:
            Developer[person1] -= 1
        else:
            Developer[person1] -= 1
            Developer[person2] = K + 1
        continue

    if Developer[person2] > 1:
        if Developer[person1] > 1:
            Developer[person1] -= 1
            Developer[person2] -= 1
        elif Developer[person1] == 1:
            Developer[person2] -= 1
        else:
            Developer[person2] -= 1
            Developer[person1] = K + 1


for _ in range(1, N + 1):
    if Developer[_] > 0:
        print(1, end="")
    else:
        print(0, end="")