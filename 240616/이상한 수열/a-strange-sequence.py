N = int(input())

def odd(N):
    if N == 1 :
        return 1
    
    if N == 2:
        return 2
    
    return odd(N-1) + odd(N // 3)

print(odd(N))