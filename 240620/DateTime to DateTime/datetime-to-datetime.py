a, b, c = map(int, input().split())

if a <= 11 and b <= 11 and c < 11:
    print(-1)

day, hour, minute = 0, 0, 0

if c < 11:
    hour -= 1
    minute = 60 - (11 - c)
else:
    minute = c - 11

if b < 11:
    day -= 1
    hour += 12 - (11 - b)
else:
    hour += b - 11

if a > 11:
    day += a - 11 + 1

print(day, hour, minute)


if day > 1:
    print(day * 1440 + hour * 60 + minute - (11 * 60 + 10 + 50))
else:
    print(day * 1440 + hour * 60 + minute)