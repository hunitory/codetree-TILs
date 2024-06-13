a, b = map(int, input().split())

def f(a, b):
    if max(a, b) == a:
        return a + 25, b * 2
    else:
        return a * 2, b + 25

a, b = f(a, b)
print(a, b)