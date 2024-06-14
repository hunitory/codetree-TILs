N = int(input())

def print_num(N):
    if N <= 2:
        return N
    
    return N + print_num(N - 2)

print(print_num(N))