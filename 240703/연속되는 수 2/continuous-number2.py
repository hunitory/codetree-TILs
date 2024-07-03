n = int(input())

num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

max_cnt = 1
cnt = 0

for i in range(1, n):
    if num_list[i - 1] == num_list[i]:
        cnt += 1
    else:
        if max_cnt < cnt :
            max_cnt = cnt
        cnt = 0

if max_cnt < cnt :
    max_cnt = cnt
    
print(max_cnt + 1)