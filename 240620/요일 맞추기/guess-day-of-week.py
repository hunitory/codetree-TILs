m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

standard_day = sum(num_of_days[:m1]) + d1

problem_day = sum(num_of_days[:m2]) + d2

diff_day = problem_day - standard_day


print(f'{days[diff_day // 7]}')