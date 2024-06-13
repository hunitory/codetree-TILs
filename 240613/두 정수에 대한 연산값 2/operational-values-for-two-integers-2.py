a, b = map(int, input().split())

def f(a, b):
    if max(a,b) == a:
        return a * 2, b + 10
    else:
        return a + 10, b * 2

a, b = f(a, b)
print(a, b)