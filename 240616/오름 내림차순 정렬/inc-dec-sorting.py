n = int(input())

num_list = list(map(int, input().split()))

print(*sorted(num_list))
print(*sorted(num_list, reverse=True))