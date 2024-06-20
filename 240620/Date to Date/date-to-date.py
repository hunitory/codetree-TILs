num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

ans = 0

month, day = 0, 0 

month = m2 - m1
if month >= 2:
    ans += sum(num_of_days[m1 + 1: m2])
    ans += num_of_days[m1] - d1 + 1
    ans += d2
elif month == 1:
    ans += num_of_days[m1] - d1 + 1
    ans += d2
else:
    ans = d2 - d1 + 1

print(ans)