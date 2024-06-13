N = int(input())

def print_star(cnt):
    if cnt == 0:
        return

    print("*" * (N - cnt + 1))
    print_star(cnt - 1)

print_star(N)