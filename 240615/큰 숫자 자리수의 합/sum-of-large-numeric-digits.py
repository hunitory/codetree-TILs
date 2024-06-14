number_list = list(map(int, input().split()))

def sum_seat(n):
    if n == 0:
        return 0

    return (n % 10) + sum_seat(n // 10)

target = 1
for number in number_list:
    target *= number

print(sum_seat(target))