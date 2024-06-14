n = int(input())

def sequence(n, cnt):
    if n == 1:
        return cnt
    
    if n % 2 == 0:
        return sequence(n // 2, cnt + 1)
    else:
        return sequence((3 * n) + 1, cnt + 1)

print(sequence(n, 0))