N = int(input())

def f(n):
    if n == 1:
        return 2
    
    if n == 2:
        return 4
    
    return (f(n - 1) * f(n - 2)) % 100


print(f(5))