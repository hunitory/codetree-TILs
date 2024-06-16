n = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()

if A_list == B_list:
    print('Yes')
else:
    print('No')