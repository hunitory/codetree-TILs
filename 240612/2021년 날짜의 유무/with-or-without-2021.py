import datetime

M, D = map(int, input().split())

try:
    date = datetime.datetime(2021, M, D)
    print("Yes")
except ValueError:
    print("No")