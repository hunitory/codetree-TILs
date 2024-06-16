n, k = map(int, input().split()) # n 개의 숫자, k 번째 숫자

num_list = list(map(int, input().split()))

num_list.sort()
print(num_list[k])