N, M, K = map(int, input().split())  # 학생 수 , 벌금 부여 수, 벌칙 최대 

students = [0] * (N + 1)

for m in range(M):
    punish = int(input())
    students[punish] += 1
    if students[punish] >= K:
        print(punish)
        break

else:
    print(-1)