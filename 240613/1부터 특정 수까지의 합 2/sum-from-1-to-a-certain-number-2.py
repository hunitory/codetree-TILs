N = int(input())

def sum_f(n):
    if n == 1 :
        return 1

    return sum_f(n-1) + n

print(sum_f(N))