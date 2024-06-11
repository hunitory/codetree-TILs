a, b = map(int, input().split())

check = ["3", "6", "9"]
def check_369(n):
    n_len = len(n)
    for j in range(n_len):
        if n[j] in check:
            return True
            
    return False

def can_div(n):
    return (n % 3 == 0)

cnt = 0 
for i in range(a, b + 1):
    if check_369(str(i)) or can_div(i):
        cnt += 1

print(cnt)