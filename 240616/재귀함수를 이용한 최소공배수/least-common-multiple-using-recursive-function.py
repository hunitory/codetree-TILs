import math

n = int(input())

num_list = list(map(int, input().split()))

print(math.lcm(*num_list))