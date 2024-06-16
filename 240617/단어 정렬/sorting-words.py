n = int(input())

st_list = [input() for _ in range(n)]

st_list.sort()

for st in st_list:
    print(st)