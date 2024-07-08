MAX_T = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매 초마다 서있는 위치를 기록
time_a = 1
for _ in range(n):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

# B가 매 초마다 서있는 위치를 기록
time_b = 1
for _ in range(m):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

if time_a < time_b:
	for i in range(time_a, time_b):
		pos_a[i] = pos_a[i - 1]
elif time_a > time_b:
	for i in range(time_b, time_a):
		pos_b[i] = pos_b[i - 1]

# 새롭게 만나는 횟수를 구합니다.
cnt = 0
time_max = max(time_a, time_b)
for i in range(1, time_max):
    if pos_a[i] == pos_b[i] and pos_a[i - 1] != pos_b[i - 1]:
        cnt += 1
        
print(cnt)