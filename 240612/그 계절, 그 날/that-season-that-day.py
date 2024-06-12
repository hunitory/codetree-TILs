import datetime

Spring = [_ for _ in range(3,6)]
Summer = [_ for _ in range(6,9)]
Fall = [_ for _ in range(9,12)]
Winter = [1,2,12]

Y, M, D = map(int, input().split())


try:
    date = datetime.datetime(Y, M, D)
    if M in Spring:
        print('Spring')
    elif M in Summer:
        print('Summer')
    elif M in Fall:
        print('Fall')
    else:
        print('Winter')
    
except ValueError:
    print(-1)