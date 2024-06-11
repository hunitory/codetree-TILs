a, b = map(int, input().split())

check = ["3", "6", "9"]
def check_369(n):
    return str(n)[0] in check or str(n)[1] in check

def can_div(n):
    return (n % 3 == 0)

cnt = 0 
for i in range(a, b + 1):
    if check_369(i) or can_div(i):
        cnt += 1

print(cnt)