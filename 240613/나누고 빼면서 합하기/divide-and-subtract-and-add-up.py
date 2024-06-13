n, m = map(int, input().split()) # n개의 원소, target 넘버

A = list(map(int, input().split()))

def f(n, m):
    ans = 0
    while m != 1:
        ans += A[m - 1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    
    return ans

print(f(n, m) + A[0])