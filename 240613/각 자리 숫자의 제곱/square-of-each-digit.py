N = int(input())

def f(n):
    if n == 0 :
        return 0

    return f(n // 10) + (n % 10) ** 2

print(f(N))